/*
 * Hamming weight is the number of bits set. just AND the
 * number with 1 and count # of 1s. Keep shifting n 1 bit right
 */
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while(n) {
            count = count + (n&1);
            n >>= 1;
        }
        return count;
    }
};
