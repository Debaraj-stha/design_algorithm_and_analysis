class Item:
    def __init__(self,value,weight):
        self.weight = weight
        self.value = value


    
def fractionalKnapsack(W, w,n):
    print("before sorting base on value/weight ratio")
    print("weight\tvalue\t\tvalue/weight")
    for i in range(0, 4):
        print(W[i].weight,"\t", W[i].value, "\t\t", W[i].value / W[i].weight)
        
    W.sort(key=lambda x: (x.value / x.weight), reverse=True)
    print("\n")
    print("after sorting base on value/weight ratio")
    
    print("weight\tvalue\t\tvalue/weight")
    for i in range(0, n):
        print(W[i].weight,"\t", W[i].value, "\t\t", W[i].value / W[i].weight)
    weight=0
    x=[0]*n
    for i in range(0, n+1):
        if weight+W[i].weight<w:
            x[i]=1
            weight=weight+W[i].weight
        else:
            x[i]=(w-weight)/W[i].weight
            weight-W[i].weight
            break
    print("Total profit: ")
    total=0
    for  i in range(len(x)):
        
        total+=x[i]*W[i].value
    print(total)
    print("x=" + str(x))

lists = [Item(280, 40), Item(100, 10), Item(120, 20), Item(120, 24)]
fractionalKnapsack(lists, 60,4)
