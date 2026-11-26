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

    def createAppointment(self, doctorID, patientID, date, time):

        doctor = None
        patient = None

        for d in self.doctors:
            if d.doctorID == doctorID:
                doctor = d
                break

        for p in self.patients:
            if p.patientID == patientID:
                patient = p
                break

        if doctor is None:
            print("\nDoctor not found!")
            return

        if patient is None:
            print("\nPatient not found!")
            return

        try:
            appointmentDate = datetime.strptime(date, "%Y-%m-%d")     # bu hisseni ai - dan istedim appointmentDate birde appointmentTime
            appointmentTime = datetime.strptime(time, "%H:%M")        #

            if appointmentDate.date() < datetime.today().date():
                print("\nYou cannot create an appointment in the past!")
                return

        except ValueError:
            print("\nInvalid date or time format!")
            print("Date format: YYYY-MM-DD")
            print("Time format: HH:MM")
            return

        appointmentID = max([a.appointmentID for a in self.appointments],default=0) + 1

        appointment = Appointment(appointmentID,doctor,patient,date,time)

        self.appointments.append(appointment)

        print("\nAppointment created successfully!")
        appointment.showInfo()

    def showAppointments(self):
        if not self.appointments:
            print("\nNo appointments found!")
            return

        print("\n========== ALL APPOINTMENTS ==========")

        for appointment in self.appointments:
            appointment.showInfo()