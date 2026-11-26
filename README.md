# Hospital Management System 🏥

## 📌 About the Project

Hospital Management System is a simple Python console-based application developed using Object-Oriented Programming (OOP).

The project allows users to manage doctors, patients, and appointments in a hospital.

## 🚀 Features

- Add new doctors
- Add new patients
- Display all doctors
- Display all patients
- Create appointments
- Display all appointments
- Automatically generate unique IDs
- Validate appointment date and time
- Handle invalid inputs using `try-except`

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Inheritance
- Encapsulation
- `super()` method
- Modules and Packages
- Exception Handling

## 📂 Project Structure

```text
HospitalManagement/
│
├── main.py
├── person.py
├── doctor.py
├── patient.py
├── hospital.py
└── appointment.py
```

## 📖 Class Description

### 1. Person
The parent class containing common attributes:

- Name
- Surname
- Age
- Phone

### 2. Doctor
Inherits from the Person class.

Additional attributes:

- Doctor ID
- Specialization
- Experience

### 3. Patient
Inherits from the Person class.

Additional attributes:

- Patient ID
- Blood Group
- Medical History

Encapsulation is demonstrated using public, protected, and private attributes.

### 4. Appointment
Manages appointment information:

- Appointment ID
- Doctor
- Patient
- Date
- Time
- Status

### 5. Hospital
Manages the hospital system, including doctors, patients, and appointments.

## 📋 Main Menu

```text
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
```

## ▶️ How to Run

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Open the project folder:

```bash
cd HospitalManagement
```

3. Run the application:

```bash
python main.py
```

## 🎯 Learning Objectives

This project was created to practice Python programming and understand the following concepts:

- Classes and Objects
- Inheritance
- Encapsulation
- Method Overriding
- `super()` Method
- Exception Handling
- Modular Programming

## 👨‍💻 Author

Created as a Python OOP practice project.
