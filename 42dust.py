# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

import mcb185
import sys
import math

file = sys.argv[1]
win = int(sys.argv[2])
entroThres = float(sys.argv[3])

def entropyCalc(p):
	assert(math.isclose(sum(p), 1.0))
	H = 0
	for i in p:
		if i != 0:
			H -= i * math.log2(i)
	return H

def nucleoEnt(seq):
	a_Comp = seq.count("A")/len(seq)
	t_Comp = seq.count("T") / len(seq)
	c_Comp = seq.count("C")/len(seq)
	g_Comp = seq.count("G") / len(seq)

	return entropyCalc([a_Comp, t_Comp, c_Comp, g_Comp])

for defline, seq in mcb185.read_fasta(file):
	print(f'>{defline}')
	characterCount = 0
	for i in range(len(seq) - win + 1):
		characterCount += 1
		if nucleoEnt(seq[i:i+win]) < entroThres:
			print("N", end='')
		else:
			print(seq[i], end='')
		if characterCount % 60 == 0:
			print('\n', end='')

"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
