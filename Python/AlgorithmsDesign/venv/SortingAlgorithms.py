from Queue import *


class SortingAlgorithms:

    @staticmethod
    def selection_sort(container):

        for i in range(len(container)):
            for j in range(i, len(container)):
                if container[i] > container[j]:
                    temp = container[i]
                    container[i] = container[j]
                    container[j] = temp
                    pass
                pass
            pass
        pass
    pass

    @staticmethod
    def merge_sort(container, low, high):
        if low < high:
            mid = int((low + high) / 2)
            SortingAlgorithms.merge_sort(container, low, mid)
            SortingAlgorithms.merge_sort(container, mid + 1, high)
            SortingAlgorithms.merge(container, low, high)
            pass
        pass

    @staticmethod
    def merge(container, low, high):
        mid = int((low + high)/2)

        q1 = Queue()
        q2 = Queue()

        for i in range(low, mid+1):
            q1.push(container[i])
            pass

        for i in range(mid+1, high+1):
            q2.push(container[i])
            pass

        i = low
        while not q1.is_empty() and not q2.is_empty():
            if q1.peek() < q2.peek():
                container[i] = q1.peek()
                q1.pop()
                i += 1
                pass
            else:
                container[i] = q2.peek()
                q2.pop()
                i += 1
                pass

        while not q1.is_empty():
            container[i] = q1.peek()
            q1.pop()
            i += 1
            pass

        while not q2.is_empty():
            container[i] = q2.peek()
            q2.pop()
            i += 1
            pass
