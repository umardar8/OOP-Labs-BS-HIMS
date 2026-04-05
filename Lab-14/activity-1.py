# Activity 1: Base Patient Class
class Patient:
    def __init__(self, pid, name, age, condition):
        self.pid = pid  # Patient ID
        self.name = name
        self.age = age
        self.condition = condition

    def __str__(self):
        return f"ID: {self.pid} | {self.name} ({self.age}) | Condition: {self.condition}"
    
    # def get_details(self):
    #     return f"ID: {self.pid} | {self.name} ({self.age}) | Condition: {self.condition}"
    
# Testing Area
p1 = Patient("P-001", "Sarah Khan", 29, "Fever")
print(p1)


# print(p1.get_details())