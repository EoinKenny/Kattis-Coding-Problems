import sys


case = 0

for user_input in sys.stdin:

	case+= 1

	nums = user_input.split(" ")[1:]
	nums = [int(x) for x in nums]
	min_num = min(nums)
	max_num = max(nums)

	print("Case", str(case) + ":", min_num, max_num, max_num - min_num)