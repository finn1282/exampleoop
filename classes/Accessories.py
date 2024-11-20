#Class to store accessories, takes attributes from Product parent class

from .Product import *

class Accessories(Product): # extends Product
	
	def __init__(self, name, supplier, amount, minAmount, price, user, isChewable, color):
		super().__init__(name, supplier, amount, minAmount, price, user)
		self.isChewable = isChewable
		self.color = color


if __name__=='__main__':
	product = Accessories("cattoy", "mewmewsupplier", 30, 11, 20, "user2", True, "red")
	print(vars(product))