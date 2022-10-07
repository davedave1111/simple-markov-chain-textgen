import sys
import pickle
import random

model = pickle.load(open(sys.argv[1],'rb'))

firstWordList = model[0]
wordDict = model[1]
punctuationList = model[2]

for i in range(int(sys.argv[2])):
    #print(firstWordList)
    sentence = currentWord = firstWordList[random.randint(0, len(firstWordList))-1]
    while(not any(x in punctuationList for x in sentence)):
        sentence += " "
        randIndex = random.randint(0, len(wordDict[currentWord])-1)
        nextWord = wordDict[currentWord][randIndex]
        sentence += nextWord 

        currentWord = nextWord
    
    print(sentence)

