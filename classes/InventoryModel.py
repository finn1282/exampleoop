class InventoryModel:

	def __init__(self):
		self.__size = 0
		self.__products = []

	def addProduct(self, product):
		self.__products.append(product)

	def removeProduct(self, product):
		product.amountReduce(1)

	def productsGetter(self):
		return self.__products