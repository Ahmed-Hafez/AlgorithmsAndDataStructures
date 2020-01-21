package Algorithms;


import java.util.*;

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
        Queue<T> q1 = new LinkedList<>();
        Queue<T> q2 = new LinkedList<>();

        int i = low; //Counter

        // Inserting the first half part in the specified
        // part in the container in a queue
        for (; i <= mid; i++)
            q1.add(container[i]);

        // Inserting the first half part in the specified
        // part in the container in a queue
        for (; i <= high; i++)
            q2.add(container[i]);

        i = low;

        // Compare the items in the two queues
        while (!q1.isEmpty() && !q2.isEmpty())
        {
            if (q1.peek().compareTo(q2.peek()) < 0)
            {
                container[i++] = q1.peek();
                q1.remove();
            }
            else
            {
                container[i++] = q2.peek();
                q2.remove();
            }
        }

        // Check if the first queue still has items
        while (!q1.isEmpty())
        {
            container[i++] = q1.peek();
            q1.remove();
        }

        // Check if the second queue still has items
        while (!q2.isEmpty())
        {
            container[i++] = q2.peek();
            q2.remove();
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
    // Using shell original sort
    public static <T extends Comparable> void ShellSort1(T[] container){
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

    // Implementation of sell sort algorithm
    // Using Knuth Sequence
    public static <T extends Comparable> void ShellSort2(T[] container){
        int gap = 1;
        while (gap < container.length) gap = gap*3+1;
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
            gap = (gap-1) / 3;
        }
    }

    // Implementation of radix Sort algorithm
    public static void RadixSort(Integer[] container){
        Queue[] buckets = new LinkedList[10];
        for (int i = 0; i < 10; i++)
            buckets[i] = new LinkedList();

        // Get number of passes
        int max = Integer.MIN_VALUE, pass = 0;
        for (int item: container)
            if (item > max) max = item;
        while(max != 0){
            pass++;
            max /= 10;
        }

        for (int i = 0; i < pass; i++) {
            for (int item : container) {
                int digit = item / (int) Math.pow(10, i);
                digit %= 10;
                buckets[digit].add(item);
            }
            int x = 0;
            for (int k = 0; k < 10; k++) {
                while (!buckets[k].isEmpty()) {
                    container[x] = (int)buckets[k].remove();
                    x++;
                }
            }
        }


    }
}
