scores = input().split()

for n in range(0, len(scores)):
    scores[n] = int(scores[n])
    if n == 0:
        max = scores[n]
        next
    if scores[n] > max:
        max = scores[n]

print(max)