class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }

        Set<Character> set = new HashSet<>();
        int left = 0;
        int right = 0;
        int max = 0;

        /* keep processing until right ptr reaches the end */
        while (right < s.length()) {
            if (set.add(s.charAt(right))) {
                /* Add to set iff not already there
                 * Keep expanding by doing right++
                 * Keep updating max string length
                 * which will always be position(s)
                 * between right and left ptr
                 */
                right++;
                max = Math.max(max, right-left);
            } else {
                /* set.add will return false and would not
                 * add it in if it exists
                 * Iterate left and then remove from set
                 * Key-> both ptrs move forward
                 */
                set.remove(s.charAt(left++));
            }
        }
        return max;
    }
}
