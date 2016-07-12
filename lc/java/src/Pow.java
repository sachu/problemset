/*
https://leetcode.com/problems/powx-n/

Implement pow(x, n).

#1
8.88023
3

#2
2.00000
-2147483648

#3
-1.00000
-2147483648
*/

public class Pow {
    public double myPow(double x, int n) {
        if (n == 0) {
            return 1;
        }

        if (n < 0) {
            // n = -n; When n=Integer.MIN_VALUE, then n=-n will overflow.
            //         e.g. 2.0 raised to -2147483648 will return infinity
            if (n == Integer.MIN_VALUE) {
                n += 1;
                x = 1 / (x * x); // because we already processed 1 step in the line above
            } else {
                x = 1 / x;
            }
            n = -n;
        }

        if (n % 2 == 0) {
            return myPow(x * x, n / 2);
        }
        return x * myPow(x * x, n / 2);
    }
}