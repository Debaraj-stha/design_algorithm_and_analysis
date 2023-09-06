def bubbleSort(mylist):
    length = len(mylist)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
    print("bubbleSort:\t")
    for i in range(length - 1):
        print(mylist[i], end=",")
    print("\n")


def insertionSort(mylist):
    length = len(mylist)
    for i in range(length - 1):
        j = i - 1
        temp = mylist[i]
        while j >= 0 and mylist[j] > temp:
            mylist[j + 1] = mylist[j]
            j = j - 1

    print("insertion sort:\t")
    for i in range(length - 1):
        print(mylist[i], end=",")
    print("\n")


def selectionSort(mylist):
    length = len(mylist)
    for i in range(length - 1):
        p = i
        least = mylist[i]
        for j in range(i + 1, length - 1):
            if mylist[j] < least:
                least = mylist[j]
                p = j
        mylist[p], mylist[i] = mylist[i], mylist[p]
    print("selection sort")
    for arr in mylist:
        print(arr, end=",")


def merge(mylist, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = [0] * (n1 + 1)
    right = [0] * (n2 + 1)

    for i in range(n1):
        left[i] = mylist[p + i]
    for j in range(n2):
        right[j] = mylist[q + j + 1]

    left[n1] = float("inf") 
    right[n2] = float("inf")  

    i = 0
    j = 0

    for k in range(p, r + 1):
        if left[i] <= right[j]:
            mylist[k] = left[i]
            i = i + 1
        else:
            mylist[k] = right[j]
            j = j + 1


def mergeSort(mylist, p, r):
    if p < r:
        q = (p + r) // 2  # Use // for integer division
        mergeSort(mylist, p, q)
        mergeSort(mylist, q + 1, r)
        merge(mylist, p, q, r)


if __name__ == "__main__":
    mylist = [99, 75, 89, 3, 1, 55, 32, 2, 5]

    bubbleSort(mylist)
    insertionSort(mylist)
    selectionSort(mylist)
    mylist = [7, 33, 1, 2, 6, 8]
    length = len(mylist)
    mergeSort(mylist, 0, length - 1)
    print("\nmergesort")
    for i in mylist:
        print(i, end=",")
