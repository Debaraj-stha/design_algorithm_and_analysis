# length=0
# heapSize=0

def heapify(myList,i):
    l=2*i+1
    r=2*i+2
    if l<=heapSize-1 and myList[l]>myList[i]:
        largest=l
    else:
        largest=i
    if r<=heapSize-1 and myList[r]>myList[largest]:
        largest=r
    if(largest!=i):
        myList[i],myList[largest]=myList[largest],myList[i]
        heapify(myList,largest)
def buildHeap(myList):
    global heapSize
    heapSize=length
    for i in range(length//2-1,-1,-1):
        heapify(myList,i)
def heapSort(myList):
    buildHeap(myList)
    print("after buildHeap")
    for x in myList:
        print(x,end=",")
    for i in range(length-1,0,-1):
        myList[0],myList[i]=myList[i],myList[0]
        global heapSize
        heapSize=heapSize-1
        heapify(myList,0)
        
        
lists=[9,5,1,2,7,3,4]
length=len(lists)
heapSort(lists)
print("after heapSort")
for x in lists:
    print(x,end=",")
    