#include <cs50.h>
#include <ctype.h>
#include <stdio.h>



float calc_hours(int hours[], int weeks, char output);

int main(void)
{
    int weeks = get_int("Number of weeks taking CS50: ");
    int hours[weeks];

    for (int i = 0; i < weeks; i++)
    {
        hours[i] = get_int("Week %i HW Hours: ", i);
    }

    char output;
    do
    {
        output = toupper(get_char("Enter T for total hours, A for average hours per week: "));
    }
    while (output != 'T' && output != 'A');

    printf("%.1f hours\n", calc_hours(hours, weeks, output));
}

// TODO: complete the calc_hours function
float calc_hours(int hours[], int weeks, char output)
{
    float total = 0; // total sum of hours
    float avg; // average of all hours within array

    //for loop to create the total and averages
    for(int p = 0; p < weeks; p++)
    {
        total += hours[p];
        if (p == weeks - 1 && output == 'A')
        {
            total = (float) total/ (float) weeks;
        }

    }
    return total;
}