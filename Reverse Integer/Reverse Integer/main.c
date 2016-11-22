// Reverse an Integer. LeetCode OJ Problem #7

#include <stdio.h>


int reverseInteger(int number)
{
    int result = 0;
    int flag = 0;
    if (number < 0)
    {
        number = 0 - number;
        flag = 1;
        printf("Making Number Positive: %d\n", number);
    }
    int p = number;
    while(p > 0)
    {
        /*CALCULATE VALUE TO APPEND AT EACH LEVEL*/
        int mod = p % 10;
        /*REDUCE P*/
        p = p/10;
        /*APPEND VALUE TO RESULT, SHIFT USING MULTIPLICATION BY 10*/
        result = result * 10 + mod;
    }
        if(flag == 1)
        {
            result = 0 - result;
        }
    return result;
}

int main(int argc, const char * argv[])
{
    printf("Reverse: %d\n", reverseInteger(-123));
    return 0;
}
