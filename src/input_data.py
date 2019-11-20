import math


class InputData:
    def __init__(self):
        self.nominal_power = 200
        self.voltage = 230
        self.frequency = 50
        self.poles_number = 4
        self.synchronous_speed = 3000/self.poles_number
        self.efficiency = 0.8
        self.power_coef = 0.8
        self.slots = 2
        self.oklad_pradowy = 25000
        self.induction = 1
        self.wykorzystanie_podzialki_coef = 0.715
        self.wspolczynnik_smuklosci = 1.3

        check = input("Do you want to input your data? (y/n) \n")
        if check == 'y':
            temp = input("Enter nominal power value: \n")
            while str.isnumeric(temp) is False:
                temp = input("Wrong value!! Enter the numeric value: \n")
            self.nominal_power = int(temp)

            temp = input("Enter nominal voltage value: \n")
            while str.isnumeric(temp) is False:
                temp = input("Wrong value!! Enter the numeric value: \n")
            self.voltage = int(temp)

            temp = input("Enter frequency value: \n")
            while str.isnumeric(temp) is False:
                temp = input("Wrong value!! Enter the numeric value: \n")
            self.frequency = int(temp)

            temp = input("Enter poles number: \n")
            while str.isnumeric(temp) is False:
                temp = input("Wrong value!! Enter the numeric value: \n")
            self.poles_number = int(temp)
