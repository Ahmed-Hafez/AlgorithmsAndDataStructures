package DataStructures.Trees;

public class BST<T> {

    private Node<T> Root;

    public Node<T> getRoot() {
        return Root;
    }

    public void insert(Node node){
        if (Root == null) {
            Root = node;
            return;
        }
        Node<T> current = Root;
        Node<T> parent = Root;
        while(current != null){
            parent = current;
            if(node.key >= current.key)
                current = current.RightChild;
            else
                current = current.LeftChild;
        }
        if(node.key >= parent.key)
            parent.RightChild = node;
        else
            parent.LeftChild = node;
    }

    public Node min(){
        Node<T> current = Root;
        Node<T> last = Root;
        while(current != null){
            last = current;
            current = current.LeftChild;
        }
        return last;
    }

    public Node max(){
        Node<T> current = Root;
        Node<T> last = Root;
        while(current != null){
            last = current;
            current = current.RightChild;
        }
        return last;
    }

    public int getHeight(){
        return height(Root);
    }

    private int height(Node<T> node){
        if(node == null) return 0;
        return Math.max(height(node.LeftChild), height(node.RightChild)) + 1;
    }
}
