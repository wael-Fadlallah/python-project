from unittest.mock import patch
from unittest import TestCase

# import unittest 

from main import *

class TestCarRental(TestCase):
    def test_carRental(self):
        # test if a new bill is created 
        self.assertEqual(bill.newBill("wael",10,100),True)
        # test if a new bill is created
        self.assertIsNone(customer.ReturnCar(agent,bill))
        # 
    
    # test input for rent a car 
    @patch('main.input', return_value=['1', '42'])
    def test_rent_a_car(self,input):
        # mocked_input.side_effect = 
        result = agent.RentCar()

        self.assertEqual(result,{
        'name':'hatchback',
        'num_of_days':42,
        'price':1050
        })