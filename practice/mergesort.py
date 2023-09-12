def merge(mylist,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*(n1+1)
    R=[0]*(n2+1)
    for i in range(n1):
        L[i]=mylist[p-i]
    for j in range(n2):
        R[j]=mylist[q+i+1]
    R[n1]=float('inf')
    L[n2]=float('inf')
    i=0
    j=0
    for k in range(p,r+1):
        if L[i]<=R[j]:
            mylist[k]=L[i]
            i=i+1
        else:
            mylist[k]=R[j]
            j=j+1
def mergesort(mylist,p,r):
    if p<r:
        q=(p+r)//2
        mergesort(mylist,p,q)
        mergesort(mylist,q+1,r)
        merge(mylist,p,q,r)
item=[8,9,3,2,1,6]
length=len(item)
mergesort(item,0,length-1)
for i in item:
    print(i,end=",")