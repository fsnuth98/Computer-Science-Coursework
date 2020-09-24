'''
CSC102 - Lab 04
Problem 2: Acronym Recursive
Franklin Nuth
Rasul Rasulov
February 9th, 2018
'''

def acronym1(wordsList):
    if len(wordsList) == 0:
        return ""
    else:
        currentWord = wordsList[0]
        return currentWord[0].upper() + "." + acronym1(wordsList[1:])  
    
def acronym2(wordsList, index):
    if index == len(wordsList):
        return ""
    else:
        currentWord = wordsList[index]
        return currentWord[0].upper() + "." + acronym2(wordsList, index)  
    
text = input ("Enter a phrase: ")
acro = acronym1(text.split())
print("The acronym of", text, "is", acro)
acronym2('Apple', 'p')