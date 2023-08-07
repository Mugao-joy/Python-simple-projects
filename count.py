numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count_even = 0
count_odd = 0
for number in numbers :
    if number % 2 == 0:
        count_even += 1
    elif number % 2 == 1:
        count_odd += 1
print(f'the number of even numbers is : {count_even}')
print(f'the number of odd numbers is : {count_odd}')

