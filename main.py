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