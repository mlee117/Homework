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
total = 0

for length in range(nt):
	r = random.randint(1, 100)
	if 1 <= r <= 30:
		dna += 'A'
	elif 31 <= r <= 60:
		dna += 'T'
	elif 61 <= r <= 80:
		dna += 'C'
	elif 81 <= r <= 100:
		dna += 'G'

for i in range(len(dna)):
	if dna[i] == "A" or dna[i] == "T":
		target += 1
	total += 1
at = target/total

print(total, at, dna)

"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
