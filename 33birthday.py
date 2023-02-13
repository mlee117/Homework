# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list
import sys
import random
input = sys.argv[1:]

people = int(input[1])
annual = int(input[0])
trials = 10000

finalCount = 0

for trial in range(1, trials+1):
	birthdays = []
	count = 0
	same = 'No'
	for i in range(1, people+1):
		dayBirth = random.randint(1, annual)
		birthdays.append(dayBirth)
	birthdays.sort()

	for i in range(len(birthdays)):
		for j in range(i + 1, len(birthdays)):
			if birthdays[i] == birthdays[j]:
				same = 'Yes'
				if same == 'Yes':
					count += 1
	if count >= 1:
		finalCount += 1

print(f'{finalCount/trials:.3f}')

"""
python3 33birthday.py 365 23
0.571
"""

