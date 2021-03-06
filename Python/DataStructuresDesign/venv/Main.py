from Queue import *
from Stack import *
from LinkedList import *
from HashTable import *
from Graph import *

# Queue
print("<-- Queue -->")

q = Queue()

q.push(1)
q.push(2)
q.push(3)

for i in range(q.get_size()):
    print(q.peek())
    q.pop()
print("--------------------------")

# -----------------------------

# Stack
print("<-- Stack -->")

st = Stack()

st.push(1)
st.push(2)
st.push(3)

for i in range(st.get_size()):
    print(st.peek())
    st.pop()
print("--------------------------")

# -----------------------------

# LinkedList
print("<-- LinkedList -->")

ls = LinkedList()
ls.insert(5)
ls.insert(6)
ls.insert(7)
ls.insert(9)

print(ls)

ls.remove(6)

print(ls)
print("--------------------------")

# SortedLinkedList
print("<-- SortedLinkedList -->")

sls = SortedLinkedList()

sls.insert(1)
sls.insert(3)
sls.insert(2)
sls.insert(5)
sls.insert(4)

print(str(sls))
print("--------------------------")


# -----------------------------

# HashTable
print("<-- HashTable -->")

sh = HashTable()
sh.insert(1, 5)
sh.insert(2, 6)
sh.insert(11, 5)
print(sh)
sh.insert(2, 5)
print(sh)
sh.remove(2)
print(sh)

print(sh.find(1))
print(sh.size)

print(sh.get_value(11))
print(sh.is_empty())

print("--------------------------")

# DoublyLinkedList
print("<-- DoublyLinkedList -->")

ls = DoublyLinkedList()
ls.insert_front(5)
ls.insert_front(4)
ls.insert_front(3)
ls.insert_front(2)
ls.insert_back(6)


print(ls)
ls.remove(3)
print(ls)
ls.remove(2)
print(ls)
ls.remove(6)
print(ls)
ls.remove(4)
print(ls)
ls.remove(5)
print("here, null", ls)
print("--------------------------")

# UnDirectedGraph
print("<-- UnDirectedGraph -->")

ug = UnDirectedGraph(10)

ug.add_edge(1, 5)
ug.add_edge(1, 6)
ug.add_edge(5, 2)
ug.add_edge(2, 3)
ug.add_node(4)
ug.add_node(7)
ug.add_node(9)
ug.add_node(6)

print("number of connected components =", ug.connected_components())
print(ug.visited)
print("--------------------------")
