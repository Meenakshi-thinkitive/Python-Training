 # a list of three elements
ages = [19, 26, 29]
print(ages)


# an empty list
empty_list = []
print(empty_list)

# a list containing strings and numbers
student = ['Jack', 32, 'Computer Science']
print(student)
print(student[0])
print(student[-1])
print(student[1:])

student.append("Harsh")
print(student)
student.insert(2, 'Shikha')
print(student)

numbers = [1,2,3]
numbers.extend(student)
print(numbers)
numbers[2] = 4
print(numbers)
# remove- removes element with the given ele and not the index
numbers.remove(4) 
print(numbers)
print(len(numbers))

# create a list with square values --- Comprehensions
numbers = [n**2 for n in range(1, 6)]
print(numbers)    

# Output: [1, 4, 9, 16, 25]