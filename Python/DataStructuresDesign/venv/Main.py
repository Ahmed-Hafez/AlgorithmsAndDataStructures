from Queue import *
from Stack import *
from LinkedList import *

q = Queue()

q.push(1)
q.push(2)
q.push(3)

for i in range(q.get_size()):
    print(q.peek())
    q.pop()


st = Stack()

st.push(1)
st.push(2)
st.push(3)

for i in range(st.get_size()):
    print(st.peek())
    st.pop()

ls = LinkedList()
ls.insert(5)
ls.insert(6)
ls.insert(7)
ls.insert(9)

print(ls.display_list())

ls.remove(6)

print(ls.display_list())