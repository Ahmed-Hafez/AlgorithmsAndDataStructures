class Queue:

    def __init__(self):
        self.__size = 0
        self.__front = 0
        self.__queueContainer = []

    def get_size(self):
        return self.__size

    def push(self, item):
        self.__size += 1
        self.__queueContainer.append(item)

    def pop(self):
        if self.is_empty():
            return

        self.__queueContainer.remove(self.__queueContainer[self.__front])
        self.__size -= 1

    def peek(self):
        return self.__queueContainer[self.__front]

    def is_empty(self):
        return self.__size == 0