import os
import heapq
myText = "aaadeff"
frequencyDictionary = {}

class HuffmanTree:
    def __init__(self, myText):
        self.myText = myText
        pass

    def trackFrequency(self):
                #   Track frequency of character and adds to dictionary
        for character in myText:
            if character in frequencyDictionary:
                frequencyDictionary[character] += 1
            else:
                #   if first occurance, frequency = 1
                frequencyDictionary.update({character: 1})
    
    def heapify(self):
        
        global frequencyDictionary
        # List to hold values from dictionary
        heap_dict=[]
        
        # extract the values from dictionary
        for i in frequencyDictionary.values():
            heap_dict.append(i)
            
        # heapify the values
        heapq.heapify(heap_dict)  
        print("Values of the dict after heapification :",heap_dict)
        
        # list to hold final heapified dictionary
        new_dict=[]
        
        # mapping and reconstructing final dictionary
        for i in range(0,len(heap_dict)):
            
            # Iterating the oringinal dictionary
            for k,v in frequencyDictionary.items():
            
                if v==heap_dict[i] and (k,v) not in new_dict:
                    new_dict.append((k,v))
                    
        new_dict=dict(new_dict)
        
        frequencyDictionary = new_dict
        # print("Final dictionary :",new_dict)
        
    
    def compress(self):
        self.trackFrequency()
        # self.heapify()
        
        pass
    def decompress(self):
        pass
    
tree = HuffmanTree(myText);
tree.compress()
tree.heapify()
print(frequencyDictionary)