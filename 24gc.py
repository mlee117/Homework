import math
# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

target = 0
seq = 0

for i in range(len(dna)):
    if dna[i] == "G" or dna[i] == "C":
        target += 1
    seq += 1
gc = math.ceil((target/seq)*100)/100

print(gc)

"""
python3 24gc.py
0.42
"""
