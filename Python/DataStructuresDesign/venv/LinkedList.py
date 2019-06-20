class Link:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.__first = None

    def insert(self, value):
        link = Link(value)
        link.next = self.__first
        self.__first = link

    def remove(self, value):

        if self.__first is None:
            raise Exception("Ops, The list is empty")

        current = self.__first
        previous = self.__first

        while current.value is not value:
            if current.next is None:
                raise Exception("Item not found")

            previous = current
            current = current.next

        if current is self.__first:
            self.__first = self.__first.next
            pass
        else:
            previous.next = current.next

    def find(self, value):
        current = self.__first

        while current is not None and\
                current.value is not value:
            if current.next is None:
                return None

            current = current.next
            pass

        return current

    def __str__(self):
        list = ""

        current = self.__first

        while current is not None:
            list = list + str(current) + " "
            current = current.next

        return list


class SortedLinkedList:

    def __init__(self):
        self.__first = None

    def insert(self, value):
        link = Link(value)

        current = self.__first
        previous = None

        while current is not None and current.value < value:
            previous = current
            current = current.next
            pass

        if previous is None:  # In the beginning
            self.__first = link
            pass

        else:
            previous.next = link
            pass

        link.next = current

    def remove(self, value):

        if self.__first is None:
            raise Exception("Ops, The list is empty")

        current = self.__first
        previous = self.__first

        while current.value is not value:
            if current.next is None:
                raise Exception("Item not found")

            previous = current
            current = current.next

        if current is self.__first:
            self.__first = self.__first.next
            pass
        else:
            previous.next = current.next

    def find(self, value):
        current = self.__first

        while current is not None and\
                current.value is not value:

            if current.next is None:
                return None

            current = current.next
            pass

        return current

    def __str__(self):
        list = ""

        current = self.__first

        while current is not None:
            list = list + str(current) + " "
            current = current.next
        return list


class DoublyLinkedList:

    def __init__(self):
        self.__first = None
        self.__last = None

    def insert_front(self, value):
        link = Link(value)
        if self.__last is None:
            self.__last = link
            pass
        else:
            self.__first.previous = link
            pass
        link.next = self.__first
        self.__first = link

    def insert_back(self, value):
        link = Link(value)
        if self.__first is None:
            self.__first = link
            pass
        else:
            self.__last.next = link
            pass
        link.previous = self.__last
        self.__last = link

    def remove(self, value):

        node = self.find(value)
        if node is not None:
            if node.previous is not None:
                node.previous.next = node.next
                pass
            else:
                self.__first = node.next
            if node.next is not None:
                node.next.previous = node.previous
                pass
            else:
                self.__last = node.previous
            pass
        else:
            raise Exception("Item not found")

    def find(self, value):
        current = self.__first

        while current is not None and\
                current.value is not value:

            if current.next is None:
                return None

            current = current.next
            pass

        return current

    def __str__(self):
        list = ""

        current = self.__first

        while current is not None:
            list = list + str(current) + " "
            current = current.next

        return list
