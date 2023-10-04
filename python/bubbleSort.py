def bubblesort(myList):
    length = len(myList)
    for i in range(length-1):
        for j in range(length-i-1):
            if myList[j] > myList[j+1]:
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1] = temp
lists=[5,9,1,4,2,6,7]
bubblesort(lists)
for x in lists:
    print(x,end=",")