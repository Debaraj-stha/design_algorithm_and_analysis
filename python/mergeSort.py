def merge(myList,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(n1):
        L[i] = myList[p + i]
    for j in range(n2):
        R[j] = myList[q + j + 1]
    L.append(float('inf'))
    R.append(float('inf'))
    i=0
    j=0
    L[n1]=float('inf')
    L[n2]=float('inf')
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            myList[k] = L[i]
            i += 1
        else:
            myList[k] = R[j]
            j += 1

def mergeSort(myList,p,r):
    if p<r:
        q=int((p+r)/2)
        mergeSort(myList,p,q)
        mergeSort(myList,q+1,r)
        merge(myList,p,q,r)
lists=[7,9,88,1,5,8,3,22]
length=len(lists)
mergeSort(lists,0,length-1)
for x in lists:
    print(x,end=",")