# Question
'''
Given a sentence, group and print all words that are made up of the same characters
For example, 'I eat cake.  Dog loves god.  She ate lunch.  He hits himself.' ==>
    ate eat
    dog god
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import string

stringIn = raw_input()
stringRemove = string.punctuation
# remove punctuation
for char in stringRemove:
    stringIn = stringIn.replace(char, '')
# to lower case
stringIn = stringIn.lower()
# split the words into a list
stringInList = stringIn.split()

wordDict = {} # indicate whether the word has been checked
answerDict = {}
    
for i in range(len(stringInList)):
    if wordDict.get(stringInList[i]) == None:
        wordDict[stringInList[i]] = True
        answerDict[stringInList[i]] = [stringInList[i]]
    elif wordDict.get(stringInList[i]): # this word has been checked already
        continue
    for j in range(i+1, len(stringInList)):
        if wordDict.get(stringInList[j]) == None: # unchecked ones with i
            for word in answerDict:
                if len(word) == len(stringInList[j]):
                    tempDict = {}
                    for char in word:
                        if tempDict.get(char) == None:
                            tempDict[char] = 1
                        else:
                            tempDict[char] = tempDict[char] + 1
                    for char in stringInList[j]:
                        if tempDict.get(char) != None:
                            tempDict[char] = tempDict[char] - 1
                    if sum(tempDict.values()) == 0:
                        answerDict[word].append(stringInList[j])
                        wordDict[stringInList[j]] = True

answer =[]
for row in answerDict.values():
    if len(row) > 1:
        answer.append(sorted(row))
for row in sorted(answer):
    print (' ').join(row)