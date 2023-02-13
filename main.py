import os
myText = "aaa bb cc deff"
frequencyDictionary = {}

class HuffmanTree:
    def __init__(self, myText):
        self.myText = myText
        pass

    def compress(self):
        
        for character in myText:
            if character in frequencyDictionary:
                frequencyDictionary[character] += 1
            else:
                frequencyDictionary.update({character: 1})
        
        pass
    
    def decompress(self):
        pass
    
tree = HuffmanTree(myText);
tree.compress()
print(frequencyDictionary)