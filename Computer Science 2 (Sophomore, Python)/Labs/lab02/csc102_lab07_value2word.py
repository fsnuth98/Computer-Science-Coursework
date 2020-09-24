# Franklin Nuth
# Rasul Rasulov
# CSC102, Lab 2 : Value to Word
# January 26th, 2018

dictionary = ({'1':'one'}, {'2':'two'},{'3':'three'},{'4':'four'},{'5':'five'},{'6':'six'},{'7':'seven'},{'8':'eight'},{'9':'nine'},{'10':'ten'},{'11':'eleven'},{'12':'twelve'},{'13':'thirteen'},{'14':'fourteen'},{'15':'fifthteen'},{'16':'sixteen'},{'17':'seventeen'},{'18':'eighteen'},{'19':'nineteen'},{'20':'twenty'})
    
def main():
    
    value = input("Please enter a number from 0 to 99: ")
    
    for value in range(len(dictionary)):
        if value > 20:
            y = (value%10)
            value = dictionary[value[i]]
            print(dictionary.items(value))            
        else:
            value = dictionary.items()
            print(dictionary.items(value))
    
main()