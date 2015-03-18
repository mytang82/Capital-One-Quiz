# Question
'''
Find number of ways one can get N heads from M flip
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
stringIn = raw_input()
stringInList = stringIn.split()
M = int(stringInList[0])
N = int(stringInList[1])
print math.factorial(M)/(math.factorial(N)*math.factorial(M-N))