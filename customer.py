class Customer:
	# car_data = {
    #   'name':'hatchback',
    #   'num_of_days':10,
	#   'price':150
    #   }
	rentedCars = []

	def Rent(self,car):
		self.rentedCars.append(car.RentCar())

	def ReturnCar(self,obj,bill):
		if self.rentedCars == []:
			return print("you dose not have any rented cars")

		print("what car do you want to return : ")

		i = 1
		for car in self.rentedCars :
			print(str(i) + " - " + str(car['name']))
			i += 1

		index = int(input('')) - 1
		i -= 1
		if index >= i :
			print(" car not found try again ")
			index = int(input('')) - 1

		car = self.rentedCars[index]

		alreadyInStock = False
		for stockCar in obj.stock :
			if stockCar[0] == car['name'] :
				stockCar[1] += 1
				alreadyInStock = True

		if alreadyInStock == False :
			stock = [ car['name'] ,1]
			obj.stock.append(stock)
	
		self.rentedCars.pop(index)
		
		bill.newBill(car['name'],car['num_of_days'],car['price'])
		obj.ShowStock()

	def RentedCars(self):
		if self.rentedCars == []:
			return print("you dose not have any rented cars")
		for car in self.rentedCars :
			print("-",car['name'],'rented for',car['num_of_days'],'days')

