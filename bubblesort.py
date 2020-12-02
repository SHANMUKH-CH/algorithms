#bubble sort or sinking sort
#simplest algorithm
#swaps adj elements if they`re in wrong order
def BS(a):
    n=len(a)
    for x in range(n-1):
        for y in range(0, n-x-1):
            if a[y] > a[y+1]:
                a[y], a[y+1] = a[y+1], a[y]
a=[100,78,98,900,3,1,74,78]
BS(a)
d=[a[x] for x in range(len(a))]
print(d)
