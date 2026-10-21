# class Students:
    # def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

# student1 = Students("John", 20, "Nano")
# student2 = Students("Jane", 22, "Java")
# student3 = Students("Mike", 21, "C++")

# print(type(student1))
# print(type(student2))
# print(type(student3))


# # create a class called Person with attributes name, age, complexion, and height. Create three instances of the Person class and print their attributes. Also, add a class attribute called legs with a value of 2 and print it for each instance.

# class Person:
#     legs = 2
#     def __init__(self, name, age, complexion, height):
#         self.name = name
#         self.age = age
#         self.complexion = complexion
#         self.height = height
# person1 = Person("John", 20, "Fair", 5.8)
# person2 = Person("Jane", 22, "Wheatish", 5.5)
# person3 = Person("Mike", 21, "Dark", 5.9)

# print(person1.name, person1.age, person1.complexion, person1.height)
# print(person2.name, person2.age, person2.complexion, person2.height)
# print(person3.name, person3.age, person3.complexion, person3.height)
# print(person1.legs)
# print(person2.legs)
# print(person3.legs)



# # create an instnace method for introduction that returns a string introducing the person with their name, age, complexion, and height. 


# class Person:
#     legs = "i have 3 legs"
#     def __init__(self, name, age, complexion, height):
#         self.name = name
#         self.age = age
#         self.complexion = complexion
#         self.height = height

#     def introduction(self):
#         return f"Hello, my name is {self.name} I am {self.age} years old, i am {self.complexion} incomplexion, and my height is {self.height} feet."
# person1 = Person("John", 20, "Fair", 5.8)
# person2 = Person("Jane", 22, "Wheatish", 5.5)
# person3 = Person("Mike", 21, "Dark", 5.9)

# print(person1.introduction())
# print(person2.introduction())
# print(person3.introduction())
# print(person1.legs)
# print(person2.legs)
# print(person3.legs)



# class Students:
#     ssl = 12
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#     def student_name(self):
#         return f"My name is {self.name}"

#     @classmethod
#     def get_ssl(cls, a):
#         newssl = cls.add_numbers(a) + cls.ssl
#         return newssl

#     @staticmethod
#     def add_numbers(b):
#         return 12+b

#     @property
#     def name(self):
#         # newname = self.__name + "Nano"
#         return self.__name

#     @name.setter
#     def name(self, name):
#         self.__name = name

# student1 = Students("John", 20, "Nano")
# print(student1.name)

# student1.name = "Jane"
# print(student1.name)

# student1 = Students("John", 20, "Nano")
# print(student1.get_ssl(20))


# inheritance, polymorphism, abstraction

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"My name is {self.name} and I am {self.age} years old."    
    
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def info(self):
        return f" Hi{self.name} I am studying {self.age} years old and you are a student."

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def info(self):
        return f" Hi {self.name} I am {self.age} years old and you are a teacher."

person = Person("John", 20)
student = Student("Jane", 22, "Nano")
teacher = Teacher("Mike", 30, "Math")

print(person.info())
print(student.info())
print(teacher.info())

# print(type(student))
# print(type(teacher))
# print(type(person))

typesofpeople = [person, student, teacher]

for person in typesofpeople:
    print(person.info())