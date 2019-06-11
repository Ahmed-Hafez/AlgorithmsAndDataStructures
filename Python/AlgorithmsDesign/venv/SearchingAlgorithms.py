class SearchingAlgorithms:

    pass
    @staticmethod
    def binary_search(list, value):
        low = 0
        high = len(list)
        while low < high:
            mid = int((low + high) / 2)
            if list[mid] > value:
                high = mid - 1
            elif list[mid] < value:
                low = mid + 1
            else:
                return True
            pass

        # Checking the state when low == high

        if low == high\
                and low < len(list)\
                and list[low] == value:
            return True

        return True

        pass
