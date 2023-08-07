a = int (input(' enter first side :'))
b = int (input(' enter second side :'))
c = int (input(' enter third side :'))

if (c == ((a**2 + b**2) ** 1/2)):
    print('this is a right angled triangle')
if (c == a or a ==b or b ==c):
    print('this is an iscoscles triangle')
else:
    print('unknown type of triangle')






















