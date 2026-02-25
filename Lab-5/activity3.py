class Patient:
    def __init__(self, name, age, mrn):
        self.__name = name
        self.__age = age
        self.__mrn = mrn

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_mrn(self):
        return self.__mrn
    
    def set_age(self, age):

        if age > 0 and age < 120:
            self.__age = age
            print(f"Successfully set age to {age}")
        else:
            print(f"{age} is not in the range")
    
p1 = Patient("Ali", 30, "A1")

print(f"Current Age: {p1.get_age()}")
p1.set_age(44)
print(f"New Age: {p1.get_age()}")