using System;
using System.Collections.Generic;
using DS = DataStructures;
using System.Linq;

namespace Algorithms
{
    public static class SortingAlgorithms
    {
        #region Public methods

        /// <summary>
        /// Implementation of selection sort algorithm
        /// </summary>
        /// <typeparam name="T">The type of the objects in the <see cref="IList{T}"/></typeparam>
        /// <param name="container">The container to search in</param>
        public static void SelectionSort<T>(IList<T> container)
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
                        Swap<T>(ref x, ref y);
                        container[i] = x;
                        container[j] = y;
                    }
                }
            }
        }

        /// <summary>
        /// Implementation of selection sort algorithm
        /// </summary>
        /// <typeparam name="T">The type of the objects in the <see cref="IList{T}"/></typeparam>
        /// <param name="container">The container to search in</param>
        /// <param name="low">The starting index</param>
        /// <param name="high">The ending index</param>
        public static void MergeSort<T>(IList<T> container, int low, int high)
            where T : IComparable
        {
            if (low < high)
            {
                int mid = (low + high) / 2;
                MergeSort(container, low, mid);
                MergeSort(container, mid + 1, high);
                Merge(container, low, high);
            }
        }

        #endregion

        #region Private methods

        /// <summary>
        /// Swap the values of the provided objects
        /// </summary>
        /// <typeparam name="T">The type of the objects</typeparam>
        /// <param name="x">The first object</param>
        /// <param name="y">The second object</param>
        private static void Swap<T>(ref T x, ref T y)
        {
            T temp = x;
            x = y;
            y = temp;
        }

        /// <summary>
        /// Merging function which used in merge sort
        /// </summary>
        /// 
        /// <typeparam name="T">
        /// The type of the objects in the specified
        /// <see cref="IList{T}"/> container
        /// </typeparam>
        /// 
        /// <param name="container">The container to sort its elements</param>
        /// <param name="low">The starting index</param>
        /// <param name="high">The ending index</param>
        private static void Merge<T>(IList<T> container, int low, int high)
            where T : IComparable
        {
            // The middle of the part which we sort in the container
            int mid = (low + high) / 2;

            // Containers used in merge sort
            // Note : This Queue data structure is implemented by me,
            //        you can see it in the C#/DataStructuresDesign folder on the repo.
            DS.Queue<T> q1 = new DS.Queue<T>();
            DS.Queue<T> q2 = new DS.Queue<T>();

            
            int i = low; //Counter

            // Inserting the first half part in the specified
            // part in the container in a queue
            for (; i < mid; i++)
                q1.push(container[i]);

            // Inserting the first half part in the specified
            // part in the container in a queue
            for (; i < high; i++)
                q2.push(container[i]);

            i = low;

            // Compare the items in the two queues
            while (!q1.isEmpty() && !q2.isEmpty())
            {
                if (q1.peek().CompareTo(q2.peek()) < 0)
                {
                    container[i++] = q1.peek();
                    q1.pop();
                }
                else
                {
                    container[i++] = q2.peek();
                    q2.pop();
                }
            }

            // Check if the first queue still has items
            while (!q1.isEmpty())
            {
                container[i++] = q1.peek();
                q1.pop();
            }

            // Check if the second queue still has items
            while (!q2.isEmpty())
            {
                container[i++] = q2.peek();
                q2.pop();
            }
        }
        #endregion

    }
}
