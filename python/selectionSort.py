def selectionSort(myList):
    length = len(myList)
    for i in range(length-1):
        p=i
        least=myList[i]
        for j in range(i+1,length):
            if myList[j]<least:
                least=myList[j]
                p=j
        myList[p],myList[i]=myList[i],myList[p]
lists=[7,2,9,1,9,46,20]
selectionSort(lists)
for x in lists:
    print(x,end=",")