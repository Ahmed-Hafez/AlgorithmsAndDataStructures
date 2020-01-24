package DataStructures.Trees;

public class Node<T>{
    int key;
    T data;
    Node<T> RightChild, LeftChild;
    public Node(int key){
        this.key = key;
    }

    @Override
    public String toString() {
        return "" + key;
    }
}
