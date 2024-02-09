#include <stdio.h>

#define MAX 10 /* Size of the array */

void init_array(int arr[], int val)
{
   for(int i = 0; i < MAX; i++)
   {
      arr[i] = val;
   }
}

void copy_array(int src[], int dst[])
{
   for(int i = 0; i < MAX; i++)
   {
      dst[i] = src[i];
   }
}

int main()
{
   int array_1[MAX];
   int array_2[MAX];
   int init_value = 0xFE;

   /* Initializing the array */
   init_array(array_1, init_value);

   /* copy array_1 to array_2 */
   copy_array(array_1, array_2);

   // Print result
   for(int i = 0; i < MAX; i++)
   {
      printf("Array_2 at index %d: %X\n", i, array_2[i]);
   }

   return 0;
}