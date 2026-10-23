class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount #initially same as getter function, but discounts will be applied here


class SeniorP(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        original_bill = self.get_bill_amount()
        return original_bill * 0.8


class PhilHealthP(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)


    def calculate_bill(self):
        original_bill = self.get_bill_amount()
        return original_bill * 0.85  


regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorP("Maria Santos", 15000)
philhealth_patient = PhilHealthP("Pedro Reyes", 15000)

patients = [regular_patient, senior_patient, philhealth_patient]

# print sequence

print("Hospital Billing System")
print("-----------------------")
for patient in patients:
    print(f"Patient Name:  {patient.get_name()}")
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}") # to make it 2 decimals
    print(f"Final Bill:    ₱{patient.calculate_bill():,.2f}\n")
