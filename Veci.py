"""
Kattis Problem Veci

Your program will be given an integer X. Find the smallest number larger than X consisting of the same digits as X.
"""

from itertools import combinations
#### Example
# 2416 => 2461
# 330 => 0

# The integer X (1 ≤ X ≤ 999999). The first digit in X will not be a zero.
user_input = str(input())
# Split into array of the numbers in String/Integer form
str_numbers = list(user_input)
int_numbers = [int(x) for x in str_numbers]

# ============= The Stupid Way ================== #
combinations = combinations(str_numbers)

for item in combinations:
	print(item)

