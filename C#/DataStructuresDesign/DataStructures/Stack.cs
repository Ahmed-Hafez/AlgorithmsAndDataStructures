using System.Collections.Generic;

namespace DataStructures
{
    /// <summary>
    /// Stack data structure
    /// </summary>
    /// <typeparam name="T">The type of the stored items</typeparam>
    public class Stack<T>
    {
        #region Private Members

        /// <summary>
        /// The size of the stack
        /// </summary>
        private int size;

        /// <summary>
        /// The index of the peek value
        ///
        /// Note : I didn't consider that this is the stack size
        ///        because in future we may use it in another feature
        ///        for the stack of large data to make some priority for some data
        /// </summary>
        private int top;

        /// <summary>
        /// The container of the items of the stack
        /// </summary>
        private List<T> stackContainer;

        #endregion

        #region Constructor

        /// <summary>
        /// Initializes a new instance from the Stack class
        /// </summary>
        public Stack()
        {
            size = 0;
            top = -1;
            stackContainer = new List<T>();
        }

        #endregion

        #region Stack Methods

        /// <summary>
        /// Returns the stack size
        /// </summary>
        public int getSize() => size;
        
        /// <summary>
        /// Pushes an item in the stack
        /// </summary>
        /// <param name="item">The item to push in the stack</param>
        public void push(T item)
        {
            stackContainer.Add(item);
            top++;
            size++;
        }

        /// <summary>
        /// Removes an item from the stack
        /// </summary>
        public void pop()
        {
            // Check if the stack has items to pop from
            if (isEmpty())
                return;

            stackContainer.Remove(stackContainer[top]);
            top--;
            size--;
        }

        /// <summary>
        /// Get the peek(top) value in the stack
        /// </summary>
        public T peek() => stackContainer[top];
        
        /// <summary>
        /// Checks if the stack is empty or not
        /// </summary>
        public bool isEmpty() => (size == 0);

        #endregion
    }
}
