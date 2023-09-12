def partition(mylist,p,r):
    x=mylist[r]
    i=p-1
    for j in range(p,r):
        if mylist[j]<=x:
            i=i+1
            mylist[i],mylist[j]=mylist[j],mylist[i]
    mylist[i+1],mylist[r]=mylist[r],mylist[i+1]
    return i+1
def quicksort(mylist,p,r) :
    if p<r:
        q=partition(mylist,p,r)
        quicksort(mylist,p,q-1)
        quicksort(mylist,q+1,r)
        
item=[9,5,2,7,4,10,1]
length=len(item)
quicksort(item,0,length-1)
for i in item:
    print(i,end=",")