from .Edibles import *
from .Accessories import *
from tabulate import tabulate

class Inventory:

	#initialize inventory object
	def __init__(self, user):
		self.user = user
		#create empty dictionary
		self.productsDict = dict()
		#loads user data from file
		self.inputFromFile(user)
	
	#reads user data from file and saves to dictionary
	def inputFromFile(self, user):
		productList = []
		returnList = []

		#reads all lines in database
		with open("database.txt", "r") as database:
			database = database.readlines()
		
		#checks if user is current user then saves to productList, if not then saves to returnList
		for i, j in enumerate(database):
			if j == "":
				pass
			j = eval(j.replace("\n", ""))
			database[i] = j
			if(database[i]['user'].lower() == user.lower()):
				productList.append(j)
			else: 
				returnList.append(j)

		#writes returnList back to database file
		with open("database.txt", "w") as output:
			for i in returnList:
				output.write(str(i))
				output.write("\n")	

		#from productList creates product objects and saves into product dictionary
		for product in productList:
			self.addProduct(product['productType'], product['name'], product['supplier'], product['amount'], product['minAmount'], product['price'], product['sales'], list(product.values())[-2], list(product.values())[-1])

	#outputs current product dictionary to file
	def outputToFile(self):
		#converts product objects into json
		productsList = self.convertToList(self.productsDict, True)
		#writes each object data out to database file
		with open("database.txt", "a") as output:
			for prod in productsList:
				output.write(str(prod))
				output.write("\n")

	#converts object dictionary into list of json data
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
	
	#creates product objects and adds to product dictionary
	def addProduct(self, productType, name, supplier, amount, minAmount, price, sales, opt1, opt2):
		if productType == "Edibles":
			product = Edibles(name, supplier, amount, minAmount, price, sales, self.user, opt1, opt2)
		else:
			product = Accessories(name, supplier, amount, minAmount, price, sales, self.user, opt1, opt2)
		self.productsDict[name] = product
	
	def removeProduct(self, name):
		self.productsDict.pop(name)
	
	def increaseStock(self, name, amount):
		self.productsDict[name].increaseAmount(amount)

	def decreaseStock(self, name, amount):
		self.productsDict[name].reduceAmount(amount)

	def makeSales(self, name, amount):
		return self.productsDict[name].sellProduct(amount)
	
	def lowStock(self):
		productsList = self.convertToList(self.productsDict)
		outputList = []
		for i in productsList:
			if i['amount']<i['minAmount']:
				outputList.append(i)
		return outputList

	#linear sort to find the value in an attribute that matches input
	def findBy(self, attribute, attributeValue):
		productsList = self.convertToList(self.productsDict)
		outputList = []
		for i in productsList:
			if attribute=='petType' and i['productType']=="Accessories":
				continue
			if(i[attribute].lower()==attributeValue.lower()):
				outputList.append(i)
		return outputList
				
	#insertion sort to sort through a specific attribute, can be ascending or descending order
	def sortBy(self, attribute, order='ASC'):
		sortedStack = self.convertToList(self.productsDict)
		#sort by ascending order
		if(order=='ASC'):
			for i in range(1, len(sortedStack)):
				value = sortedStack[i][attribute]
				key = sortedStack[i]
				j=i-1
				while j>=0 and value<sortedStack[j][attribute]:
					sortedStack[j+1]=sortedStack[j]
					j-=1
				sortedStack[j+1] = key
		#sort by descending order
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

	#displays product list, can take in specific lists
	def outputProductsList(self, products = None):
		productsList = self.convertToList(self.productsDict) if products==None else products
		outputList_a = []
		outputList_e = []

		for i in productsList:
			temp_list = list(i.values())
			temp_list.pop(0)
			if(i['productType']=='Accessories'):
				outputList_a.append(temp_list)
			else:
				outputList_e.append(temp_list)
		if(len(outputList_a)>0):
			print("Accessories:")
			print(tabulate(outputList_a, headers=["Product Name", "Supplier", "Amount", "Minimum Amount", "Price (RM)", "Sales", "Chewable", "Colour"], floatfmt=".2f"))
		if(len(outputList_e)>0):
			print("Edibles:")
			print(tabulate(outputList_e, headers=["Product Name", "Supplier", "Amount", "Minimum Amount", "Price (RM)", "Sales", "Expiry Date", "Animal"], floatfmt=".2f"))