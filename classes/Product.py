class Product:

	def __init__(self, name, price, supplier, amount):
		self.__name = name
		self.__price = price
		self.__supplier = supplier
		self.__amount = amount

	def nameGetter(self):
		return self.__name

	def amountGetter(self):
		return self.__amount
	
	def amountSetter(self, amount):
		self.__amount = amount

	def amountReduce(self, amount):
		self.__amount -= amount	