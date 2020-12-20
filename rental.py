from customer import Customer

class Rental:
  types = ['hatchback','sedan','SUV']
  CarType = types[0]
  stock = []

  def __init__(self):
    self.stock.append(['hatchback',4])
    self.stock.append(['sedan',3])
    self.stock.append(['SUV',3])
    print(self.stock)

  def ShowStock(self):
    print( 'Available cars : \n ' )
    i = 1 
    for x in self.stock :
      if x[1] != 0 :  
        print ('\t'+  str(i) + ' - ' + str(x[0]) + ' : ' +str( x[1]) + ' in stock ')
        i = i + 1 

  def RentCar(self):
    i = 1 
    for x in self.stock :
      print ('\t'+  str(i) + ' - ' +x[0])
      i = i + 1 
    print(' what car you want to rent : \t ')
    carIndex = int(input('')) - 1
    
    car = self.stock[carIndex]
    # return print(car) 

    car[1] = car[1] - 1
    print("How many days you want rent a " + car[0]+ " for :  " )
    days = int(input(''))

    if days < 7 :
      if car[0] == 'hatchback':
        price = 30 
      elif car[0] == 'sedan':
        price = 50 
      else:
        price = 100
    else :
      if car[0] == 'hatchback':
        price = 25
      elif car[0] == 'sedan':
        price = 50
      else:
        price = 100

    print( " You have rented a " + car[0] + " for " + str(days) + " you will be charged " + str(price) + " per day we hope you enjoy our service " )
    price = price * days

    car_data = {
      'name':car[0],
      'num_of_days':days,
      'price': price
      }

    self.ShowStock()
    return car_data





    



