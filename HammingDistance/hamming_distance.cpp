/*
 * The Hamming distance between two integers
 * is the number of positions at which the
 * corresponding bits are different.
 *
 *      1 (0 0 0 1)
 * XOR =   0 1 0 1
 *      4 (0 1 0 0)
 *           ^   ^
 * do an xor and count the 1's
 ≥.*/

 class Solution {
 public:
     int hammingDistance(int x, int y) {
         int k = x^y;
         int count = 0;
         while (k) {
             count = count + (k & 1);
             k = k >> 1;
         }
         return count;
     }
 };
