from doctor import Doctor
from patient import Patient
from hospital import Hospital

hospital = Hospital("City Hospital")

def getInt(message):
    while True:
        try:
            value = int(input(message))

            if value < 0:
                print("Please enter a positive number!")
                continue

            return value

        except ValueError:
            print("Please enter a valid number!")


def getText(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Field cannot be empty!")

def addDoctor():
    try:
        print("\n========== ADD DOCTOR ==========")

        name = getText("Name: ")
        surname = getText("Surname: ")
        age = getInt("Age: ")

        if age == 0:
            print("Age must be greater than zero!")
            return

        phone = getText("Phone: ")
        specialization = getText("Specialization: ")
        experience = getInt("Experience: ")

        doctorID = max([d.doctorID for d in hospital.doctors],default=0) + 1

        doctor = Doctor(name,surname,age,phone,doctorID,specialization,experience)

        hospital.addDoctor(doctor)

    except Exception as e:
        print("Error:", e)


def addPatient():
    try:
        print("\n========== ADD PATIENT ==========")

        name = getText("Name: ")
        surname = getText("Surname: ")
        age = getInt("Age: ")

        if age == 0:
            print("Age must be greater than zero!")
            return

        phone = getText("Phone: ")
        bloodGroup = getText("Blood Group: ")
        medicalHistory = getText("Medical History: ")

        patientID = max([p.patientID for p in hospital.patients],default=0) + 1

        patient = Patient(name,surname,age,phone,patientID,bloodGroup,medicalHistory)

        hospital.addPatient(patient)

    except Exception as e:
        print("Error:", e)

def createAppointment():
    try:
        print("\n========== CREATE APPOINTMENT ==========")

        if not hospital.doctors:
            print("Please add a doctor first!")
            return

        if not hospital.patients:
            print("Please add a patient first!")
            return

        hospital.showDoctors()
        doctorID = getInt("\nEnter Doctor ID: ")
        hospital.showPatients()
        patientID = getInt("\nEnter Patient ID: ")
        date = getText("Date (YYYY-MM-DD): ")
        time = getText("Time (HH:MM): ")

        hospital.createAppointment(doctorID,patientID,date,time)

    except Exception as e:
        print("Error:", e)

def main():
    while True:
        try:
            print("""
====================================
       HOSPITAL MANAGEMENT SYSTEM
====================================

1. Add Doctor
2. Add Patient
3. Show All Doctors
4. Show All Patients
5. Create Appointment
6. Show All Appointments
0. Exit

====================================
""")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                addDoctor()

            elif choice == "2":
                addPatient()

            elif choice == "3":
                hospital.showDoctors()

            elif choice == "4":
                hospital.showPatients()

            elif choice == "5":
                createAppointment()

            elif choice == "6":
                hospital.showAppointments()

            elif choice == "0":
                print("\nThank you for using Hospital Management System!")
                break

            else:
                print("\nInvalid choice! Please try again.")

        except Exception as e:
            print("Unexpected error:", e)

main()