class Bill:
	bills = []
	# issue a new bill with the provided data 
	def newBill(self,carName,period,price,):
			self.carName = carName
			self.period  = period
			self.price   = price 
			list = {
				'car' 	: carName ,
				'days'	: period ,
				'price'	: price
			}
			self.bills.append(list)

			return print('new bill have neen created')
	# list all the current bills 
	def listBills(self):
		
		i = 1 
		for bill in self.bills :
			print(str(i) + " - " + " a bill for " + bill['car'] + " total payment is " + str(bill['price']) )

      
