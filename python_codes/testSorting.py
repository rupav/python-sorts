import unittest
import selectionSort
import bubbleSort
import bubbleSortR
import insertionSort
import insertionSortR
import mergeSort
import quickSort
import countingSort
import radixSort
import heapSort


class Test(unittest.TestCase):
    def testSelectionSort(self):
        A = [5, 1, 3, 0, 10]
        selectionSort.selectionSort(A)
        B = [0, 1, 3, 5, 10]
        if (A != B):
            self.fail("selectionSort method fails.")

    def testBubbleSort(self):
        A = [5, 1, 3, 0, 10]
        bubbleSort.bubbleSort(A)
        B = [0, 1, 3, 5, 10]
        if (A != B):
            self.fail("bubbleSort method fails.")

    def testBubbleSortR(self):
        A = [5, 1, 3, 0, 10]
        bubbleSortR.bubbleSortR(A, len(A))
        B = [0, 1, 3, 5, 10]
        if (A != B):
            self.fail("bubbleSortR method fails.")

    def testInsertionSort(self):
        A = [5, 1, 3, 0, 10]
        insertionSort.insertionSort(A)
        B = [0, 1, 3, 5, 10]
        if (A != B):
            self.fail("insertionSort method fails.")

    def testInsertionSortR(self):
        A = [5, 1, 3, 0, 10]
        insertionSortR.insertionSortR(A, 0)
        B = [0, 1, 3, 5, 10]
        if (A != B):
            self.fail("insertionSortR method fails.")

    def testMergeSort(self):
        A = [5, 1, 3, 0, 10]
        new = mergeSort.mergeSort(A)
        B = [0, 1, 3, 5, 10]
        if (new != B):
            self.fail("mergeSort method fails.")

    def testQuickSort(self):
        A = [5, 1, 3, 0, 10]
        new = quickSort.quickSort(A)
        B = [0, 1, 3, 5, 10]
        if (new != B):
            self.fail("quickSort method fails.")

    def testCountingSort(self):
        A = [5, 1, 3, 0, 10]
        new = countingSort.countingSort(A)
        B = [0, 1, 3, 5, 10]
        if (new != B):
            self.fail("countingSort method fails.")

    def testRadixSort(self):
        A = [513, 124, 333, 101, 666]
        new = radixSort.radixSort(A)
        B = [101, 124, 333, 513, 666]
        if (new != B):
            self.fail("radixSort method fails.")

    def testHeapSort(self):
        A = [5, 1, 3, 0, 10]
        heapSort.heapSort(A)
        B = [0, 1, 3, 5, 10]
        if (A != B):
            self.fail("heapSort method fails.")
