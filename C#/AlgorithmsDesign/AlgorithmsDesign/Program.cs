using System;
using System.Collections.Generic;
using Algorithms;

namespace AlgorithmsDesign
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] arr = { 1, 2, 3, 4, 5, 8, 11, 20 };
            Console.WriteLine(SearchingAlgorithms.BinarySearch<int>(arr, 20));

            List<string> list = new List<string>() { "Ahmed", "ahmed", "sara" };
            Console.WriteLine(SearchingAlgorithms.BinarySearch<string>(list, "ahmed"));
        }
    }
}
