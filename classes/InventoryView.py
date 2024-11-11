class InventoryView():

	# def __init__(self):

	def outputProducts(self, productList):
		for i in productList:
			for j in i.values():
				print(j, end=" ")
			print("")