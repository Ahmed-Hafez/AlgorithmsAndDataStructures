package DataStructures;

import java.util.ArrayList;

// Implements the stack data structure functionality
public class Stack<T> {

    // Private Members

    // The size of the stack
    private int size;

    // The index of the peek value
    //
    // Note : I didn't consider that this is the stack size
    //        because in future we may use it in another feature
    //        for the stack of large data to make some priority for some data
    private int top;

    // The container of the items of the stack
    private ArrayList<T> stackContainer;

    //----------------------------------------------------------------------

    // Constructor

    // Initializes a new instance from the Stack class
    public Stack(){
        size = 0;
        top = -1;
        stackContainer = new ArrayList<>();
    }

    //-----------------------------------------------------------------------

    // Stack Methods

    // Returns the stack size
    public int getSize(){
        return size;
    }

    // Pushes an item in the stack
    public void push(T item){
        stackContainer.add(item);
        top++;
        size++;
    }

    // Removes an item from the stack
    public void pop(){

        // Check if the stack has items to pop from
        if(isEmpty())
            return;

        stackContainer.remove(top);
        top--;
        size--;
    }

    // Get the peek(top) value in the stack
    public T peek(){
        return stackContainer.get(top);
    }

    // Checks if the stack is empty or not
    public boolean isEmpty(){
        return (size == 0);
    }
    //-----------------------------------------------------------------------
}
