import json
from classes.Edibles import *
from classes.Accessories import *
from .InventoryModel import *
from .InventoryView import *

class InventoryController():

	def __init__(self):
		self.inventoryModel = InventoryModel()
		self.inventoryView = InventoryView()

	def addProduct(self, productType, name, supplier, price, amount, minAmount, sales, opt1, opt2):
		if(productType == "Edibles"):
			product = Edibles(name, supplier, price, amount, minAmount, sales, opt1, opt2)
		elif(productType == "Accessories"):
			product = Accessories(name, supplier, price, amount, minAmount, sales, opt1, opt2)
		else:
			return -1
		self.inventoryModel.addProduct(product)

	def removeProduct(self, productName):
		self.inventoryModel.removeProduct(productName)

	def sellProduct(self, productName, amount):
		self.inventoryModel.sellProduct(productName, amount)

	def findLowStock(self):
		lowStock = self.inventoryModel.findLowStock()
		self.inventoryView.outputInventory(lowStock)

	def findBy(self, attribute, attributeValue):
		return self.inventoryModel.findBy(attribute, attributeValue)

	def sortBy(self, attribute, order="ASC"):
		return self.inventoryModel.sortBy(attribute, order)
	
	def addStock(self, productName, amount):
		self.inventoryModel.addStock(productName, amount)
	
	def removeStock(self, productName, amount):
		self.inventoryModel.removeStock(productName, amount)

	def inputFromFile(self, file="data.txt"):
		with open(file, "r") as dataIn:
			data = dataIn.read()
		data = json.loads(data)
		for i in data:
			if(i['productType'] == "Edibles"):
				i['opt1'] = i.pop('expiry')
				i['opt2'] = i.pop('petType')
			else:
				i['opt1'] = i.pop('isChewable')
				i['opt2'] = i.pop('color')
			self.addProduct(**i)

	def outputToFile(self, file="data.txt", inventory=None):
		if(inventory==None):
			inventory=self.inventoryModel.productsStack
		with open(file, "w") as out:
			json.dump(self.inventoryModel.productsStack, out)

	def outputInventory(self, inventory=None):
		if(inventory==None):
			inventory=self.inventoryModel.productsStack
		self.inventoryView.outputInventory(inventory)