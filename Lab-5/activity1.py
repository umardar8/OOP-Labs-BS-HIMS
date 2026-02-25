class Patient:
    def __init__(self, name, age, mrn):
        self.__name = name
        self.__age = age
        self.__mrn = mrn

    def displayInfo(self):
        print('Name of Patient is ', self.__name)
        print('Age of Patient is ', self.__age)
        print('MRN of Patient is ', self.__mrn)

    # Getter
    def displayName(self):
        print('Name of Patient is ', self.__name)

p1 = Patient("Ali", 30, "A1")

# p1.__name

p1.displayInfo()

# p1.displayName()