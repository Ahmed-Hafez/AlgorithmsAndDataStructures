package Algorithms;

import DataStructures.Queue;

import java.util.List;

public class SortingAlgorithms{

    // Implementation of selection sort algorithm
    public static <T extends Comparable> void SelectionSort (T[] container){

        for (int i = 0; i < container.length; i++)
        {
            for (int j = i; j < container.length; j++)
            {
                if (container[i].compareTo(container[j]) > 0)
                {
                    T temp = container[i];
                    container[i] = container[j];
                    container[j] = temp;
                }
            }
        }
    }


    // Implementation of merge sort algorithm
    public static <T extends Comparable> void MergeSort(T[] container, int low, int high)
    {
        if (low < high)
        {
            int mid = (low + high) / 2;
            MergeSort(container, low, mid);
            MergeSort(container, mid + 1, high);
            Merge(container, low, high);
        }
    }


    private static <T extends Comparable> void Merge(T[] container, int low, int high)
    {
        // The middle of the part which we sort in the container
        int mid = (low + high) / 2;

        // Containers used in merge sort
        // Note : This Queue data structure is implemented by me.
        Queue<T> q1 = new Queue<>();
        Queue<T> q2 = new Queue<>();

        int i = low; //Counter

        // Inserting the first half part in the specified
        // part in the container in a queue
        for (; i <= mid; i++)
            q1.push(container[i]);

        // Inserting the first half part in the specified
        // part in the container in a queue
        for (; i <= high; i++)
            q2.push(container[i]);

        i = low;

        // Compare the items in the two queues
        while (!q1.isEmpty() && !q2.isEmpty())
        {
            if (q1.peek().compareTo(q2.peek()) < 0)
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


    // Implementation of insertion sort algorithm
    public static <T extends Comparable> void InsertionSort(T[] container)
    {
        int insertionPosition, out; // out = first unsorted element
        for(out = 1; out < container.length; out++){
            T temp = container[out];
            insertionPosition = out;
            while(insertionPosition > 0 && container[insertionPosition-1].compareTo(temp) > 0){
                container[insertionPosition] = container[insertionPosition-1];
                insertionPosition--;
            }
            container[insertionPosition] = temp;
        }
    }


    // Implementation of sell sort algorithm
    public static <T extends Comparable> void ShellSort(T[] container){
        int gap = container.length / 2;
        while(gap != 0){
            for(int i = 0; i < gap; i++){
                // Doing insertion sort
                int insertionPosition, out;
                for(out = gap + i; out < container.length; out+=gap){
                    T temp = container[out];
                    insertionPosition = out;
                    while(insertionPosition > i && container[insertionPosition - gap].compareTo(temp) > 0){
                        container[insertionPosition] = container[insertionPosition - gap];
                        insertionPosition -= gap;
                    }
                    container[insertionPosition] = temp;
                }
            }
            gap = gap / 2;
        }
    }
}
