global_count = 0

def choose_pivot(arr): 
	return arr[0]

def qsort(arr) :
	global global_count
	length = len(arr)
	if length < 2:
		return arr
	pivot = choose_pivot(arr)
	i, j = 1, 1
	while j < length: 
		if (arr[j] < pivot) :
			t = arr[j]
			arr[j] = arr[i]
			arr[i] = t	
			i = i + 1
		j = j + 1

	len1, len2 = len(arr[1:i]), len(arr[i:])
	
	if (len1 > 0): global_count = global_count + len1 - 1 
	if (len2 > 0): global_count = global_count + len2 - 1 

	return qsort(arr[1:i]) + [pivot] + qsort(arr[i:])



lines = [int(line.strip()) for line in open('C:/Users/c00522/Downloads/QuickSort.txt')]
#lines = [int(line.strip()) for line in open('C:/Users/c00522/Downloads/QuickSort_sample.txt')]

sorted_array = qsort(lines)

for line in sorted_array:
	print(line)

print('Answer: ', global_count)

#print(len(lines))
