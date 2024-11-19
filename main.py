from classes.InventoryController import *

if __name__ == '__main__':

	inventory = InventoryController()

	inventory.inputFromFile()
	inventory.outputInventory()