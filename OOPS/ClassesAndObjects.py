# class Car: 
#     # brand = 'Mercedes'

#     def __init__(self, colour, brand):
#         print(self)
#         self.colour = colour
#         self.brand = brand

#     def getColour(self):
#         print(self.colour)
    
#     def getBrand(self):
#         print(self.brand)

# car1 = Car('black', 'Mercedes')
# print(car1.getBrand())
# print(car1)


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_sum(self):
#         sum = 0
#         for i in self.marks:
#             sum += i

#         print('The sum of marks of', self.name, 'is', sum )

#     @staticmethod
#     def printHello():
#         print("Hello")

# s1 = Student('Meenakshi', [80, 90, 95]);
# s1.get_sum()
# s1.printHello()


class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Meenu")
print(s1.name)
del s1.name
print(s1.name)

         