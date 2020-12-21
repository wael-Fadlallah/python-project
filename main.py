from rental import Rental
from customer import Customer
from bill import Bill

def main() :

# initat the objects
  agent     = Rental()
  customer  = Customer()
  bill      = Bill()

# inifity loop that request user to input an option
  while True:
    operation = input('''
    Select operation:
    [1] View available cars
    [2] Rent a Car
    [3] Display rented cars
    [4] Return a car
    [5] Show Bills
    [6] Exit programm
		''')

# check the option 
    if operation == '1':
      agent.ShowStock()

    if operation == '2':
      customer.Rent(agent)

    if operation == '3':
      customer.RentedCars()

    if operation == '4':
      customer.ReturnCar(agent,bill)

    if operation == '5':
      bill.listBills()

    if operation == '6':
      print ("exiting ")
      break

main()

