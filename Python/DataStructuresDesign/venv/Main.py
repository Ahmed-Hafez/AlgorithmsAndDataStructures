from Queue import *
from Stack import *
from LinkedList import *
from HashTable import *


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
