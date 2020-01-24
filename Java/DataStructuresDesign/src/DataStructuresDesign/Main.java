package DataStructuresDesign;

import DataStructures.Trees.*;

public class Main {

    public static void main(String[] args) {

//        System.out.println("-------------------------------------");
//
//        System.out.println("Stack Implementation");
//
//        Stack<Integer> st = new Stack<>();
//        st.push(1);
//        st.push(2);
//        st.push(3);
//        st.push(4);
//        st.push(5);
//
//        st.pop();
//
//        int stSize = st.getSize();
//
//        for(int i = 0; i < stSize; i++){
//            System.out.println(st.peek());
//            st.pop();
//        }
//
//        System.out.println("-------------------------------------");
//        System.out.println("Queue Implementation");
//
//        Queue<Integer> q = new Queue<>();
//        q.push(1);
//        q.push(2);
//        q.push(3);
//        q.push(4);
//        q.push(5);
//
//        q.pop();
//
//        int qSize = q.getSize();
//
//        for(int i = 0; i < qSize; i++){
//            System.out.println(q.peek());
//            q.pop();
//        }

        BST<String> s = new BST<>();
        s.insert(new Node<String>(15));
        s.insert(new Node<String>(3));
        s.insert(new Node<String>(1));
        s.insert(new Node<String>(12));
        s.insert(new Node<String>(18));
        System.out.println(s.min());
        System.out.println(s.max());
        System.out.println(s.getHeight());
    }
}

