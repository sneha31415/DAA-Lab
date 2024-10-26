"""
File Compression and Decompression: using Huffman Coding.
Input: A text file.
Output: A compressed binary file and a corresponding code table.
"""

from huffmanCoding import *
import pickle

def getCharFreqMap(text):
    freqMap = {}
    
    for char in text:
        if char in freqMap:
            freqMap[char] += 1
        else:
            freqMap[char] = 1
    
    return freqMap


def encodeString(text, huffman_codes):
    encodedString = ''.join([huffman_codes[char] for char in text])
    return encodedString


def write_compressed_file(outputPath, encodedString):
    myByteArray = bytearray()

    # Convert binary string to bytes
    for i in range(0, len(encodedString), 8):
        byte_chunk = encodedString[i:i + 8]
        myByteArray.append(int(byte_chunk, 2))

    with open(outputPath, 'wb') as file:
        file.write(myByteArray)


# Save the Huffman code table for decompression
def save_huffman_codes(outputPath, huffman_codes):
    with open(outputPath, 'wb') as file:
        pickle.dump(huffman_codes, file)

# Main function
def compress_file(input_file, outputBinaryFile, huffmanCodetable):
    with open(input_file, 'r') as file:
        text = file.read()

    # Create a frequency map of characters
    charFreqMap = getCharFreqMap(text)

    # Build Huffman Tree
    root = huffmanTree(charFreqMap)

    # Generate Huffman Codes
    huffmanCodes = getHuffmanCodes(root)

    # Encode the text using Huffman codes
    encodedString = encodeString(text, huffmanCodes)

    # Write the encoded data to a binary file
    write_compressed_file(outputBinaryFile, encodedString)

    # Save the Huffman codes to a file for decompression
    save_huffman_codes(huffmanCodetable, huffmanCodes)

inputFile = 'implementation/inputText.txt'  
outputBinaryFile = 'output.bin' 
HuffmanCodeTable = 'HuffmanCodeTable.pkl'  

compress_file(inputFile, outputBinaryFile, HuffmanCodeTable)