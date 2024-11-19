from classes.InventoryController import *

if __name__ == '__main__':

	inventory = InventoryController()

	inventory.inputFromFile()
	inventory.outputInventory(inventory.sortBy('price', 'DESC'))
	inventory.outputInventory(inventory.findBy('supplier', 'mewmew'))

	print("test")