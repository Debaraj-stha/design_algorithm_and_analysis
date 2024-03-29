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
        for j in range(i + 1, length):
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


def partition(mylist, p, r):
    x = mylist[r]
    i = p - 1
    for j in range(p, r):
        if mylist[j] <= x:
            i = i + 1
            mylist[i], mylist[j] = mylist[j], mylist[i]
    mylist[i + 1], mylist[r] = mylist[r], mylist[i + 1]
    return i + 1


def quicksort(mylist, p, r):
    if p < r:
        q = partition(mylist, p, r)
        quicksort(mylist, p, q - 1)
        quicksort(mylist, q + 1, r)


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
    mylist = [9, 6, 5, 1, 7, 22, 4]
    length = len(mylist)
    print("\nquic sort")
    quicksort(mylist, 0, length - 1)
    for i in mylist:
        print(i, end=",")
