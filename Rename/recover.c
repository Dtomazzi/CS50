//Recovers JPEGS
#include <stdio.h>
#include <stdlib.h>
//Borrowed idea of using BYTE for buffer from cs50.stackexchange.com/questions/2680/
//what-data-structure-do-you-use-to-store-the-buffer-in-recover
// Originally, was using "char buffer[512];"

 typedef unsigned char BYTE;

int main (int argc, char *argv[])
{

BYTE buffer[512];
char *infiles=argv[1];
char filename[8];
int fcount=0;

   if (argc !=2)
    {
       fprintf(stderr,"Usage: ./recover file\n");
       return 1;
    }

FILE *infile = fopen( infiles, "r");

   if (!infile)
    {
      fclose(infile);
      fprintf(stderr, "Could not open %s.\n", infiles);
      return 2;
    }


FILE *jpg= NULL;

 while (fread(buffer, 512, 1, infile) == 1)
  {

    if (buffer[0]== 0xff &&
         buffer[1]==0xd8 &&
         buffer[2]==0xff &&
        (buffer[3] & 0xf0)==0xe0)
     {
      if (fcount==0)
      {
       sprintf(filename, "%03i.jpg", fcount);
       jpg=fopen(filename, "w");
       fwrite(buffer, 512, 1, jpg);
       fcount++;
      }
      else
       {
        fclose(jpg);
        sprintf(filename, "%03i.jpg", fcount);
        jpg=fopen(filename, "w");
        fwrite(buffer, 512, 1, jpg);
        fcount++;
       }
     }

     else if (fcount >= 1)
      {
       fwrite(buffer, 512, 1, jpg);
      }

}

fclose(jpg);
 fclose(infile);
}