number = int (input ('enter a number: '))
n = int(input('enter the power: '))
nth_power = number ** n
if (nth_power % 2 == 0):
    print('nth_power of this number is even')
else:
    print('nth_power of this number is odd')