# Enter your code here. Read input from STDIN. Print output to STDOUT
stringIn1 = raw_input() # amount of money
stringIn2 = raw_input() # unique coin denominations

# convert string to int
stringIn1 = int(stringIn1)
stringIn2List = stringIn2.split()
for i in range(len(stringIn2List)):
    stringIn2List[i] = int(stringIn2List[i])

# get a power set of unique coin denominations
def powerSet(aList):
    if len(aList) == 0:
        return [[]]
    else:
        sub = powerSet(aList[1:])
        first = [aList[0]]
        withFirst = []
        for s in sub:
            withFirst.append(s + first)
        everything = sub + withFirst
        return everything

coinComb = powerSet(stringIn2List)

result = 0
for eachSet in coinComb:
    if len(eachSet) == 0:
        continue
    elif len(eachSet) == 1:
        if (stringIn1 / eachSet[0]) == int(stringIn1 / eachSet[0]):
            result = result + 1
    elif len(eachSet) == 2:
        if (stringIn1 % max(eachSet)) == 0:
            continue
        elif (stringIn1 / max(eachSet)) % min(eachSet) == 0:
            result = result + 1   
    elif len(eachSet) == 3:
        a1 = max(eachSet)
        eachSet.remove(a1)
        a2 = max(eachSet)
        a3 = min(eachSet)
        if ((stringIn1 / a1) / a2) % a3 == 0:
            result = result + 1        
    elif len(eachSet) == 4:
        a1 = max(eachSet)
        eachSet.remove(a1)
        a2 = max(eachSet)
        eachSet.remove(a2)
        a3 = max(eachSet)
        a4 = min(eachSet)
        if (((stringIn1 / a1) / a2) / a3) % a4 == 0:
            result = result + 1 
    elif len(eachSet) == 5:
        a1 = max(eachSet)
        eachSet.remove(a1)
        a2 = max(eachSet)
        eachSet.remove(a2)
        a3 = max(eachSet)
        eachSet.remove(a3)
        a4 = max(eachSet)
        a5 = min(eachSet)
        if ((((stringIn1 / a1) / a2) / a3) / a4) % a5 == 0:
            result = result + 1 
    
print result