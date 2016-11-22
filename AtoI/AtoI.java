//LeetCodeOJ Problem #8 String to Integer with corner cases
package AtoI;

public class AtoI
{
    public static int stringToInteger(String input)
    {
        if(input == null || input.length() == 0)
        return 0;
        input = input.trim();
        char flag = '+';
        int i = 0;
        double result = 0;
        if(input.charAt(0) == '-')
        {
            flag = '-';
            i++;
        }
        else if(input.charAt(0) == '+')
        {
            flag = '+';
            i++;
        }
        while(input.length() > i && input.charAt(i) >= '0' && input.charAt(i) <= '9')
        {
            result = result * 10 + (input.charAt(i) - '0');
            i++;
        }
        if(flag == '-')
        {
            result = -result;
        }
        if(result > Integer.MAX_VALUE) {
            System.out.println("MAX VALUE REACHED ALERT!");
            return Integer.MAX_VALUE;
        }
        if(result < Integer.MIN_VALUE) {
            System.out.println("MIN VALUE REACHED ALERT!");
            return Integer.MIN_VALUE;
        }
        return (int) result;
    }


    public static void main(String args[])
    {
        String test = "+123";
        System.out.println(stringToInteger(test));
    }
}