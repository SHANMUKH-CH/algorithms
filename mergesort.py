# Python program for implementation of MergeSort
def mergesort(array, left, mid, right): 
	n1 = mid-left+1
	n2 = right-mid 
	# creating  temporary arrays 
	L,R = [0]*(n1), [0]*(n2)
	# Copying data to temporary arrays Left[] and Right[] 
	for x in range(0,n1): 
		L[x]=array[left+x] 
	for y in range(0,n2): 
		R[y]=array[mid+1+y] 
	# Merging the temporary arrays back into arr[l..r] 
	x,y,z = 0,0,left
	while x<n1 and y<n2 : 
		if L[x]<=R[y]: array[z]=L[x]; x+=1
		else: 
			array[z]=R[y]; y+=1
		z += 1
	# Copy the remaining elements of L[], if there are any 
	while x < n1: 
		array[z] = L[x] 
		x += 1
		z += 1
	# Copy the remaining elements of R[], if there are any 
	while y < n2: 
		array[z] = R[y] 
		y += 1
		z += 1
# sub-array of arr to be sorted 
def mergeSort(array,left,right): 
	if left<right: 
		# Same as (l+r)//2, but avoids overflow for large l and h 
		m = (left+(right-1))//2
		# Sort first and second halves 
		mergeSort(array, left, m) 
		mergeSort(array, m+1, right) 
		merges(array, left, m, right) 
if __name__=='__main__':
    arr = [12, 11, 13, 5, 6, 7] 
    n = len(arr)
    print(mergeSort(arr,0,n-1))