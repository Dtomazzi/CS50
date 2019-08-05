#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>


int main(int argc, string argv[])
{


int pos=0;
if (argc != 2)
 {
  printf("Please enter one command line argument!\n");
  return 1;
 }
else
 {
  string key=argv[1];
  int k=strlen(key);
  for (int i=0; i < k;)
   {
     if (isalpha(key[i]))
      {
       i++;
      }
    else
     {
     printf("Argument must only contain alphabetical letters!\n");
     return 1;
     }
  }
 }
 string key=argv[1];
int k=strlen(key);
string text= get_string("plaintext: ");
printf("ciphertext: ");

for (int i=0, n=strlen(text); i < n; i++)
  {
    int h=pos % k;
	   if (islower(text[i]) && islower(key[h]))
	     {
	       int cipher=(int)key[h] - 97;
	       //If key + the text is greater than 122, subtract by 26 - key
		if ((int) text[i] + cipher >122)
		  {
		      text[i]= (int) text[i] - (26 - cipher);
		      pos++;
		      printf("%c", text[i]);
		  }
                //If key + text is less than 122m, add text[i] by key
                else if ((int) text[i] + cipher  < 122)
                 {
                   text[i]=(int) text[i] + cipher;
                   pos++;
                   printf("%c", text[i]);
                 }
              }
          else if (islower(text[i]) && isupper(key[h]))
             {
                int cipher=(int)key[h] - 65;
	        //If key + the text is greater than 122, subtract by 26 - key
	        if ((int) text[i] + cipher >122)
	          {
		    text[i]= (int) text[i] - (26 - cipher);
		    pos++;
		    printf("%c", text[i]);
	           }
	         //If key + text is less than 122m, add text[i] by key
                 else if ((int) text[i] + cipher  < 122)
                   {
                    text[i]=(int) text[i] + cipher;
                    pos++;
                    printf("%c", text[i]);
                   }
              }
         else if (isupper(text[i]) && islower(key[h]))
              {
                 int cipher=(int)key[h] - 97;
		 //If key + the text is greater than 122, subtract by 26 - key
	         if ((int) text[i] + cipher >90)
		   {
		     text[i]= (int) text[i] - (26 - cipher);
		     pos++;
		     printf("%c", text[i]);
		    }
		    //If key + text is less than 122m, add text[i] by key
                 else if ((int) text[i] + cipher  < 90)
                   {
                    text[i]=(int) text[i] + cipher;
                    pos++;
                    printf("%c", text[i]);
                    }
               }
     else if (isupper(text[i]) && isupper(key[h]))
              {
               int cipher=(int)key[h] - 65;
	       //If key + the text is greater than 122, subtract by 26 - key
	        if ((int) text[i] + cipher >90)
		   {
		    text[i]= (int) text[i] - (26 - cipher);
		    pos++;
	            printf("%c", text[i]);
	            }
	           //If key + text is less than 122m, add text[i] by key
                else if ((int) text[i] + cipher  < 90)
                    {
                     text[i]=(int) text[i] + cipher;
                     pos++;
                     printf("%c", text[i]);
                     }
                   }
	else
             {
	       printf("%c", text[i]);
             }
	 }
	 printf("\n");
	 return 0;
}
