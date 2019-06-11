package Algorithms;

public class SearchingAlgorithms {

    // Implementation of binary search algorithm
    public static boolean binarySearch(int[] list, int value){

        int low = 0;
        int high = list.length;

        while (low < high){

            int mid = (low + high) / 2;
            if(list[mid] > value)
                high = mid - 1;
            else if(list[mid] < value)
                low = mid + 1;
            else return true;

        }

        // Checking the state when low == high
        if(low == high
                && low < list.length
                && list[low] == value)
            return true;

        return false;
    }
}
