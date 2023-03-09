# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. has option and default value for window size
# 2. has option and default value for entropy threshold
# 3. has a switch for N-based or lowercase (soft) masking
# 4. works with uppercase or lowercase input files
# 5. works as an executable
# 6. outputs a FASTA file wrapped at 60 characters

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

#!/usr/bin/env python3

import mcb185
import math
import argparse


def entropyCalc(p):
	assert (math.isclose(sum(p), 1.0))
	H = 0
	for i in p:
		if i != 0:
			H -= i * math.log2(i)
	return H


def nucleoEnt(seq):
	a_Comp = (seq.count("A") + seq.count("a")) / len(seq)
	t_Comp = (seq.count("T") + seq.count("t")) / len(seq)
	c_Comp = (seq.count("C") + seq.count("c")) / len(seq)
	g_Comp = (seq.count("G") + seq.count("g")) / len(seq)

	return entropyCalc([a_Comp, t_Comp, c_Comp, g_Comp])


parser = argparse.ArgumentParser(description='Better Dust')

parser.add_argument('file', type=str, metavar='<path>', help='Input')
parser.add_argument('-w', required=False, type=int, default=11, metavar='<int>', help='Custom window size input (default: 11).')
parser.add_argument('-t', required=False, type=float, default=1.4, metavar='<float>', help='Custom entropy threshold (default: 1.4).')
parser.add_argument('-s', required=False, action='store_true', help='N-based or lowercase (soft) masking.')

arg = parser.parse_args()

for defline, seq in mcb185.read_fasta(arg.file):
	print(f'>{defline}')
	characterCount = 0
	isBad = 0
	for i in range(len(seq) - arg.w + 1):
		characterCount += 1
		if nucleoEnt(seq[i:i + arg.w]) < arg.t:
			if arg.s:
				print(seq[i].lower(), end='')
			else:
				print("N", end='')
			isBad = arg.w - 1
		elif isBad > 0:
			if arg.s:
				print(seq[i].lower(), end='')
			else:
				print("N", end='')
			isBad -= 1
		else:
			print(seq[i], end='')
		if characterCount % 60 == 0:
			print('\n', end='')

"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGcttttcattctGACTGCAACGGGCAATATGTCTCTGTGTggattaaaaaaagagtgTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGagtaaattaaaattttattgaCTTAGG
TCACtaaatactttaaCCAATATAGGCATAGCGCACAGacagataaaaattacaGAGTac
acaacatccaTGAAACGCATTAGCACCACCATtaccaccaccatcaccaTTACCACAGGT
AACggtgcgggctgACGCGTACAGgaaacacagaaaaaagccCGCACCTGACAGTGCggg
ctttttttttcgaCCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AggcaggggcaggtggCCAccgtcctctctgcccccgccaaaatcaccaaccacctGGTG
GCGATgattgaaaaaaccattaGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
"""
