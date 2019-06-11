package DataStructuresDesign;

import DataStructures.*;

public class Main {

    public static void main(String[] args) {


        Stack<Integer> st = new Stack<>();
        st.push(1);
        st.push(2);
        st.push(3);
        st.push(4);
        st.push(5);

        st.pop();

        int size = st.getSize();

        for(int i = 0; i < size; i++){
            System.out.println(st.peek());
            st.pop();
        }

    }
}
