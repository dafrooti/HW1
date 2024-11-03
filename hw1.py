import random

# Base class Student
class Student:
    def __init__(self, name, age, height, classes):
        self.name = name
        self.age = age
        self.height = height
        self.classes = classes

    # Getter method
    def printdetails(self):
        print(f"Name: {self.name}, Age: {self.age}, Height: {self.height}, Classes: {self.classes}")

    # Setter method   
    def changedetails(self):
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.height = input("Enter Height: ")
        self.classes = input("What are your classes: ")
        print(f"Updated Details -> Name: {self.name}, Age: {self.age}, Height: {self.height}, Classes: {self.classes}")

# Subclass SubStudent
class SubStudent(Student):
    def __init__(self, name, age, height, classes, major):
        super().__init__(name, age, height, classes)
        self.major = major

    def printmajor(self):
        print(f"Name: {self.name}, Major: {self.major}")

    # Method to generate and categorize marks
    def categorize_marks(self):
        # Generate 20 random marks between 0 and 100
        marks = [random.randint(0, 100) for _ in range(20)]
        
        # Initialize lists for different ranges of marks
        list1 = []  
        list2 = []  
        list3 = []  

        # Categorize marks
        for mark in marks:
            if mark <= 30:
                list1.append(mark)
            elif 31 <= mark <= 69:
                list2.append(mark)
            else:
                list3.append(mark)

        # Display categorized marks
        print("Need to Contact Parents:", list1)
        print("Failing Grades:", list2)
        print("Passing:", list3)
        
id2 = SubStudent("Shruti", 16, 5, "History", "Engineering")
id2.printdetails()
id2.categorize_marks()
