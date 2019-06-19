from SearchingAlgorithms import *
from MathAlgorithms import *
from SortingAlgorithms import *
from Queue import *

container = [7, 6, 9, 2, 4, 6, 1, 2]
print(container)
#SortingAlgorithms.selection_sort(container)
#SortingAlgorithms.merge_sort(container, 0, len(container)-1)
container = SortingAlgorithms.quick_sort(container)
print(container)

print(MathAlgorithms.KaratsubaMultiplication(12345, 6789))

print(SearchingAlgorithms.binary_search([1, 2, 3, 4, 5, 6], 3))
