def insertionSort(mylist):
    length = len(mylist)
    for i in range(1, length):
        key=mylist[i]
        j=i-1
        while j>=0 and mylist[j]>key:
            mylist[j+1]=mylist[j]
            j=j-1
        mylist[j+1]=key

def selectionSort(mylist):
    length=len(mylist)
    for i in range(length-1):
        least=mylist[i]
        p=i
        for j in range(i+1,length-1):
            if mylist[j]<least:
                least=mylist[j]
                p=j
        mylist[i],mylist[p]=mylist[p],mylist[i]
def bubbleSort(mylist):
    length=len(mylist)
    for i in range(length-1):
        for j in range(length-1-i):
            if mylist[j]>mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
def binarySearch(myList,key):
    low=0
    high=len(myList)-1
    while low<=high:
        mid=(low+high)//2
        if myList[mid]==key:
            return mid
        elif key<myList[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
def binarySearchRecursive(myList,key,l,h):
    if l<=h:
        mid=(l+h)//2
        if myList[mid]==key:
            return mid
        elif key<myList[mid]:
            return binarySearchRecursive(myList,key,l,mid-1);
        else:
            return binarySearchRecursive(myList,key,mid+1,h)
    else:
        return -1
mylist = [18,93,4,77,2,1,62]
# selectionSort(mylist)
# for i in mylist:
#     print(i,end=",")
lists=[1,2,3,4,5,6,7,8]
key=8
x=binarySearchRecursive(lists,key,0,7)
print(x)
if x==-1:
    print("not found")
else:
    print(f"search item {key} is present at position {x}")