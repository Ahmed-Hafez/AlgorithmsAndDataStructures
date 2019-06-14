package DataStructures;

import java.util.ArrayList;

public class Queue<T> {

    // Private Members

    // The size of the queue
    private int size;

    // The index of the peek value
    //
    // Note : I didn't consider that this is the queue size
    //        because in future we may use it in another feature
    //        for the queue of large data to make some priority for some data
    private int front;

    // The container of the items of the queue
    private ArrayList<T> queueContainer;

    //----------------------------------------------------------------------

    // Constructor

    // Initializes a new instance from the queue class
    public Queue(){
        size = 0;
        front = 0;
        queueContainer = new ArrayList<>();
    }

    //-----------------------------------------------------------------------

    // queue Methods

    // Returns the queue size
    public int getSize(){
        return size;
    }

    // Pushes an item in the queue
    public void push(T item){
        queueContainer.add(item);
        size++;
    }

    // Removes an item from the queue
    public void pop(){

        // Check if the queue has items to pop from
        if(isEmpty())
            return;

        queueContainer.remove(front);
        size--;
    }

    // Get the peek(front) value in the queue
    public T peek(){
        return queueContainer.get(front);
    }

    // Checks if the queue is empty or not
    public boolean isEmpty(){
        return (size == 0);
    }
    //-----------------------------------------------------------------------

}
