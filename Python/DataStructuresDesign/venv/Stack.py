class Stack:

    size = 0
    top = -1
    queueContainer = []

    @classmethod
    def get_size(cls):
        return cls.size

    @classmethod
    def push(cls, item):
        cls.size += 1
        cls.top += 1
        cls.queueContainer.append(item)

    @classmethod
    def pop(cls):
        if cls.is_empty():
            return

        cls.queueContainer.remove(cls.queueContainer[cls.top])
        cls.size -= 1
        cls.top -= 1

    @classmethod
    def peek(cls):
        return cls.queueContainer[cls.top]

    @classmethod
    def is_empty(cls):
        return cls.size == 0
