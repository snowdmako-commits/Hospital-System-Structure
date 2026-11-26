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

    def showDoctors(self):
        if not self.doctors:
            print("\nNo doctors found!")
            return

        print("\n========== DOCTORS ==========")

        for doctor in self.doctors:
            doctor.showInfo()

    def showPatients(self):
        if not self.patients:
            print("\nNo patients found!")
            return

        print("\n========== PATIENTS ==========")

        for patient in self.patients:
            patient.showInfo()