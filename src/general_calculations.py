import input_data
import math


class Calculations(input_data.InputData):
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
        self.volume = self.inside_motor_power * 2 * math.sqrt(2) / (pow(math.pi, 3) * self.oklad_pradowy * self.induction * self.wykorzystanie_podzialki_coef * (self.synchronous_speed/60) * 0.96 )

    def motor_dimension_calculation(self):
        self.motor_dimension = pow((self.volume * 2 * math.sqrt(2) / (self.wspolczynnik_smuklosci * math.pi)),1/3)

    def pole_divider_calculation(self):
        self.pole_divider = self.motor_dimension * math.pi / (2*self.poles_number)

    def motor_lenth_calculation(self):
        self.motor_lenth = self.wspolczynnik_smuklosci*self.pole_divider


def general_calulations():
    x = Calculations()
    x.rotation_inducted_voltage_coefficient_calculation()
    x.rotation_inducted_voltage_calculation()
    x.electric_power_calculation()
    x.nominal_current_calculation()
    x.slots_number_calculation()
    x.electrical_angle_slots_voltage_calucation()
    x.group_coef_calculation()
    x.podzialka_biegunowa_calculation()
    x.inside_motor_power_calculation()
    x.motor_volume_calculation()
    x.motor_dimension_calculation()
    x.pole_divider_calculation()
    x.motor_lenth_calculation()
    print("\nWspolczynnik indukowanego napięcia rotacji = " + str(x.rotation_inducted_voltage_coefficient))
    print("\nNapiecie indukowane rotacji = " + str(x.rotation_inducted_voltage))
    print("\nMoc elektryczna maszyny = " + str(x.electric_power))
    print("\nPrad znamionowy  maszyny = " + str(x.nominal_current))
    print("\nMoc pozorna wewnetrzna maszyny = " + str(x.inside_motor_power))
    print("\nLiczba zlobkow stojana  = " + str(x.slots_number))
    print("\nKat elektryczny miedzy wektorami napiec zlobkowych = " + str(x.electrical_angle_slots_voltage))
    print("\nWspolczynnik grupy = " + str(x.group_coef))
    print("\nPoskok srednicowy uzwojenia = " + str(x.podzialka_biegunowa))
    print("\nPodzialka biegunowa = " + str(x.podzialka_biegunowa))
    print("\nWspolczynnik skrótu = " + '1')
    print("\nObjetosc obliczeniowa = " + str(x.volume))
    print("\nSrednica obliczeniowa maszyny = " + str(x.motor_dimension))
    print("\nPodzialka biegunowa maszyny = " + str(x.pole_divider))
    print("\nDlugosc obliczeniowa maszyny = " + str(x.motor_lenth))


general_calulations()
