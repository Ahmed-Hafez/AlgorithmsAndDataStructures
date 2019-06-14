package AlgorithmsDesign;

import Algorithms.MathAlgorithms;
import Algorithms.SearchingAlgorithms;
import Algorithms.SortingAlgorithms;

public class Main {

    public static void main(String[] args) {


        System.out.println(MathAlgorithms.KaratsubaMultiplication(12345, 6789));

        System.out.println(SearchingAlgorithms.binarySearch(new int[]{1,2,3,4,5,6}, 3));


        Integer[] arr = {1,4,2,3,6,7,76,324,12,12,43,456,987};
        Integer[] arr2 = {7, 4, 2, 6, 1, 8, 3};

        SortingAlgorithms.MergeSort(arr, 0, arr.length-1);
        SortingAlgorithms.MergeSort(arr2, 0, arr2.length-1);

        for (int item : arr) {
            System.out.print(item + " ");
        }

        System.out.println();
        for (int item : arr2) {
            System.out.print(item + " ");
        }

    }
}
