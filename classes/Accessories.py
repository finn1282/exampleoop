#Class to store accessories, takes attributes from Product parent class

from .Product import *

class Accessories(Product): # extends Product
	
	def __init__(self, name, supplier, amount, minAmount, price, sales, user, isChewable, color):
		super().__init__(name, supplier, amount, minAmount, price, sales, user)
		self.isChewable = isChewable
		self.color = color
