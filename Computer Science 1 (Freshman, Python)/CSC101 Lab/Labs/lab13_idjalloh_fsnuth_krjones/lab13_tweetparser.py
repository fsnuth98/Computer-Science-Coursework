'''
Idrissa Jalloh
Franklin Nuth
Kareem Jones
CSC101 Lab 13
Part 3: Tweet Parser
April 28 2017
'''
import random

hashtags=[]
mentions=[]
url=[]
tweet=input("Type tweet:")
words=tweet.split()

for i in range(len(words)):
    if words[i].startswith('#'):
        hashtags.append(words[i])
    elif words[i].startswith('@'):
        mentions.append(words[i])
    elif words[i].startswith('https://'):
        url.append(words[i])
        
print("Hashtags found: ", ','.join(hashtags))
print("Mentions found: ", ','.join(mentions))
print("URLs found: ",','.join(url))