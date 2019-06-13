class SortingAlgorithms:

    @staticmethod
    def selection_sort(self, list):

        for i in range(len(list)):
            for j in range(len(list) - i):
                if list[i] > list[j]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
                    pass
                pass
            pass
        pass
    pass
