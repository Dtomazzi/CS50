// Helper functions for music

#include <string.h>
#include <stdio.h>
#include <math.h>

#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
 int numerator=(int) fraction[0];
 int denominator=(int) fraction[2];

 if (denominator == '8')
 {
   return numerator-48;
 }
 else if (denominator == '4')
 {
    return (numerator-48)*2;
 }
 else if (denominator== '2')
 {
    return (numerator-48)*4;
 }
 else
 {
    return (numerator-48)*8;
 }
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
 int base;
 //separate note from octave
 int octaves= (int) note[strlen(note)-1] - 48;
 base= 55 *pow(2.0,octaves-1.0);
//Conditions for note/octave inputs
 if (strlen(note)==2)
   {
 	if (note[0]=='A')
 	{
 	   return base;
 	}
 	else if (note[0]=='B')
 	{
 	   return round(base*pow(2.0, (2.0/12.0)));
 	}
 	else if (note[0]=='C')
 	{
 	   return round(base/pow(2.0, (9.0/12.0)));
 	}
 	else if (note[0]=='D')
 	{
 	   return round(base/pow(2.0, (7.0/12.0)));
 	}
 	else if (note[0]=='E')
 	{
 	   return round(base/pow(2.0, (5.0/12.0)));
 	}
    else if (note[0]=='F')
    {
       return round(base/pow(2.0,(4.0/12.0)));
    }
    else if (note[0]=='G')
    {
       return round(base/pow(2.0,(2.0/12.0)));
    }
    else
    {
        return 1;
    }
   }
//Conditions for '#' or 'b' in input
 else if (strlen(note)==3)
 {
   if (note[0]=='C' || (note[0]=='D' && note[1]=='b'))
   {
   	return round(base/pow(2.0,(8.0/12.0)));
   }
   else if (note[0]=='E' || (note[0]=='D' && note[1]=='#'))
   {
   	return round(base/pow(2.0,(6.0/12.0)));
   }
   else if ((note[0]=='G' && note[1]=='b') || (note[0]=='F' && note[1]=='#'))
   {
   	return round(base/pow(2.0, (3.0/12.0)));
   }
   else if ((note[0]=='A' && note[1]=='b') || (note[0]=='G' && note[1]=='#'))
   {
   	return round(base/pow(2.0, (1.0/12.0)));
   }
   else
   {
   	return round(base*pow(2.0,(1.0/12.0)));
   }
 }
 else
  {
  	return 1;
  }
}

// Determines whether a string represents a rest
bool is_rest(string s)
 {
  if (strcmp(s, "") == 0 || strcmp(s, "\n")== 0)
    {
      return true;
    }
    else
    {
      return false;
    }
}
