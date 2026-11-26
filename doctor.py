from person import Person

class Doctor(Person):
    def __init__(self, name, surname, age, phone,doctorID, specialization, experience):

        super().__init__(name, surname, age, phone)

        self.doctorID = doctorID
        self.specialization = specialization
        self.experience = experience

    def showInfo(self):
        print(f"\nDoctor ID: {self.doctorID}")
        super().showInfo()
        print(f"Specialization: {self.specialization}")
        print(f"Experience: {self.experience} years")