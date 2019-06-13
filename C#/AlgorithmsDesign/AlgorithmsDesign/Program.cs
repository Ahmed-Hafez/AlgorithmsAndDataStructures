using System;
using System.Collections.Generic;
using Algorithms;

namespace AlgorithmsDesign
{
    class Program
    {
        /*public static long multiply(long x, long y)
        {
            long result = 0;

            int size1 = GetSize(x);
            int size2 = GetSize(y);

            //find the max size of two integers
            int N = Math.Max(size1, size2);

            if (N < 2)
                return x * y;

            //Max length divided by two and rounded up
            N = (N / 2) + (N % 2);

            //The mulitplying factor for calculating a,b,c,d
            long m = (long)Math.Pow(10, N);

            long b = x % m;
            long a = x / m;
            long c = y / m;
            long d = y % m;

            long z0 = multiply(a, c);
            long z1 = multiply(b, d);
            long z2 = multiply(a + b, c + d);

            result = ((long)Math.Pow(10, N * 2) * z0) + z1 + ((z2 - z1 - z0) * m);
            return result;
        }*/
        static void Main(string[] args)
        {
            Console.WriteLine("G = {0},\nK = {1},\nP = {2},\nX = ",
                MathAlgorithms.GradeSchoolMultiplication(999999999, 999999999),
                MathAlgorithms.KaratsubaMultiplication(999999999, 999999999),
                999999999L * 999999999L);

            //Console.WriteLine(Math.Pow(10, 2).ToString());

            int[] arr = { 1, 2, 3, 4, 5, 8, 11, 20, 4,465,4645,645,675,765,7,567,65 };
            Console.WriteLine(SearchingAlgorithms.BinarySearch<int>(arr, 20));

            List<string> list = new List<string>() { "Ahmed", "ahmed", "sara", "amgad" };
            Console.WriteLine(SearchingAlgorithms.BinarySearch<string>(list, "ahmed"));

            SortingAlgorithms.selectionSort<int>(arr);
            foreach (var item in arr)
            {
                Console.Write(item + " ");
            }
            Console.WriteLine();
            SortingAlgorithms.selectionSort<string>(list);
            foreach (var item in list)
            {
                Console.Write(item + " ");
            }
        }
    }
}
