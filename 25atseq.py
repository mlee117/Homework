# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers
import random

random.seed()
nt = 30
dna = ''
target = 0

for length in range(nt):
	r = random.randint(1, 100)
	if 1 <= r <= 30:
		dna += 'A'
		target += 1
	elif 31 <= r <= 60:
		dna += 'T'
		target += 1
	elif 61 <= r <= 80:
		dna += 'C'
	else:
		dna += 'G'

print(nt, target/nt, dna)

"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
