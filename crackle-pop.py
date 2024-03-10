lower, upper = 1, 100

print("(>'o')> <('o'<)")
print("Welcome to CracklePop!\n")
print("Printing numbers from {} through {}...\n".format(lower, upper))

for i in range(lower, upper+1):
    if (i % 3 != 0 and i % 5 != 0):
        print(i)
        continue

    if (i % 3 == 0):
        print("Crackle", end="")
    if (i % 5 == 0):
        print("Pop", end="")
    print()
    