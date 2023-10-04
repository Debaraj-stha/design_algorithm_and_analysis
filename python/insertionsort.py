def insertionSort(myList):
    length = len(myList)
    for i in range(1, length):
        key=myList[i]
        j=i-1
        while j>=0 and myList[j]>key:
            myList[j+1]=myList[j]
            j=j-1
        myList[j+1]=key
data=[4,9,1,3,6,30,2]
insertionSort(data)
for  x in data:
    print(x,end=",")