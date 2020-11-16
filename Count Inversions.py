#NEED PYTHON 3.8 FOR THE PROGRAM TO RUN 
#COUNTINVERSIONS USING MERGE SORT(nlogn)
#chinnam_shanmukha_sai_AMENP2CSN20009
def countInversions(S):
    if len(S)<=1:
        return S, 0
    if len(S)==2:
        if S[0]<S[1]:
            return S, 0
    def mergeSort(arr1,arr2):
        x, y, inv0, index1, index2, S = 0, 0, 0, len(arr1), len(arr2), []
        while x < index1 and y < index2:
            if arr1[x] <= arr2[y]:
                S.append(arr1[x])
                x += 1; inv0 += y
            elif arr1[x] > arr2[y]:
                S.append(arr2[y])
                y += 1
        if x!=index1:
            S.extend(arr1[x:])
            inv0 += (index1 - x) * y
        if y!=index2:S.extend(arr2[y:])
        return S, inv0
    mid = len(S)//2
    arr1, inv1= countInversions(S[:mid])
    arr2, inv2 = countInversions(S[mid:])
    sort_X, inv0 = mergeSort(arr1,arr2)
    return sort_X, inv0 + inv1 + inv2
if __name__=='__main__':
    x = input('')
    try:
        value=int(x)
    except ValueError:
        print("Only Integers, try again!")
        exit
    else:
        p,n=[],int(x)
        if(1<=(n)<=106):
            for x in range(1,n+1):
                try:
                    if 0<=(y:=int(input()))<=108:p.append(y)
                    else:
                        print("Elements range: 0-108");break
                except ValueError:
                    print("Invalid input, try again!");break
        else:
            print("N`s range: 1-106")
        print('\n')
        print(countInversions(p)[1])