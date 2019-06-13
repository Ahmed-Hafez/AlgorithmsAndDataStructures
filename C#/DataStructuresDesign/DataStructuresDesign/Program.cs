using System;
using DataStructures;

namespace DataStructuresDesign
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("<-- Stack -->");
            Stack<int> stack = new Stack<int>();
            stack.push(1);
            stack.push(2);
            stack.push(3);
            stack.push(4);

            int size = stack.getSize();
            for (int i = 0; i < size; i++)
            {
                Console.WriteLine(stack.peek());
                stack.pop();
            }

            Console.WriteLine("<-- Queue -->");
            Queue<int> queue = new Queue<int>();
            queue.push(1);
            queue.push(2);
            queue.push(3);
            queue.push(4);

            size = queue.getSize();
            for (int i = 0; i < size; i++)
            {
                Console.WriteLine(queue.peek());
                queue.pop();
            }
        }
    }
}
