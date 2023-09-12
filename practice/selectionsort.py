def selection(mylist):
    length = len(mylist)
    for i in range(length-1):
        p=i
        least=mylist[i]
        for j in range(i + 1, length ):
            if mylist[j] < least:
                least = mylist[j]
                p = j
        mylist[p], mylist[i] = mylist[i], mylist[p]

item=[8,9,3,2,1,6]
selection(item)
for x in item:
    print(x,end=",")