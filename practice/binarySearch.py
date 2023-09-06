def binarySearch(mylist, key):
    length = len(mylist)
    low = 0
    high = length - 1
    while low <= high:
        mid = int((low + high) / 2)
        if key == mylist[mid]:
            return mid
        elif key < mylist[mid]:
            high -= 1
        else:
            low += 1
    return -1


def binarySearchResursive(mylist, key, low, high):
    # print("calling binarySearch")
    if low <= high:
        mid = int((low + high) / 2)
        # print(mylist[mid])
        print(key)
        if key == mylist[mid]:
            return mid
        elif key < mylist[mid]:
            return binarySearchResursive(mylist, key, low, mid - 1)
        else:
            return binarySearchResursive(mylist, key, mid + 1, high)
    else:
        return -1


if __name__ == "__main__":
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 99
    # result = binarySearch(mylist, key)
    # if result == -1:
    #     print("search key not founf")
    # else:
    #     print(f"index of search key is {result}")
    length = len(mylist)
    result = binarySearchResursive(mylist, key, 0, length - 1)
    if result == -1:
        print("search key not found")
    else:
        print(f"index of search key is {result}")
