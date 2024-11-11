from .Product import *

class Food(Product):
	def __init__(self, name, price, supplier, amount, expiry):
		super().__init__(name, price, supplier, amount)
		self.__expiry = expiry

	def getName(self):
		return self.__expiry

if __name__ == "__main__":
	print("ok")
	food = Food("new", 23, "yete", 10, 123)
	print(food.getName())