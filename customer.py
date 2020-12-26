class Customer:
	# empty list for rented cars
	rentedCars = []
	isVip = False

	# car types rates
	types_rates = {'hatchback':25,'sedan':40,'SUV':90}
	# call rent method from the rental class
	def Rent(self,rental):
		self.rentedCars.append(rental.RentCar(self.types_rates,self.isVip))
	
	# return a car to the stock 
	# return true if success 
	def ReturnCar(self,obj,bill):
		# if there is no cars to return print a message 
		if self.rentedCars == []:
			return print("you dose not have any rented cars")

		print("what car do you want to return : ")

		# print rented cars list 
		i = 1
		for car in self.rentedCars :
			print(str(i) + " - " + str(car['name']))
			i += 1

		index = int(input('')) - 1
		# check if the input is a car index and if not print a message 
		i -= 1
		if index >= i :
			print(" car not found try again ")
			index = int(input('')) - 1

		car = self.rentedCars[index]
		# check if the car type is in stock , if true incress stock number be 1 if not add the car type 
		alreadyInStock = False
		for stockCar in obj.stock :
			if stockCar[0] == car['name'] :
				stockCar[1] += 1
				alreadyInStock = True

		if alreadyInStock == False :
			stock = [ car['name'] ,1]
			obj.stock.append(stock)
	
		self.rentedCars.pop(index)
		
		# issue a bill
		bill.newBill(car['name'],car['num_of_days'],car['price'])
		obj.ShowStock()
		return True 

	# print all rented cars 
	def RentedCars(self):
		# if there is no rented cars print a message alse print a cars list
		if self.rentedCars == []:
			return print("you dose not have any rented cars")
		for car in self.rentedCars :
			print("-",car['name'],'rented for',car['num_of_days'],'days')


# create a VIP class the extend customer and override the types_rates list 
class VIP(Customer):
	# car types rates
	types_rates = {'hatchback':20,'sedan':35,'SUV':80}
	isVip = True