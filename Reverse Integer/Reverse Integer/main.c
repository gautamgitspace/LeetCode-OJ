#include <stdio.h>
#DEFINE INT_MAX 2147483647
#DEFINE INT_MIN -2147483648


long reverse(long number)
{
    long result = 0;
    int flag = 0;
    if (number < 0)
    {
        number = 0 - number;
        flag = 1;
    }
    int p = number;
    while(p > 0)
    {
        result = result * 10 + p % 10;
        p = p / 10;
    }
        if(flag == 1)
        {
            result = 0 - result;
        }
    if (result > INT_MAX || result < INT_MIN)
        return 0;
    return result;
}
