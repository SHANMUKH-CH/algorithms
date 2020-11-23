#BS is a popular search algo
#efficent and more commonly used technique to solve problems
#works on sorted elements or array
#number of iterations will be reduced by the value that is being searched
#A=[0,1,2,3,4,5,6,7,8,9]
#low=0; high=n-1
#median of the low and high bounds is (lower_bound + upper_bound)/2=4
#implementation - recursive
# Returns index of x in arr if present, else -1 
def BS(l, low, high, key): 
	# Check base case 
	if high>=low: 
		mid = (high + low)//2
		# If element is present at the middle itself 
		if l[mid] == x: 
			return mid 
		# If element is smaller than mid, then it can only 
		# be present in left subarray 
		elif l[mid] > x: 
			return BS(l, low, mid - 1, x) 
		# Else the element can only be present in right subarray 
		else: 
			return BS(l, mid + 1, high, x) 
	else: 
		# Element is not present in the array 
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
