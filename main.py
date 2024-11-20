from classes.Inventory import *

if __name__=='__main__':
	inventory = Inventory("user1")
	lowStock = inventory.sortBy("amount")
	inventory.outputProductsList(lowStock)
	inventory.outputToFile()