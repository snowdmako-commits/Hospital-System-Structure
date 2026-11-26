from appointment import Appointment
from doctor import Doctor
from patient import Patient
from datetime import datetime

class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []
        self.appointments = []