from abc import ABC, abstractmethod
from datetime import datetime

# Abstraction Example
class HospitalStaff(ABC):
    def __init__(self, name):
        self.name = name

    def attendance(self):
        print(f"{self.name} clocked in at {datetime.now()}")

    @abstractmethod
    def perform_duty(self):
        pass

class Surgeon(HospitalStaff):
    def __init__(self, name):
        super().__init__(name)

    def perform_duty(self):
        print(f"{self.name} is performing surgery in ward A")

# -------------------------------------------------------
# Interface Example

class IDevice(ABC):

    @abstractmethod
    def start_device(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

class HeartMonitor(IDevice):
    def start_device(self):
        print("Starting the sensors for detecting heart beat")

    def get_status(self):
        print("Heartbeat at 72 BPM (Normal)")
        
# Execution of Abstraction
s = Surgeon("Mohsin")
s.perform_duty()

# Execution of Interface
h = HeartMonitor()
h.start_device()
h.get_status()