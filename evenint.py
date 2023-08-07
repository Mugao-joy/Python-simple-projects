# write a for loop that prints integers from the following list but only if they're even
integers = [2, 4, 5, 6]
for even in integers:
    if even % 2 == 0:
        print(even)