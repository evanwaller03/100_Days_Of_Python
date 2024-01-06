import random

print("Coin Toss Game:")
selection = input("Heads(h) or Tails(t)")


rand_int = random.randint(0,1)

if selection.lower() == 'h' and rand_int == 1:
    print("Heads, you won.")
elif selection.lower() == 'h' and rand_int == 0:
    print("Tails, you lost.")
elif selection.lower() == 't' and rand_int == 1:
    print("Heads, you lost.")
else:
    print("Tails, you won.")