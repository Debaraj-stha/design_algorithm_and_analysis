def partition(myList,p,r):
    x=myList[r]
    i=p-1
    for j in range(p,r):
        if myList[j]<x:
            i=i+1
            myList[i],myList[j]=myList[j],myList[i]
    myList[i+1],myList[r]=myList[r],myList[i+1]
    for a in myList:
        print(a,end=",")
    print("\n")
    return i+1

def quickSort(myList,p,r):
    if p<r:
        q=partition(myList,p,r)
        quickSort(myList,p,q-1)
        quickSort(myList,q+1,r)
lists=[8,9,3,2,5,7]
length=len(lists)
quickSort(lists,0,length-1)
print("quick dort")
for x in lists:
    print(x,end=",")