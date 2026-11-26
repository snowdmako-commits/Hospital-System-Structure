from person import Person

class Patient(Person):
    def __init__(self, name, surname, age, phone, patientID, bloodGroup, medicalHistory):

        super().__init__(name, surname, age, phone)

        self.patientID = patientID
        self._bloodGroup = bloodGroup
        self.__medicalHistory = medicalHistory

    def showInfo(self):
        print(f"\nPatient ID: {self.patientID}")
        super().showInfo()
        print(f"Blood Group: {self._bloodGroup}")
        print(f"Medical History: {self.__medicalHistory}")

    def getMedicalHistory(self):
        return self.__medicalHistory

    def updateMedicalHistory(self, newHistory):
        self.__medicalHistory = newHistory
        print("Medical history updated successfully.")