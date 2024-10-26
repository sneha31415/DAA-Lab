from compressionDecompression import *

def getOriginalFileSize(text):
    # each ascii char takes 8 bits 
    return 8 * len(text)

def getCompressedFileSize(text):

    charFreqMap = getCharFreqMap(text)

    # Build Huffman Tree
    root = huffmanTree(charFreqMap)

    # Generate Huffman Codes
    huffmanCodes = getHuffmanCodes(root)  

    compressedFileSize = 0
    tableSize = 0
    for char, freq in charFreqMap.items():
        compressedFileSize += (freq * len(huffmanCodes[char])) 
        tableSize += (8 + len(huffmanCodes[char]))

    return compressedFileSize + tableSize

def compressionRatio(inputFile):
    with open(inputFile, 'r') as file:
        text = file.read()

    originalSize = getOriginalFileSize(text)
    compressedSize = getCompressedFileSize(text)
    compressionRatio = originalSize / compressedSize
    
    print(f"the file is compressed to {compressionRatio:.4f} times.")
    print(f"The original file size is {originalSize} bits and compressed size is {compressedSize} bits")

inputFile = 'implementation/inputText.txt'
compressionRatio(inputFile)
    
    




