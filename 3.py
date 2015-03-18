# Question
'''
Given M money, find number of way to make changes use coins in list N
For example, 10 cents with [1 5 10] cents ==> 4
    1   5   10
    ----------
    0   0   1
    0   2   0
    5   1   0
    10  0   0
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
stringIn1 = raw_input() # amount of money
stringIn2 = raw_input() # unique coin denominations

# convert string to int
stringIn1 = int(stringIn1)
stringIn2List = stringIn2.split()
for i in range(len(stringIn2List)):
    stringIn2List[i] = int(stringIn2List[i])

def uniqueWay(number, factorSet,innerLoop=False):
    way = 0
    if (number == 0) and not innerLoop: # no money input, so just return 0
        return 0
    elif (number == 0) and innerLoop:
        return 1
    elif len(factorSet) == 0: # no changes input, so just return 0
        return 0
    elif len(factorSet) == 1:
        if (number / float(factorSet[0])) == int(number / factorSet[0]) \
            and (number / float(factorSet[0])) > 0:
            return 1
        else: # remaining money cannot use the last coin for change
            return 0
    else:
        # remaining money cannot use the last 2 coins for change
        if len(factorSet) == 2 and \
            (number % max(factorSet)) % min(factorSet) > 0:
            return 0        
        else:
            factorSetTemp = factorSet[:]
            a1 = max(factorSetTemp)
            factorSetTemp.remove(a1)
            for k in range((number/a1)+1):
                way = way + uniqueWay( (number - (k*a1)), factorSetTemp, True)
            return way

print uniqueWay(stringIn1, stringIn2List)

# Test cases
# ----------
print uniqueWay(10, [1,5,10])
# 4
print uniqueWay(14, [1,3,5])
# 11
print uniqueWay(100, [1,5,10,25,50,100])
# 293

'''
Original approach using powerset.  Will not result in unique way, but instead
just the possible ways grouped by coins.  For example, 10 and [1, 5, 10] ==> 3
Have errors and do not produce the correct results
'''
'''
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
        if (stringIn1 / float(eachSet[0])) == int(stringIn1 / eachSet[0]):
            result = result + 1
    elif len(eachSet) > 1:
        j = len(eachSet)
        if (stringIn1 / max(eachSet)) == 1:
            continue
        else:
            while j > 2:
                a1 = max(eachSet)
                eachSet.remove(a1)
                stringIn1 = stringIn1 % a1
                j = j - 1
            if (stringIn1 % max(eachSet)) % min(eachSet) == 0:
                result = result + 1
    print eachSet, result
'''