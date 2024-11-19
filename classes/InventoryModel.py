class InventoryModel:

	def __init__(self):
		self.productsStack = []

	def addProduct(self, product):
		newProduct = vars(product)
		productType = {"productType": product.__class__.__name__}
		productType.update(newProduct)
		self.productsStack.append(productType)

	def removeProduct(self, productName):
		for i in self.productsStack:
			if i['name'] == productName:
				self.productsStack.remove(i)

	def sellProduct(self, productName, amount):
		product = self.findBy("name", productName)
		product = product[0]
		product['sales']+=amount

	def findLowStock(self):
		lowStock = []
		for i in self.productsStack:
			amount = i['amount']
			minAmount = i['minAmount']
			if amount<minAmount:
				lowStock.append(i)
		return lowStock

	def findBy(self, attribute, attributeValue):
		search = []
		for i in self.productsStack:
			if(i[attribute] == attributeValue):
				search.append(i)
		return search

	def sortBy(self, attribute, order):
		if(order=='ASC'):
			sortedStack = self.productsStack
			for i in range(1, len(sortedStack)):
				value = sortedStack[i][attribute]
				key = sortedStack[i]
				j=i-1
				while j>=0 and value<sortedStack[j]['price']:
					sortedStack[j+1]=sortedStack[j]
					j-=1
				sortedStack[j+1] = key
			return sortedStack
		else:
			sortedStack = self.productsStack
			for i in range(1, len(sortedStack)):
				value = sortedStack[i][attribute]
				key = sortedStack[i]
				j=i-1
				while j>=0 and value>sortedStack[j]['price']:
					sortedStack[j+1]=sortedStack[j]
					j-=1
				sortedStack[j+1] = key
			return sortedStack
		
	def addStock(self, productName, amount):
		product = self.findBy("name", productName)	
		product['amount'] += amount

	def removeStock(self, productName, amount):
		product = self.findBy("name", productName)	
		product['amount'] -= amount