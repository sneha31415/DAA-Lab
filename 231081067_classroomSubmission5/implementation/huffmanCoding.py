"""
Huffman Coding Implementation:
"""

import heapq

class Node:
    def __init__(self, freq, symbol = None, left=None, right=None):
        self.freq = freq
        self.symbol= symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def huffmanTree(charFreqMap):
    pq = [Node(freq = frequency, symbol = char) for char, frequency in charFreqMap.items()]
    heapq.heapify(pq)

    # building the huffman tree
    while len(pq) > 1:
        # extract the two nodes with the smallest freq from pq
        leftChild = heapq.heappop(pq)
        rightChild = heapq.heappop(pq)
        # push the merged node into pq
        mergedNode = Node(freq = leftChild.freq + rightChild.freq, left = leftChild, right = rightChild)
        heapq.heappush(pq, mergedNode)

    # return the last node in heap which is the root
    return heapq.heappop(pq)


# print the huffman codes using the tree
def getHuffmanCodes(root, code = "", huffmanCodes = {}):
    if root is None:
        return
    # print the code on reaching a leaf node
    if root.symbol is not None:
        huffmanCodes[root.symbol] = code

    getHuffmanCodes(root.left, code + "0", huffmanCodes)
    getHuffmanCodes(root.right, code + "1", huffmanCodes)

    return huffmanCodes

