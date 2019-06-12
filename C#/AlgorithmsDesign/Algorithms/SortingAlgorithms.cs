using System;
using System.Collections.Generic;
using System.Linq;

namespace Algorithms
{
    public static class SortingAlgorithms
    {
        /// <summary>
        /// Swap the values of the provided objects
        /// </summary>
        /// <typeparam name="T">The type of the objects</typeparam>
        /// <param name="x">The first object</param>
        /// <param name="y">The second object</param>
        private static void Swap<T>(ref T x,ref T y)
        {
            T temp = x;
            x = y;
            y = temp;
        }

        /// <summary>
        /// Sorting the provided <see cref="IList{T}"/> object
        /// </summary>
        /// <typeparam name="T">The type of the objects in the <see cref="IList{T}"/></typeparam>
        /// <param name="container">The container to search in</param>
        public static void selectionSort<T>(IList<T> container)
            where T : IComparable
        {
            for (int i = 0; i < container.Count; i++)
            {
                for (int j = i; j < container.Count; j++)
                {
                    if (container.ElementAt<T>(i).CompareTo(container.ElementAt<T>(j)) > 0)
                    {
                        T x = container[i];
                        T y = container[j];
                        Swap<T>(ref x,ref y);
                        container[i] = x;
                        container[j] = y;
                    }
                }
            }
        }

    }
}
