# Franklin Nuth
# Rasul Rasulov
# CSC102, Lab 2 : Key Words
# January 26th, 2018

import os.path
import sys

def main():
    keyWords = {"and", "as", "assert", "break", "class", 
                "continue", "def", "del", "elif", "else",
                "except", "False", "finally", "for", "from",
                "global", "if", "import", "in", "is", "lambda",
                "None", "nonlocal", "not", "or", "pass", "raise",
                "return", "True", "try", "while", "with", "yield"}
    dictionary = {}
    for keyWords, value in dictionary:
        print(keyWords, 0)
    
    filename = input("Enter a Python source code filename: ").strip()

    if not os.path.isfile(filename):  # Check if target file exists
        print("File", filename, "does not exist")
        sys.exit()

    infile = open(filename, "r") # Open files for input 
    
    text = infile.read().split() # Read and split words from the file 
    
    count = 0
    for word in text:
        if word in keyWords:
            count += 1

    for kwrd, fq in keyWords.items():
        print("The keyword ", kwrd, "is found ", fq, "times.")
        
    print("The number of keywords in", filename, "is", count)
    
main()