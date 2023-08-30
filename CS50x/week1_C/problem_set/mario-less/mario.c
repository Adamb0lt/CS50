#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Ask for height with do while loop
    int h;

    do
    {
        h = get_int("Height: ");

    } while(h < 1 || h > 8);

    //Main for loop for running the smaller for loops that print the spaces and hashtags
    for ( int i = 0; i < h; i++)
    {
        //for creating spaces of the right aligning pyramid
        for( int j = h - i - 1; j > 0; j--)
        {
            printf(" ");
        }



        //for creating the hashtags of right aligning pyramid
        for( int p = 0; p < i + 1; p++)
        {
            printf("#");
        }

        //for creating the hashtags of left aligning pyramid
        for( int l = 0; l < i+1; l++)
        {
            printf("#");
        }

        printf("\n");

    }
}