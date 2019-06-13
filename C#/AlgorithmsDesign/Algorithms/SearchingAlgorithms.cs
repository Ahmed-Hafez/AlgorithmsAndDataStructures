using System;
using System.Collections.Generic;
using System.Linq;

namespace Algorithms
{
    public static class SearchingAlgorithms
    {
        /// <summary>
        /// Searching for the <paramref name="value"/> provided in the provided <see cref="IList{T}"/> object
        /// </summary>
        /// <typeparam name="T">The type of the objects in the <see cref="IList{T}"/></typeparam>
        /// <param name="container">The container to search in</param>
        /// <param name="value">The value to search for</param>
        public static bool BinarySearch<T>(IList<T> container, T value) 
            where T : IComparable
        {
            T[] mContainer = new T[container.Count];
            container.CopyTo(mContainer, 0);

            SortingAlgorithms.SelectionSort<T>(mContainer);

            int lowPtr = 0;
            int highPtr = mContainer.Length;

            while (lowPtr < highPtr)
            {
                int midPtr = (lowPtr + highPtr) / 2;
                int comparingValue = mContainer.ElementAt<T>(midPtr).CompareTo(value);

                if (comparingValue > 0)
                    highPtr = midPtr - 1;
                else if (comparingValue < 0)
                    lowPtr = midPtr + 1;
                else return true;
            }

            // Check the state when (lowPtr == highPtr)
            if (lowPtr == highPtr
                && lowPtr < mContainer.Length
                && mContainer.ElementAt<T>(lowPtr).CompareTo(value) == 0)
                return true;

            return false;
        }
    }
}
