# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input
import sys
import math

numList = []
H = 0

# Getting numbers from command line and text-number conversion
for i in range(1, len(sys.argv)):
	try:
		p = float(sys.argv[i])
		assert(p > 0 and p <= 1)
	except:
		raise
	numList.append(p)
numList.sort()
assert(math.isclose(sum(numList), 1.0))

# Shannon Entropy Calculator
for i in numList:
	H -= i * math.log2(i)
print(f"{H:.3f}")

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
