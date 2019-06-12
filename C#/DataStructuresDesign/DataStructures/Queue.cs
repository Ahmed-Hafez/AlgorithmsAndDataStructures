using System.Collections.Generic;

namespace DataStructures
{
    /// <summary>
    /// Queue data structure
    /// </summary>
    /// <typeparam name="T">The type of the stored items</typeparam>
    public class Queue<T>
    {
        #region Private Members

        /// <summary>
        /// The size of the queue
        /// </summary>
        private int size;

        /// <summary>
        /// The index of the peek value
        ///
        /// Note : I didn't consider that this is the queue size
        ///        because in future we may use it in another feature
        ///        for the queue of large data to make some priority for some data
        /// </summary>
        private int front;

        /// <summary>
        /// The container of the items of the queue
        /// </summary>
        private List<T> queueContainer;

        #endregion

        #region Constructor

        /// <summary>
        /// Initializes a new instance from the queue class
        /// </summary>
        public Queue()
        {
            size = 0;
            front = 0;
            queueContainer = new List<T>();
        }

        #endregion

        #region Queue Methods

        /// <summary>
        /// Returns the queue size
        /// </summary>
        public int getSize() => size;

        /// <summary>
        /// Pushes an item in the queue
        /// </summary>
        /// <param name="item">The item to push in the queue</param>
        public void push(T item)
        {
            queueContainer.Add(item);
            size++;
        }

        /// <summary>
        /// Removes an item from the queue
        /// </summary>
        public void pop()
        {
            // Check if the queue has items to pop from
            if (isEmpty())
                return;

            queueContainer.Remove(queueContainer[front]);
            size--;
        }

        /// <summary>
        /// Get the peek(front) value in the queue
        /// </summary>
        public T peek() => queueContainer[front];

        /// <summary>
        /// Checks if the queue is empty or not
        /// </summary>
        public bool isEmpty() => (size == 0);

        #endregion
    }
}
