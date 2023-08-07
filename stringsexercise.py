#create a string (i code) and store it in a variable named var_1
var_1 = 'i code'
print(var_1)

#create a string (it's cool) and store it in a variable named var_2
var_2 = "it's cool"
print(var_2)

#count the number of characters in string var_1 
count = 0
for chars in var_1:
    count = count + 1
print(count)

#count the number of characters in string var_2
count = 0
for chars in var_2:
    count = count + 1
print(count)

#what is the index of characters 'i' and 'e' in the string var_1
index = 0
while index < len(var_1):
    i = var_1[index]
    print(index, i)
    index = index + 1
    e = var_1[index]
    print(index, e)
    index = index + 1

#print the 3rd character of var_2 from the left
print (var_2 [2:3])

#what is the value of var_1[-2]
print (var_1[-2])

#print the string var_1 using slicing technique
print (var_1[:])

#print the first 3 characters of var_2 using slicing technique
print(var_2[:3])

#print ('icd') from var_1 using slicing technique
print(var_1 [: : 2])

#reverse the string var_2
print( var_2 [: : -1])

#is this operation valid? 
print (var_2 [2] == 'd')

#concatenate a string 'is awesome' to var_1 (make sure there is a space character) and store it in var_1
var_1 = var_1 + ' is awesome'
print(var_1)

#print the string 'icd' 10 times
print('icd' * 10)

#print the string 'icd' 10 times using the slicing technique 
var_3 = 'i code'
print (var_3[: : 2]*10)

#make the character in var_1 uppercased
print(var_1.upper())

#split the string var_2 by space character
print(var_2.split())
