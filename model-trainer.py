import sys
import pickle 
import os

print("Opening File...")
#inputFile = open(str(sys.argv[1]), 'r')

punctuationList = ['.', '?', '!']
firstWordList = []
wordDict = {}

isFirstWordInSetence = True

print("Building Word Dictionaries...")
with open(str(sys.argv[1]), 'r') as text:
    fullText = text.read()
    words = fullText.split()
    
    for current, next in zip(words, words[1:]):
        print(current)
        # if this is the last word, we already added everything so we're good to exit. 
        if(next is ''):
            break
    
        # if we are on the first word in a sentence
        if(isFirstWordInSetence is True):
            # add to first words array (we will use this to pick "seed" words to start sentences later)
            firstWordList.append(current)        
            isFirstWordInSetence = False
            
        # if this word isn't already in the wordDict
        if(not (current in wordDict)):
            wordDict.update({current : [next]}) # add the word as the key and create list with next word as the first val
   
        # if it already exists, we just have to add the next word to the list value associated
        else:
            wordDict[current].append(next) # already exists, append next word at key  

        # At the very end, we want to check if we've hit a word with a period. If so it's the last 
        # word in a sentence and we can set isFirstWordInSetence to true so the next word will be 
        # added to firstWordArray
        if any(x in punctuationList for x in current):
            isFirstWordInSetence = True

print(len(firstWordList))
with open(sys.argv[2], "wb") as outputFile:
    pickle.dump([firstWordList, wordDict, punctuationList], outputFile)



        


