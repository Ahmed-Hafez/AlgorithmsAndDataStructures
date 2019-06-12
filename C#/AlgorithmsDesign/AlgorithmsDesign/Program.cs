using System;
using System.Collections.Generic;
using Algorithms;

namespace AlgorithmsDesign
{
    class Program
    {
        static void Main(string[] args)
        {
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
