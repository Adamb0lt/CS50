#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int n;

    do
    {
        n = get_int("start size: ");
    }
    while (n < 9);

    // TODO: Prompt for end size
    int j;

    do
    {
        j = get_int("end size: ");
    }
    while (j < n);
    // TODO: Calculate number of years until we reach threshold
    // alternate method to calculate the years using a for loop
    /*int s;
    for (s = 0; s < j; s++)
    {
        n = n+(n/3)-(n/4);
        if(n >= j)
        {
          break;
        }

    }
    printf("Years: %i\n", s);
    */
    int s = 0;

    do
    {
        s++;
        n = n + (n / 3) - (n / 4);
    }
    while (n < j);

    // TODO: Print number of years
    printf("Years: %i\n", s);
}
