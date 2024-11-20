#Class to store edible foods, takes attributes from Product parent class

from .Product import *

class Edibles(Product): #extends Product class
	
	def __init__(self, name, supplier, amount, minAmount, price, user, expiryDate, petType):
		super().__init__(name, supplier, amount, minAmount, price, user)
		self.expiryDate = expiryDate
		self.petType = petType
