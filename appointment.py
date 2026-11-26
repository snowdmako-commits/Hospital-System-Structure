class Appointment:
    def __init__(self, appointmentID, doctor, patient, date, time):
        self.appointmentID = appointmentID
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time
        self.status = "Scheduled"

    def showInfo(self):
        print("\n========== APPOINTMENT ==========")
        print(f"Appointment ID: {self.appointmentID}")
        print(f"Doctor: {self.doctor.name} {self.doctor.surname}")
        print(f"Patient: {self.patient.name} {self.patient.surname}")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Status: {self.status}")
        print("=================================")