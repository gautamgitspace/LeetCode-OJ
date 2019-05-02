"""
Merge two sorted arrays
arr1 = [3, 5, 6, 9, 14]
arr2 = [1, 7, 9]
result = [1, 3, 5, 6, 7, 9, 14]

KEY - end of nums1 is big enough to hold m+n. Start comparing
from end and keep adding to m+n-1 index of nums1
"""

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int indexA = m - 1;
        int indexB = n - 1;
        int indexR = m + n - 1;

        while (indexB >=0 ) {
            if (indexA >= 0 && nums1[indexA] > nums2[indexB]) {
                nums1[indexR] = nums1[indexA];
                indexA --;
            } else {
                nums1[indexR] = nums2[indexB];
                indexB --;
            }
            indexR --;
        }
    }
}
