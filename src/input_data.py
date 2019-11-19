import math

class InputData:
    def __init__(self):
        self.nominal_power = 400
        self.voltage = 230
        self.frequency = 50
        self.poles_number = 3
        self.synchronous_speed = 3000/self.poles_number
        self.efficiency = 0.8
        self.power_coef = 0.8
        self.slots = 2
        self.oklad_pradowy = 25000
        self.induction = 0.9
        self.wykorzystanie_podzialki_coef = 0.715
        self.wspolczynnik_smuklosci = 1.3

        check = input("Do you want to input your data? (y/n) \n")
        if check == 'y':
            temp = input("Enter nominal power value: \n")
            while  str.isnumeric(temp) is False:
                temp = input("Wrong value!! Enter the numeric value: \n")
            self.nominal_power = int(temp)

            temp = input("Enter nominal voltage value: \n")
            while  str.isnumeric(temp) is False:
                temp = input("Wrong value!! Enter the numeric value: \n")
            self.voltage = int(temp)

            temp = input("Enter frequency value: \n")
            while  str.isnumeric(temp) is False:
                temp = input("Wrong value!! Enter the numeric value: \n")
            self.frequency = int(temp)
            
            temp = input("Enter poles number: \n")
            while  str.isnumeric(temp) is False:
                temp = input("Wrong value!! Enter the numeric value: \n")
            self.poles_number = int(temp)
    
    def rotation_inducted_voltage_coefficient_calculation(self):
        self.rotation_inducted_voltage_coefficient = 0.985-0.005*self.poles_number

    def rotation_inducted_voltage_calculation(self):
        self.rotation_inducted_voltage = self.rotation_inducted_voltage_coefficient*self.voltage
    
    def electric_power_calculation(self):
        self.electric_power = self.nominal_power/self.efficiency

    def nominal_current_calculation(self):
        self.nominal_current = self.electric_power/(3*self.voltage*self.power_coef)

    def inside_motor_power_calculation(self):
        self.inside_motor_power = 3*self.nominal_current*self.rotation_inducted_voltage

    def slots_number_calculation(self):
        self.slots_number = 2*self.slots*self.poles_number*3
        
    def electrical_angle_slots_voltage_calucation(self):
        self.electrical_angle_slots_voltage = 2*math.pi*self.poles_number/self.slots_number

    def group_coef_calculation(self):
        self.group_coef = math.sin(self.slots_number*self.electrical_angle_slots_voltage/2)/(self.slots_number*math.sin(self.electrical_angle_slots_voltage/2))
    
    def podzialka_biegunowa_calculation(self):
        self.podzialka_biegunowa = self.slots_number / (2*self.poles_number)
    
    def motor_volume_calculation(self):
        self.volume =  self.inside_motor_power * 2 * math.sqrt(2) / (pow(math.pi, 3) * self.oklad_pradowy * self.induction * self.wykorzystanie_podzialki_coef * (self.synchronous_speed/60) * 0.96 )
 
    def motor_dimension_calculation(self):
        self.motor_dimension = pow((self.volume * 2 * math.sqrt(2) / (self.wspolczynnik_smuklosci * math.pi)),1/3)

    def motor_lenth_calculation(self):
        self.motor_lenth = 10