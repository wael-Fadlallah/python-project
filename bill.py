class Bill:
	bills = []
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

			return print(self.bills)

	def listBills(self):
		
		i = 0 
		for bill in self.bills :
			print(str(i) + " - " + " a bill for " + bill['car'] + " total payment is " + str(bill['price']) )

      
