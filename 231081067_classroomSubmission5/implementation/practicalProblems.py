"""
Instructions : 

Given a sample string (e.g., "hello world"), encode it using Huffman Coding.
Input: A string.
Output: The encoded binary string
"""

from compressionDecompression import *
from huffmanCoding import *


inputText = "hellllo world"

charFreqMap = getCharFreqMap(inputText)
root = huffmanTree(charFreqMap)
huffmanCodes = getHuffmanCodes(root)
print(huffmanCodes)

encodedString = encodeString(inputText, huffmanCodes)
print(f"the encoded String is {encodedString}")