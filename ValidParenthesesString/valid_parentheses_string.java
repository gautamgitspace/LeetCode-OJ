/*
RULES:
	- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
	- Any right parenthesis ')' must have a corresponding left parenthesis '('.
	- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
	- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
	- An empty string is also valid.
*/

class Solution {
     public boolean checkValidString(String s) {
        /* keep separate stacks for opening bracket
         * and star. When closing is encountered, pop
         * from leftID first if not empty. if leftID
         * is empty, pop from starID if not empty. if
         * both of them are empty, we have a false*/

        Stack<Integer> leftID = new Stack<>();
        Stack<Integer> starID = new Stack<>();

         for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '(')
                leftID.push(i);
            else if (ch == '*')
                starID.push(i);
            else {
                if (leftID.isEmpty() && starID.isEmpty())   return false;
                if (!leftID.isEmpty())
                    leftID.pop();
                else
                    starID.pop();
            }
        }
        /* this is for cases where we don't encounter a closing
         * at all. such as "((*(*(**". Here the key is that index
         * stored in leftID must always be less than index stored in
         * starID. This is because opening cannot appear after last
         * star (there is no way to balance that)*/
        while (!leftID.isEmpty() && !starID.isEmpty()) {
            if (leftID.pop() > starID.pop())
                return false;
        }
        /* correct balanced sequence will result in an empty leftID */
        return leftID.isEmpty();
    }
}
