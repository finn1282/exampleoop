from .Edibles import *
from .Accessories import *
from tabulate import tabulate

class Inventory:

	def findBy(self, attribute, attributeValue):
		productsList = self.convertToList(self.productsDict)
		outputList = []
		for i in productsList: 
			if(i[attribute]==attributeValue):
				outputList.append(i)
		return outputList
				
	def sortBy(self, attribute, order='ASC'):
		sortedStack = self.convertToList(self.productsDict)
		if(order=='ASC'):
			for i in range(1, len(sortedStack)):
				value = sortedStack[i][attribute]
				key = sortedStack[i]
				j=i-1
				while j>=0 and value<sortedStack[j][attribute]:
					sortedStack[j+1]=sortedStack[j]
					j-=1
				sortedStack[j+1] = key
		else:
			for i in range(1, len(sortedStack)):
				value = sortedStack[i][attribute]
				key = sortedStack[i]
				j=i-1
				while j>=0 and value>sortedStack[j][attribute]:
					sortedStack[j+1]=sortedStack[j]
					j-=1
				sortedStack[j+1] = key
		return sortedStack

	def lowStock(self):
		productsList = self.convertToList(self.productsDict)
		outputList = []
		for i in productsList:
			if i['amount']<i['minAmount']:
				outputList.append(i)
		return outputList

	def makeSales(self, name, amount):
		return self.productsDict[name].sellProduct(amount)

	def decreaseStock(self, name, amount):
		self.productsDict[name].reduceAmount(amount)

	def increaseStock(self, name, amount):
		self.productsDict[name].increaseAmount(amount)

	def removeProduct(self, name):
		self.productsDict.pop(name)

	def outputProductsList(self, products = None):
		if products==None:
			outputList = []
			for i in self.convertToList(self.productsDict):
				outputList.append(list(i.values()))
			print(tabulate(outputList, headers=["Product Name", "Price (RM)", "Supplier", "Amount", "Minimum Amount", "Sales", "Chewable", "Colour"], floatfmt=".2f"))
		else:
			outputList = []
			for i in products:
				outputList.append(list(i.values()))
			print(tabulate(outputList, headers=["Product Name", "Price (RM)", "Supplier", "Amount", "Minimum Amount", "Sales", "Chewable", "Colour"], floatfmt=".2f"))

	def convertToList(self, dict, user=False):
		productList=[]
		for i in list(dict.values()):
			productVar = eval(str(vars(i)))
			if(user==False):
				productVar.pop("user")
			productDict = {"productType": i.__class__.__name__}
			productDict.update(productVar)
			productList.append(productDict)
		return productList

	def addProduct(self, productType, name, supplier, amount, minAmount, price, sales, opt1, opt2):
		if productType == "Edibles":
			product = Edibles(name, supplier, amount, minAmount, price, sales, self.user, opt1, opt2)
		else:
			product = Accessories(name, supplier, amount, minAmount, price, sales, self.user, opt1, opt2)
		self.productsDict[name] = product

	def outputToFile(self):
		productsList = self.convertToList(self.productsDict, True)
		with open("database.txt", "a") as output:
			for prod in productsList:
				output.write(str(prod))
				output.write("\n")

	def inputFromFile(self, user):
		productList = []
		returnList = []

		with open("database.txt", "r") as database:
			database = database.readlines()
		
		for i, j in enumerate(database):
			if j == "":
				pass
			j = eval(j.replace("\n", ""))
			database[i] = j
			if(database[i]['user'] == user):
				productList.append(j)
			else: 
				returnList.append(j)

		with open("database.txt", "w") as output:
			for i in returnList:
				output.write(str(i))
				output.write("\n")	

		for product in productList:
			self.addProduct(product['productType'], product['name'], product['supplier'], product['amount'], product['minAmount'], product['price'], product['sales'], list(product.values())[-2], list(product.values())[-1])

	def __init__(self, user):

		self.user = user

		self.productsDict = dict()

		self.inputFromFile(user)


		


if __name__ == '__main__':
	inv = Inventory("u1")