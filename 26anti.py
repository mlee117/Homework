# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
comp = ''

for i in range(len(dna)):
	rev = dna[i]
	if rev == 'A':
		comp += 'T'
	elif rev == 'T':
		comp += 'A'
	elif rev == 'C':
		comp += 'G'
	elif rev == 'G':
		comp += 'C'
print(comp[::-1])

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""