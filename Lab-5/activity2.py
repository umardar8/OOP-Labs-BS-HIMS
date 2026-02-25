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
    

p1 = Patient("Ali", 30, "A1")

print(p1.__name)

print(p1.get_name())
print(p1.get_age())
print(p1.get_mrn())