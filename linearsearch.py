#linear search is used on collection of items
#technique: traversing a list from start to end 
#N-size of array(int)
#time-complexity: O(N)
#pseudo code
#for(start to end of array){
#     if (current_element equals to 5){
#         print (current_index);}
#}
#python program to print the largest num using linear S
#if element(a) is present print the index of the element
def s(list,n,a):
    for i in range(0,n):
        if(list[i]==a):
            return i
    return -1
if __name__=='__main__':
    l=[1,2,3,4,5,6,7,8,9,10]
    n=len(l)
    a=8
    #calling the function
    res=s(l,n,a)
    if res==-1:
        print("nope, element is not the list")
    else:
        print("element is present at index", res)
    