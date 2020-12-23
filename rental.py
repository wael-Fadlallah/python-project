from customer import Customer

class Rental:
  # the stock list
  stock = []

  # add 10 cars to the stock when creating the object
  def __init__(self):
    self.stock.append(['hatchback',4])
    self.stock.append(['sedan',3])
    self.stock.append(['SUV',3])
    # print(self.stock)
  
  def ShowStock(self):
    print( 'Available cars : \n ' )
    i = 1 
    for x in self.stock :
      if x[1] != 0 :  
        print ('\t'+  str(i) + ' - ' + str(x[0]) + ' : ' +str( x[1]) + ' in stock ')
        i = i + 1 

  def RentCar(self,types_rates):
    i = 1 
    for x in self.stock :
      print ('\t'+  str(i) + ' - ' +x[0])
      i = i + 1 
    print(' what car you want to rent : \t ')
    # get car index 
    carIndex = int(input('')) - 1
    
    car = self.stock[carIndex]
    # subtract the car from stock qty 
    car[1] = car[1] - 1
    
    print("How many days you want rent a " + car[0]+ " for :  " )
    days = int(input(''))
    # if the days is less than 0 don't expect the input
    while days <= 0 :
      print("invalid value for days input a number that greater than 0 : ")  
      days = int(input(''))
    # get the rate from the number of days 
    if days < 7 :
      if car[0] == 'hatchback':
        price = 30 
      elif car[0] == 'sedan':
        price = 50 
      else:
        price = 100
    else :
      if car[0] == 'hatchback':
        price = types_rates['hatchback']
      elif car[0] == 'sedan':
        price = types_rates['sedan']
      else:
        price = types_rates['SUV']
    # print the order and calcate price  
    print( " You have rented a " + car[0] + " for " + str(days) + " you will be charged " + str(price) + " per day we hope you enjoy our service " )
    price = price * days
    
    # bill info to return it
    car_data = {
      'name':car[0],
      'num_of_days':days,
      'price': price
      }
    # show stock
    self.ShowStock()
    return car_data





    



