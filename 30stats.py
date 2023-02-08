# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys
import sys

numList = []
sumPow = 0

# Getting the input values from command line and converting it to an integer list
for i in range(1, len(sys.argv)):
	numList.append(sys.argv[i])
numList.sort()
numList = [int(i) for i in numList]

# Standard deviation maths
for i in numList:
	sumPow += (i - sum(numList)/len(numList)) ** 2
stdev = (sumPow / len(numList)) ** 0.5

# Median maths
if len(numList) % 2 == 0:
	A = numList[len(numList)//2]
	B = numList[len(numList)//2-1]
	median = (A + B) / 2
else:
	median = numList[len(numList)//2]

print(f"Count: {len(numList)}")
print(f"Minimum: {float(min(numList))}")
print(f"Maximum: {float(max(numList))}")
print(f"Mean: {float(sum(numList)/len(numList)):.3f}")
print(f"Std. dev: {stdev:.3f}")
print(f"Median: {median:.3f}")

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
