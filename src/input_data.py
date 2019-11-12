import math

class InputData:
    def __init__(self):
        self.nominal_power = 400
        self.voltage = 230
        self.frequency = 50
        self.poles_number = 3
        self.synchronous_speed = 1000
        self.efficiency = 0.8
        self.power_coef = 0.8
        self.slots = 2

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

            temp = input("Enter synchronous speed value \n")
            while str.isnumeric(temp) is False:
                temp = input("Wrong value!! Enter the numeric value: \n")
            self.synchronous_speed = int(temp)
    
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
    