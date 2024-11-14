from .Product import *

class Edibles(Product):
	
	def __init__(self, name, supplier, price, amount, sales, expiry, petType):
		super().__init__(name, supplier, price, amount, sales)
		self.expiry = expiry
		self.petType = petType