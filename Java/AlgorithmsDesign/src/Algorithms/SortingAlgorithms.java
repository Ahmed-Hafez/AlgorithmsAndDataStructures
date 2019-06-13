package Algorithms;

public class SortingAlgorithms {

    // Implementation of selection sort algorithm
    public static void selectionSort(int[] list){

        for (int i = 0; i < list.length; i++){
            for(int j = i; j < list.length; j++){
                if(list[i] > list[j]){
                    int temp = list[i];
                    list[i] = list[j];
                    list[j] = temp;
                }
            }
        }
    }

}
