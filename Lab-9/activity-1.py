from abc import ABC, abstractmethod

# Task1: define ISchedulable
class ISchedulable(ABC):
    @abstractmethod
    def schedule_appointment(self, datetime_str):
        """Must be implemented to handle scheduling logic"""
        pass