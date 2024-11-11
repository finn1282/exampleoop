from .InventoryModel import *
from .InventoryView import *

class InventoryController():
	
	def __init__(self):
		self.__inventoryModel = InventoryModel()
		self.__inventoryView = InventoryView()

	def outputProducts(self):

		products = self.__inventoryModel.productsGetter()
		productsList = []

		for i in products:
			productsList.append(vars(i))

		# print(productsList)

		self.__inventoryView.outputProducts(productsList)

	def addProduct(self, product):
		self.__inventoryModel.addProduct(product)