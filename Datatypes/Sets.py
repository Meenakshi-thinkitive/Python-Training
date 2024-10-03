# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

student_id.add(117)
print(student_id)


# create an empty set
empty_set = set()


companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

# using update() method
companies.update(tech_companies)

print(companies)


languages = {'Swift', 'Java', 'Python'}

print('Initial Set:',languages)

# remove 'Java' from a set
removedValue = languages.discard('Java')

print('Set after remove():', languages)
print(removedValue) 