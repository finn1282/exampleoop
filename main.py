from classes.Food import *
from classes.InventoryController import *
from classes.InventoryModel import *
from classes.InventoryView import *


if __name__ == '__main__':
	product1 = Product("food", 10, "producer a", 5)
	food1 = Food("yum", 25, "BAnks", 20, 2020)
	inventoryController = InventoryController()
	inventoryController.addProduct(product1)
	inventoryController.addProduct(food1)

	inventoryController.outputProducts()
	