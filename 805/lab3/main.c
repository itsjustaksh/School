#include <stdio.h>
#include <stdint.h>
#include <string.h>

int main()
{
   // Problem 1:
   char str;
   char largest;
   const char exitStr = 'X';

   printf("Enter some text, enter 'X' to exit: \n");
   while (str != exitStr)
   {
      scanf("%c", &str);
      if (str > largest){
         largest = str;
         printf("Largest: %c\n", largest);
      }
   }
   printf("Longest entered string: %c\n", largest);


   // Problem 2
   // Q1
   printf("\n\n");
   printf("Hello World" + 4);

   // Q2
   printf("\nQ3: \n\n");
   int i = 43;
   printf("%d",printf("%d",printf("%d",i)));
   printf("\n");

   return 0;
}