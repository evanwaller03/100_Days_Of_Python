while True: 
    largeNum = int(input())
    if largeNum <= 1000:
        break
    print("Number must be less than 1,000.")

even_sum = 0

for n in range(2, largeNum+1,2):
    even_sum += n

print(even_sum)