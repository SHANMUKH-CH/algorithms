#BS is a popular search algo
#efficent and more commonly used technique to solve problems
#works on sorted elements or array
#number of iterations will be reduced by the value that is being searched
#A=[0,1,2,3,4,5,6,7,8,9]
#low=0; high=n-1
#median of the low and high bounds is (lower_bound + upper_bound)/2=4
#implementation - iterative
# Iterative Binary Search Function 
# It returns index of x in given array arr if present, 
# else returns -1 
def BS(l, key): 
	low = 0
	high = len(l) - 1
	mid = 0
	while low <= high: 
		mid = (high + low) // 2
		# Check if x is present at mid 
		if l[mid] < key: 
			low = mid + 1
		# If x is greater, ignore left half 
		elif l[mid] > key: 
			high = mid - 1
		# If x is smaller, ignore right half 
		else: 
			return mid 
	# If we reach here, then the element was not present 
	return -1
if __name__=='__main__': 
    l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    x = 10
    # Function call 
    y=BS(l, 0, len(l)-1, x)
    if y!= -1:
        print("Ele is at index", str(y)) 
    else:
        print("Ele is not in the list") 