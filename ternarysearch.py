#ternary search.
#ternary search is a searching technique.
#array/list is divided into  parts and then you determine in which part the element exists.
#its a divide and conquer algo.
#array to be sorted before you search.
#when the function cannot be differentiated easily, ternary search is useful. It is less prone to errors and easy to implement when
#Dealing with floating point integers, Required maximum value is reached at the end of the interval.
def TS(LIST,key):
   l,r =0, len(LIST)-1
   while l <= r:
      L1 = l
      L2 = l + (r - l) // 3
      L3 = l + 2 * (r - l) // 3
      if key == LIST[l]: return('there`s a Key at:' +str(l))
      elif key == LIST[r]: return('Key found at:' +str(r))
      elif key < LIST[l] or key > LIST[r]: return("No key")
      elif key <= LIST[L2]: r = L2
      elif key > LIST[L2] and key <= LIST[L3]:
         l = L2 + 1
         r = L3
      else: l = L3 + 1
   return
if __name__=='__main__':
   print(TS([1,2,3,4,5,6,7,8,9,10],10))