# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below
import sys
import random
input = sys.argv[1:]

# Variables
genomeSize = int(input[0])
readNum = int(input[1])
readLen = int(input[2])

# Getting the frags
frags = []
for i in range(1, readNum+1):
	frags.append(random.randint(1, genomeSize-readLen))

# List of elements for list frags
frags2 = []
for i in frags:
	frags2.append([i, i+readLen])

# Depth measurement
depth = []
for i in range(1, genomeSize+1):
	count = 0
	for j in frags2:
		if j[0] <= i <= j[1]:
			count += 1
	depth.append(count)

# Final Readout
print(min(depth[readLen:-readLen]), max(depth), sum(depth[readLen:-readLen])/len(depth[readLen:-readLen]))

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
