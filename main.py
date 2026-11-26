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