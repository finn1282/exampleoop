#Products parent class, contains properties for all products: name, supplier, amount, minAmount, sales, price, user
#Has methods to sell product, increase and decrease amounts, and set minimum amount to determine low

class Product:

	def __init__(self, name, supplier, amount, minAmount, price, sales, user):
		self.name = name
		self.supplier = supplier
		self.amount = amount
		self.minAmount = minAmount
		self.price = price
		self.sales = sales
		self.user = user

	def sellProduct(self, amount):
		self.amount -= amount
		self.sales += amount
		return self.price*amount

	def increaseAmount(self, amount):
		self.amount+=amount

	def decreaseAmount(self, amount):
		self.amount-=amount

	def setMinAmount(self, amount):
		self.minAmount = amount
