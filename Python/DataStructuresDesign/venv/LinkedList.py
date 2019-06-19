class Link:

    def __init__(self, value):
        self.value = value
        self.next = None

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

        while current.value is not value:
            if current.next is None:
                return None

            current = current.next
            pass

        return current

    def display_list(self):
        list = ""

        current = self.__first

        while current is not None:
            list = list + str(current) + " "
            current = current.next

        return list
