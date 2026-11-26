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

    def addDoctor(self, doctor):
        self.doctors.append(doctor)
        print("\nDoctor added successfully!")

    def addPatient(self, patient):
        self.patients.append(patient)
        print("\nPatient added successfully!")