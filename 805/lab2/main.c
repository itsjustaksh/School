#include <stdio.h>
#include <stdint.h>
#include <unistd.h>

int main()
{
   // Step 1: Vars and givens
   register uint8_t temperature;
   uint8_t frzTemp = 0x7F; // Greater than this means freezing, else not

   // Step 2: Init Reg with Positive Val
   temperature = 0x8F;

   // Step 3: Polling
   while(1)
   {
      if (temperature > frzTemp)
      {
         printf("Freezing, ");
      }
      printf("Current temp: %u\n", temperature);
      sleep(1);
   }
   return 0;
}
