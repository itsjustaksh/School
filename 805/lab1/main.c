#include <stdio.h>

int main()

{
   int i = 0, j = 0;
   j = i++ ? i++ : ++i;
   j = i++ ? i++, ++j : ++j, i++;

   printf("j=%d, i=%d\n", j, i);
}