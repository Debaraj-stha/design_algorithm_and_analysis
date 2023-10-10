# Huffman Coding in python

string = 'AAAOOOOOTTTTTTTEEEEEEEEEE'

# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

# Main function implementing Huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
bits=0

for key,value in freq.items():
    bits+=value*2

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)


huffmanCode = huffman_code_tree(nodes[0][0])
print(f"Bits required  before algorithm is {bits}")
# Calculate total bits required before Huffman coding
total_bits_after = 0
for char, frequency in freq:
    total_bits_after += frequency * len(huffmanCode[char])

# Calculate total bits required after Huffman coding
encoded_string = ''.join([huffmanCode[char] for char, _ in freq])


# Print the results
print('Total bits required after Huffman coding:', total_bits_after)


# Print the Huffman codes and the original string
print('\nChar | Huffman code  | frequency')
print('--------------------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s ' % (char, huffmanCode[char]),frequency)

# Print the original and encoded strings
print('\nOriginal String:', string)
print('Encoded String  :', encoded_string)
