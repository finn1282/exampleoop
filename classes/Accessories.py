from .Product import *

class Accessories(Product):
	
	def __init__(self, name, supplier, price, amount, sales, isChewable, color):
		super().__init__(name, supplier, price, amount, sales)
		self.isChewable = isChewable
		self.color = color