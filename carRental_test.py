from unittest.mock import patch
from unittest import TestCase

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
        # create a result to test it 
        result = agent.RentCar({'hatchback':25,'sedan':40,'SUV':90})

        self.assertEqual(result,{
        'name':'hatchback',
        'num_of_days':-5,
        'price':1050
        })