from car import Car
from customer import Customer

class Rental:
  pass

class Bill:
  pass

class Stock:
  pass

def main() :

  car = Car()
  customer = Customer()

  while True:
    operation = input('''
    Select operation:
    [1] View available cars
    [2] Rent a Car
    [3] Display rented cars
    [4] Return a car
    [6] Exit programm
		''')

    if operation == '1':
      car.ShowStock()

    if operation == '2':
      customer.Rent(car)

    if operation == '3':
      customer.RentedCars()

    if operation == '4':
      customer.ReturnCar(car)

    if operation == '6':
      print ("exiting ")
      break

main()

