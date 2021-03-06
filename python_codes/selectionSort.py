# The selection sort algorithm sorts an array by repeatedly finding the minimum
# element (considering ascending order) from unsorted part and putting it at the
# beginning

# selectionSort


def selectionSort(array):
	for j in range(len(array)):
		minimum_pos = j
		for i in range(j+1, len(array)):
			if array[i] < array[minimum_pos]:
				minimum_pos = i
		k = array[j]
		array[j] = array[minimum_pos]
		array[minimum_pos] = k
