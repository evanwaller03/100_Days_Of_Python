# with open("Day 26/file_1.txt", 'r') as f_1:
#     string_data = f_1.readlines()
#     nums_1 = [int(n) for n in string_data]

# with open("Day 26/file_2.txt", 'r') as f_2:
#     string_data = f_2.readlines()
#     nums_2 = [int(n) for n in string_data]

# overlap = [n for n in nums_1 if [m for m in nums_2 if m == n]]

# print(overlap)

with open("Day 26/file_1.txt", 'r') as f_1:
    nums_1 = f_1.readlines()

with open("Day 26/file_2.txt", 'r') as f_2:
    nums_2 = f_2.readlines()

overlap = [int(n) for n in nums_1 if n in nums_2]

print(overlap)
