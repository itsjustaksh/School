#include <stdio.h>
#include <stdint.h>
#include <string.h>

void squeeze(char s[], char c[])
{
   int i, j, k;
   for (k = 0; c[k] != '\0'; k++)
   {
      for (i = j = 0; s[i] != '\0'; i++)
      {
         // printf("Curr check - S1: %c S2: %c\n", s[i], c[k]);
         if (s[i] != c[k])
         {
            s[j++] = s[i];
         }

      }
      s[j] = '\0';
   }
}

int main()
{
   // char * string1 = "This is a string";
   char string1[] = "This_is_another_string";
   char charsToCut[] = "asin";

   printf("Original String: %s, removing chars: %s\n", string1, charsToCut);
   squeeze(string1, charsToCut);
   printf("Result: %s\n", string1);

   // unsigned char var1 = 0x82;
   // var1 = 0x82 >> 2;
   // printf("Result op: %x\n\n", var1);

   return 0;
}
