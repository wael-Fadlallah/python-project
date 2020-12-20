# from car import Car

class Customer:
	car_data = {
      'name':'hatchback',
      'num_of_days':10
      }
	rentedCars = [car_data]

	def Rent(self,car):
		self.rentedCars.append(car.RentCar())

	def ReturnCar(self,obj):
		if self.rentedCars == []:
			return print("you dose not have any rented cars")

		print("what car do you want to return : ")

		i = 1
		for car in self.rentedCars :
			print(str(i) + " - " + str(car['name']))
			i += 1

		index = int(input('')) - 1
		carName = self.rentedCars[index]['name']

		alreadyInStock = False
		for stockCar in obj.stock :
			if stockCar[0] == carName :
				stockCar[1] += 1
				alreadyInStock = True

		if alreadyInStock == False :
			stock = [ carName ,1]
			obj.stock.append(stock)
	
		self.rentedCars.pop(index)
		
		obj.ShowStock()

	def RentedCars(self):
		if self.rentedCars == []:
			return print("you dose not have any rented cars")
		print(self.rentedCars)