def insertionsort(mylist):
    length = len(mylist)
    for i in range(1,length):
        key=mylist[i]
        j=i-1
        while j>=0 and mylist[j]>key:
            mylist[j+1]=mylist[j]
            j=j-1
        mylist[j+1]=key
item=[8,9,3,2,1,6]
insertionsort(item)
for x in item:
    print(x,end=",")
        