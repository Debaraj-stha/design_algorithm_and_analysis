def minmax(myList,i,j):
    min1=0;
    max1=0;
    if(i==j):
        global min0,max0
        min0=max0=myList[i]
    elif(i==j-1):
        if(myList[i]<myList[j]):
            max0=myList[j]
            min0=myList[i]
        else:
            max0=myList[i]
            min0=myList[j]
    else:
        mid=(i+j)//2
        minmax(myList,i,mid)
        min1=min0
        max1=max0
        minmax(myList,mid+1,j)
        if max0<max1:
            max0=max1
        if min0>min1:
            min0=min1
lists=[2,8,43,1,92,4,7]
length=len(lists)
minmax(lists,0,length-1)
print(f"min={min0} max={max0}")