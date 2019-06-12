using System;

namespace Algorithms
{
    public class MathAlgorithms
    {
        /// <summary>
        /// Implementaion of grade school algorithm
        /// </summary>
        /// <param name="firstNum">First number</param>
        /// <param name="secondNum">Second number</param>
        public static long GradeSchoolMultiplication(long firstNum, long secondNum)
        {
            string S_SecondNum = secondNum.ToString();

            long sum = 0;

            for (int i = S_SecondNum.Length - 1, j = 0; i >= 0; i--, j++)
            {
                sum += (firstNum * (S_SecondNum[i] - '0')) * Convert.ToInt64(Math.Pow(10, j));
            }

            return sum;
        }

        /// <summary>
        /// Implementaion of Karatsuba multiplication algorithm
        /// </summary>
        /// <param name="firstNum">First number</param>
        /// <param name="secondNum">Second number</param>
        public static long KaratsubaMultiplication(long firstNum, long secondNum)
        {
            // Find the min size of two integers
            int n = Math.Min(firstNum.ToString().Length, secondNum.ToString().Length);

            if (n == 1)
                return firstNum * secondNum;

            n = n / 2;

            //The power for calculating a,b,c,d
            long p = (long)Math.Pow(10, n);

            long a = firstNum / p;
            long b = firstNum % p;
            long c = secondNum / p;
            long d = secondNum % p;

            // Performing Karatsuba equation => ac * 10^n + (10^((n+1)/2)) * (ad + bc) + bd
            long ac = KaratsubaMultiplication(a, c);
            long bd = KaratsubaMultiplication(b, d);
            long f = KaratsubaMultiplication(a + b, c + d);
            return ((long)Math.Pow(10, 2 * n) * ac) + bd + ((f - bd - ac) * p);
        }
    }
}
