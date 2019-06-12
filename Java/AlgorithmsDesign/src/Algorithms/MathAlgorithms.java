package Algorithms;

public class MathAlgorithms {
    /// <summary>
    /// Implementation of grade school algorithm
    /// </summary>
    /// <param name="firstNum">First number</param>
    /// <param name="secondNum">Second number</param>
    public static long GradeSchoolMultiplication(long firstNum, long secondNum)
    {
        String S_SecondNum = Long.valueOf(secondNum).toString();

        long sum = 0;

        for (int i = S_SecondNum.length() - 1, j = 0; i >= 0; i--, j++)
        {
            sum += (firstNum * (S_SecondNum.charAt(i) - '0')) * Math.pow(10, j);
        }

        return sum;
    }

    /// <summary>
    /// Implementation of Karatsuba multiplication algorithm
    /// </summary>
    /// <param name="firstNum">First number</param>
    /// <param name="secondNum">Second number</param>
    public static long KaratsubaMultiplication(long firstNum, long secondNum)
    {
        // Find the min size of two integers
        int n = Math.min(Long.valueOf(firstNum).toString().length(),
                Long.valueOf(secondNum).toString().length());

        // Base case
        if (n == 1)
            return firstNum * secondNum;

        n = n / 2;

        //The power for calculating a,b,c,d
        long p = (long)Math.pow(10, n);

        long a = firstNum / p;
        long b = firstNum % p;
        long c = secondNum / p;
        long d = secondNum % p;

        // Performing Karatsuba equation => ac * 10^n + (10^((n+1)/2)) * (ad + bc) + bd
        long ac = KaratsubaMultiplication(a, c);
        long bd = KaratsubaMultiplication(b, d);
        long f = KaratsubaMultiplication(a + b, c + d);
        return ((long)Math.pow(10, 2 * n) * ac) + bd + ((f - bd - ac) * p);
    }
}
