# Adam Edwards-Uribe
# section 85214-66
# 9/8/22
# Lab 3

print('This program will let you raise any integer to any integer power.')
print('Remember to use only whole numbers.')
print()

# user greeting
baseNumber= input('Please enter the base number: ')

# get user input, display first input in second input line
powerNumber= int(input('What power of ' + baseNumber + ': '))

# change data type of basenumber from string to integer
baseNumber = int(baseNumber)

# calculate power
answer = baseNumber ** powerNumber
print()

# display and format result
print()
print(baseNumber, 'to the power of', powerNumber, 'is equal to', format(answer, ',.0f'))
print()
#Exit message
print('Thank you for using the power calculator.')
print('Have a nice day!')
