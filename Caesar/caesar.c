#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>


int main(int argc, string argv[])

{
  if (argc != 2)
  {
   printf("Please enter one command line argument!\n");
   return 1;
  }
  else
  {
   string text= get_string("plaintext: ");
   printf("ciphertext: ");
   for (int i=0,n=strlen(text); i < n; i++)
    {
     if (islower(text[i]))
      {
       //Checks if the key makes text[i] become a non-letter(lowercase)
       if (atoi(argv[1]) <= 25 && (int) text[i] + atoi(argv[1]) > 122)
        {
        //If yes, shift text[i] by 26 minus key, to go back to beginning of alphabet
        text[i]=(int) text[i] - (26 -(atoi(argv[1])));
        printf("%c", text[i]);
        }
          //If argument is greater than 26,  modulo (%) then do as above
       else if (atoi(argv[1]) > 26 && ((int) text[i] + (atoi(argv[1]) % 26))>122)
        {
         text[i]=(int) text[i] - (26-(atoi(argv[1]) % 26));
         printf("%c", text[i]);
        }
       else if (atoi(argv[1]) > 26 && ((int) text[i] + (atoi(argv[1]) % 26)) < 122)
        {
         text[i]=(int) text[i] + (26-(atoi(argv[1]) % 26));
         printf("%c", text[i]);
        }
       else
        {
         text[i]=(int) text[i] +atoi(argv[1]);
         printf("%c", text[i]);
        }
      }
     else if (isupper(text[i]))
      {
       //Checks if the key makes text[i] become a non-letter(Uppercase)
       if (atoi(argv[1]) <= 25 && (int) text[i] + atoi(argv[1]) > 90)
        {
         //If yes, shift text[i] by 26 minus key, to go back to beginning of alphabet
         text[i]=(int) text[i] - (26 -(atoi(argv[1])));
         printf("%c", text[i]);
        }
         //If argument is greater than 26,  modulo (%) then do as above
        else if (atoi(argv[1]) > 26 && ((int) text[i] + (atoi(argv[1]) % 26)) > 90)
         {
          text[i]=(int) text[i] - (26-(atoi(argv[1]) % 26));
          printf("%c", text[i]);
         }
        else if (atoi(argv[1]) > 26 && ((int) text[i] + (atoi(argv[1]) % 26)) < 90)
         {
         text[i]=(int) text[i] + (26-(atoi(argv[1]) % 26));
          printf("%c", text[i]);
         }
        else
         {
          text[i]=(int) text[i] +atoi(argv[1]);
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
 }
