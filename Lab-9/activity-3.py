from abc import ABC, abstractmethod

# Task1: define ISchedulable
class ISchedulable(ABC):
    @abstractmethod
    def schedule_appointment(self, datetime_str):
        """Must be implemented to handle scheduling logic"""
        pass

# Task2: implementing the interface
class Patient(ISchedulable):
    def __init__(self, name):
        self.name = name

    def schedule_appointment(self, datetime_str):
        print(f"Patient {self.name}: Appointment requested for {datetime_str}. Checking insurance...")

class Doctor(ISchedulable):
    def __init__(self, name):
        self.name = name

    def schedule_appointment(self, datetime_str):
        print(f"Dr. {self.name}: Slot reserved for {datetime_str}. Updating rounds schedule...")

# Task3: Testing the implementation
entities = [Patient("Alice"), Doctor("Smith")]

for entity in entities:
    entity.schedule_appointment("2026-03-10 10:00 AM")