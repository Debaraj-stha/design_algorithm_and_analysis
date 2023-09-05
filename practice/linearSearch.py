


def linearSearch(A, key):
    length = len(A)
    index = -1
    for i in range(length):
        if A[i] == key:
            index = i
            break
    if index != -1:
        return True, index
    else:
        return False, index


def binarySearch(A, key):
    length = len(A)
    low = 0
    high = length - 1

    while low <= high:
        mid = int((low + high) / 2)
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high -= 1
        else:
            low += 1
        print(mid, A[mid])
    return -1


def bubbleSort(mylist):
    length = len(mylist)

    for i in range(length - 1):
        for j in range(length - 1 - i):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]

    for arr in mylist:
        print(arr, end=",")


def selectionSort(mylist):
    length = len(mylist)
    for i in range(length - 1):
        least = mylist[i]
        p = i
        for j in range(i + 1, length - 1):
            if mylist[j] < least:
                least = mylist[j]
                p = j
        mylist[p], mylist[i] = mylist[i], mylist[p]
    for arr in mylist:
        print(arr, end=",")


def bubbleSort(myList):
    length = len(myList)

    for i in range(length - 1):
        for j in range(length - 1 - i):
            if myList[j] < myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]

    return myList


def insertionSort(myList):
    length = len(myList)
    for i in range(1,length):
        temp = myList[i]
        j = i - 1
        while j >= 0 and myList[j] > temp:
            myList[j + 1] = myList[j]
            j = j - 1
        myList[j + 1] = temp
    for i in myList:
        print(i, end=",")


if __name__ == "__main__":
    my_list = [64, 34, 25, 12, 22, 11, 90]
    # key = int(input("Enter key to search"))
    # result, index = linearSearch(mylist, key)
    # print(result, index)
    # if result:
    #     print(f"\nsearch key is present at index {index}")
    # else:
    #     print("\nsearch key is not present")
    # binarySearchResult = binarySearch(mylist, key)
    # if binarySearchResult != -1:
    #     print(f"\nsearch key is present at index {binarySearchResult}")
    # else:
    #     print(f"\nsearch key is not present")
    sorted_list = bubbleSort(my_list)
    print("\nSorted array in descending order:", sorted_list)
    print("\nbubble sort")
    bubbleSort(my_list)
    my_list = [64, 34, 25, 12, 22, 11, 90]
    print("selection sorty\n")
    selectionSort(my_list)
    my_list = [64, 34, 25, 12, 22, 11, 90]
    print("insertion sort\n")
    insertionSort(my_list)
