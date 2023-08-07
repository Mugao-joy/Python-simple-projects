name = input( 'Enter Your Name:' )
age = int ( input ('enter your age: '))
marks = float (input('Enter your marks: '))
if (age >= 17 and age <= 21 and marks >= 80):
    print(name+ " is eligible")
else:
    print(name+ " is not eligible")