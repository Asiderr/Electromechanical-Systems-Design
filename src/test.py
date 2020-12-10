#!/usr/bin/env python
import calculations
import input_data
import unittest
import math


class TestInputData(unittest.TestCase):
    def test_Input_Default_Values(self):
        x = input_data.InputData()
        self.assertEqual(x.nominal_power, 400, msg="Wrong nominal power\n")
        self.assertEqual(x.voltage, 230, msg="Wrong voltage value\n")
        self.assertEqual(x.frequency, 50, msg="Wrong frequency value\n")
        self.assertEqual(x.poles_number, 3, msg="Wrong poles number\n")
        self.assertEqual(x.synchronous_speed, 1000, msg="Wrong sychronous speed value\n")        
        self.assertEqual(x.efficiency, 0.8, msg="Wrong efficency value\n")
        self.assertEqual(x.power_coef, 0.8, msg="Wrong power coefficent\n")
        self.assertEqual(x.power_coef, 0.8, msg="Wrong power coefficent\n")


"""
    def test_Input_not_default(self):
        x = input_data.InputData()
        self.assertEqual(x.nominal_power, 10, msg="Wrong nominal power/n")
        self.assertEqual(x.voltage, 10, msg="Wrong voltage value/n")
        self.assertEqual(x.frequency, 10, msg="Wrong frequency value/n")
        self.assertEqual(x.poles_number, 10, msg="Wrong poles number/n")
        self.assertEqual(x.synchronous_speed, 10, msg="Wrong sychronous speed value/n")
"""


class TestCalculations(unittest.TestCase):
    def test_rotation_inducted_voltage_coefficient_calculation(self):
        x = calculations.Calculations()
        x.rotation_inducted_voltage_coefficient_calculation()
        self.assertEqual(x.rotation_inducted_voltage_coefficient, 0.970, msg="Wrong rotation inducted voltage coefficient\n")

    def test_rotation_inducted_voltage_calculation(self):
        x = calculations.Calculations()
        x.rotation_inducted_voltage_coefficient_calculation()
        x.rotation_inducted_voltage_calculation()
        self.assertEqual(x.rotation_inducted_voltage, 223.1, msg="Wrong rotation inducted voltage \n")

    def test_electric_power_calculation(self):
        x = calculations.Calculations()
        x.electric_power_calculation()
        self.assertEqual(x.electric_power, 500, msg="Wrong electric power \n")

    def test_nominal_current_calculation(self):
        x = calculations.Calculations()
        x.electric_power_calculation()
        x.nominal_current_calculation()
        self.assertEqual(x.nominal_current, 500/(3*230*0.8), msg="Wrong nominal current \n")        

    def test_inside_motor_power_calculation(self):
        x = calculations.Calculations()
        x.rotation_inducted_voltage_coefficient_calculation()
        x.rotation_inducted_voltage_calculation()
        x.electric_power_calculation()
        x.nominal_current_calculation()
        x.inside_motor_power_calculation()
        self.assertEqual(x.inside_motor_power, 3*x.rotation_inducted_voltage*x.nominal_current)

    def test_slot_number_calculation(self):
        x = calculations.Calculations()
        x.slots_number_calculation()
        self.assertEqual(x.slots_number, 2*x.slots*x.poles_number*3)

    def test_electrical_angle_slots_voltage_calucation(self):
        x = calculations.Calculations()
        x.slots_number_calculation()
        x.electrical_angle_slots_voltage_calucation()
        self.assertEqual(x.electrical_angle_slots_voltage, 2*calculations.math.pi*x.poles_number/x.slots_number)

    def test_group_coef_calculation(self):
        x = calculations.Calculations()
        x.slots_number_calculation()
        x.electrical_angle_slots_voltage_calucation()
        x.group_coef_calculation()
        self.assertEqual(x.group_coef, calculations.math.sin((x.slots_number*x.electrical_angle_slots_voltage/2))/(x.slots_number*calculations.math.sin(x.electrical_angle_slots_voltage/2)))

    def test_podzialka_biegunowa_calculation(self):
        x = calculations.Calculations()
        x.slots_number_calculation()
        x.podzialka_biegunowa_calculation()
        self.assertEqual(x.podzialka_biegunowa, x.slots_number/(2*x.poles_number))

    def test_motor_volume_calculation(self):
        x = calculations.Calculations()
        x.rotation_inducted_voltage_coefficient_calculation()
        x.rotation_inducted_voltage_calculation()
        x.electric_power_calculation()
        x.nominal_current_calculation()
        x.inside_motor_power_calculation()
        x.motor_volume_calculation()
        self.assertEqual(x.volume, (x.inside_motor_power * 2 * math.sqrt(2)) / (pow(math.pi, 3) * x.oklad_pradowy * x.induction * x.wykorzystanie_podzialki_coef * (x.synchronous_speed/60) * 0.96))

    def test_motor_dimension_calculation(self):
        x = calculations.Calculations()
        x.rotation_inducted_voltage_coefficient_calculation()
        x.rotation_inducted_voltage_calculation()
        x.electric_power_calculation()
        x.nominal_current_calculation()
        x.inside_motor_power_calculation()
        x.motor_volume_calculation()
        x.motor_dimension_calculation()
        self.assertEqual(x.motor_dimension, pow((x.volume * 2 * math.sqrt(2))/(x.wspolczynnik_smuklosci * math.pi),1/3))

    def test_pole_divider_calculation(self):
        x = calculations.Calculations()
        x.rotation_inducted_voltage_coefficient_calculation()
        x.rotation_inducted_voltage_calculation()
        x.electric_power_calculation()
        x.nominal_current_calculation()
        x.inside_motor_power_calculation()
        x.motor_volume_calculation()
        x.motor_dimension_calculation()
        x.pole_divider_calculation()
        self.assertEqual(x.pole_divider, x.motor_dimension * math.pi/(2 * x.poles_number))

    def test_motor_lenth_calculation(self):
        x = calculations.Calculations()
        x.rotation_inducted_voltage_coefficient_calculation()
        x.rotation_inducted_voltage_calculation()
        x.electric_power_calculation()
        x.nominal_current_calculation()
        x.inside_motor_power_calculation()
        x.motor_volume_calculation()
        x.motor_dimension_calculation()
        x.pole_divider_calculation()
        x.motor_lenth_calculation()
        self.assertEqual(x.motor_lenth, x.wspolczynnik_smuklosci*x.pole_divider)


if __name__ == '__main__':
    unittest.main()
