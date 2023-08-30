#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string j = get_string("name: ");
    printf("hello, %s\n", j);
}