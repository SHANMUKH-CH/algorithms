#jump-search(uses sorted array to find the element)
#checke less elements  by jumping ahead by fixed steps or skipping some elements in place of searching all elements.
#i.e array=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], len=16, key=10
#a[] - array; size of n; index = 0 to n-1; block of size k; ele x
#step1: jump from a[0] to a[4]
#step2: jump from a[4] to a[8]
#step3: jump from a[8] to a[12]
#step4: since the ele is at index a[10] is more we jump back a step to a[9]
#step5: perfrom linear searcg from a[8] to get the key element 10
#time complexity O(n^1/2)
import math
def Jump_Search(list_of_numbers , key): 
    n = len(list_of_numbers)
    k, previous = int(math.sqrt(n)), 0
    while list_of_numbers[int(min(k, n)-1)] < key: 
        previous = k
        k += int(math.sqrt(n))
        if previous >= n: return -1
    while list_of_numbers[int(previous)] < key:
        previous += 1
        if previous == min(k, n): return -1
    if list_of_numbers[int(previous)] == key: return previous 
    return -1
if __name__=='__main__':    
    l, key=[ 0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 30, 60, 70],60 
    ind= Jump_Search(l, key) 
    print(f'key:{key} is at index {ind}') 