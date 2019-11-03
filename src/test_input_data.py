#!/usr/bin/env python
import unittest
import input_data

class TestInputData(unittest.TestCase):
    def test_Input_Default_Values(self):
        x = input_data.InputData()
        self.assertEqual(x.nominal_power, 400, msg="Wrong nominal power/n")
        self.assertEqual(x.voltage, 230, msg="Wrong voltage value/n")
        self.assertEqual(x.frequency, 50, msg="Wrong frequency value/n")
        self.assertEqual(x.poles_number, 3, msg="Wrong poles number/n")
        self.assertEqual(x.synchronous_speed, 1000, msg="Wrong sychronous speed value/n")        

if __name__ == '__main__': 
    unittest.main() 
