class Girl:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def smiles(self):
        return f"{self.name} smiles."
    
    def studies(self):
        return f"{self.name} studies hard."
    
class Student(Girl):  #Inheritance
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade  

    # (Polymorphism)
    def studies(self):
        return f"{self.name} studies hard and is in grade {self.grade}."

# Instances
girl_1 = Girl("Alice", 25)
girl_2 = Student("Laurine", 20, "12th")

# Methods
print(girl_1.smiles())  
print(girl_2.studies()) 