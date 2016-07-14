/*
 https://leetcode.com/problems/permutation-sequence/

 The set [1,2,3,…,n] contains a total of n! unique permutations.

 By listing and labeling all of the permutations in order,
 We get the following sequence (ie, for n = 3):

 "123"
 "132"
 "213"
 "231"
 "312"
 "321"
 Given n and k, return the kth permutation sequence.

 Note: Given n will be between 1 and 9 inclusive.
 */


public class PermutationSequence {
    public static int factorial(int n) {
        int fact = 1;
        for (int i = 1; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }

    private int minNum(boolean[] nums) { // false value means num has not been used yet
        for (int i = 1; i <= nums.length; i++) {
            if (!nums[i-1]) {
                return i;
            }
        }
        return -1; // should never reach here
    }

    private int nextNum(boolean[] nums, int prev) {
        // find the next unused number
        // this would be easier if the sequence was counted from 0
        int i = prev % nums.length;
        while (nums[i]) {
            i = (i + 1) % nums.length;
        }
        return i+1;
    }

    public String getPermutation(int n, int k) {
        int totalPermutations = factorial(n);

        // to handle cycling. e.g. n=3, k=10000
        // this is annoying because of off-by-one errors
        k = ((k - 1) % totalPermutations) + 1;

        String res = "";
        boolean[] nums = new boolean[n]; // digits. false means num not used yet

        for (int i = n; i >= 1; i--) {
            int digit = minNum(nums);
            int perms = factorial(i-1);
            while (k > perms) {
                k -= perms;
                digit = nextNum(nums, digit);
            }
            res += digit;
            nums[digit-1] = true;
        }
        return res;
    }
}
