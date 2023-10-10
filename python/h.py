string = 'AAAOOOOOTTTTTTTEEEEEEEEEE'
class Nodes(object):
    def __init__(self,left=None,right=None):
        self.left=left
        self.right=right
    def __str__(self):
        return '%s_%s' %(self.left,self.right)
    def children(self):
        return (self.left,self.right)
    def nodes(self):
        return (self.left,self.right)
def huffman(node,left=True,binString=""):
    if type(node) is str:
        return{node:binString}
    (l,r)=node.children()
    d=dict()
    d.update(huffman(l,True,binString+"0"))
    d.update(huffman(r,True,binString+"1"))
    return d
freq={}
for c in string:
    if c in freq:
        freq[c]+=1
    else:
        freq[c]=1
total_bits_before=0
for key,value in freq.items():
    total_bits_before+=value*2
print(total_bits_before)
freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
nodes=freq
while(len(nodes)>1):
    (key1,c1)=nodes[-1]
    (key2,c2)=nodes[-2]
    node=nodes[:-2]
    node = Nodes(key1, key2)
    nodes.append(node,c1+c2)
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    
    
    

    
        