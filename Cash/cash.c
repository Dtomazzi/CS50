#include <stdio.h>
#include <cs50.h>

int main(void)
{

 float Q = (25);
 float D = (10);
 float N = (5);
 float P= (1);
 int quarters = 0;
 int dimes = 0;
 int nickels = 0;
 int pennies =0;
 int change=0;

//Prompt user for change owed
float cash=get_float ("change owed: ");
cash=cash * 100;

//Counts number of quarters for change
for (quarters= 0; cash >= Q; quarters++)
  {
   cash= cash - Q;
  }
  //Counts number of dimes for change
  for (dimes = 0; cash >= D; dimes++)
  {
    cash = cash - D;
  }
  //Counts number of nickels for change
  for (nickels =0; cash >= N; nickels++)
  {
    cash = cash - N;
  }
  //Counts number of pennies for change
  for (pennies =0; cash >=1; pennies++)
  {
    cash = cash - P;
  }
  //Add total of coins to get change number
   change= quarters + dimes + nickels + pennies;
   printf("%i\n", change);

}