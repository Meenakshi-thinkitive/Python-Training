number = -5

if number > 0:
    print('Positive number')

elif number < 0:
    print('Negative number')

else:
    print('Zero')

print('This statement is always executed')

#ternary o/p

grade = 40

if grade >= 50:
    result = 'pass'
else:
    result = 'fail'

print(result)

result = 'pass' if number >= 50 else 'fail'

print(result)
