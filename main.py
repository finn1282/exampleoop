from classes.Inventory import * 
from classes.Report import *

def getInput(inputValues, display, type="str"):
    if(type=="str"):
        while True:
            userInput = input(display).lower()
            for i in inputValues:
                if userInput == i.lower():
                    return i
            print("Input not recognised, please input a valid selection.")
    else:
        while True:
            try: 
                userInput = int(input(display))
                if(userInput<0): 
                    raise Exception
                return userInput
            except: 
                print("Please enter a valid positive integer amount.")

if __name__=='__main__':
    print("Welcome to the Inventory Management System!")
    user = input("Please input your username: ")

    inventory = Inventory(user)


    while True:
        userAction = getInput(["1", "2", "3", "4", "5", "6"], "Please enter your option: (1) See Inventory, (2) Update Inventory, (3) Make Sales, (4) See Low Stock, (5) Produce Report, (6) Exit: ")
        print("")
        if(userAction == "1"):
            inventory.outputProductsList()
            print("")
            outputOptions = getInput(["1", "2", "3"], "Please enter your option: (1) Sort Inventory, (2) Find By Attribute, (3) Return: ")
            if(outputOptions=="1"):
                attribute = getInput(["price", "amount", "sales"], "Please input attribute to sort by (price/amount/sales): ")
                order = getInput(["ASC","DESC"], "Please input order to sort by (ASC/DESC): ")
                inventory.outputProductsList(inventory.sortBy(attribute, order))
            elif(outputOptions=="2"):
                attribute = getInput(["name", "supplier", "petType"], "Please input attribute to find (name/supplier/pettype): ")
                value = input("Please input value to find: ")
                foundList = inventory.findBy(attribute, value)
                if(len(foundList)<1):
                    print("The item you are looking for does not exist.")
                else:
                    inventory.outputProductsList(foundList)
        elif(userAction=="2"):
            continueAction=True
            while continueAction==True:
                updateOptions = getInput(["1", "2", "3", "4", "5"], "Please enter your option: (1) Add Product, (2) Remove Product, (3) Increase Stock, (4) Reduce Stock, (5) Back: ")
                
                if(updateOptions=="1"):
                    productType = getInput(["Accessories", "Edibles"], "Please input the type of product (Accessories/Edibles): ")
                    productName = input("Please input the product name: ")
                    supplier = input("Please input the supplier: ")
                    price = input("Please input the price of the product: ")
                    amount = input("Please input the amount: ")
                    minAmount = input("Please input the minimum stock amount: ")
                    sales = input("Please input the amount sold: ")
                    if(productType=="Accessories"):
                        opt1_temp = getInput(["yes", "no"], "Please input yes or no if the product is chewable (yes/no): ")
                        opt1 = False if opt1_temp=="no" else True
                        opt2 = input("Please enter the color of the product: ")
                    elif(productType=="Edibles"):
                        opt1 = getInput([], "Please enter the expiry date in the format (YYYYMMDD): ", "int")
                        opt2 = input("Please enter the type of animal that this is suited for: ")
                    inventory.addProduct(productType, productName, supplier, amount, minAmount, price, sales, opt1, opt2)
                    print("")
                    print(f"Product {productName} successfully added.")
                    continueInput = getInput(["yes", "no"], "Continue with another action? (yes/no): ")
                    continueAction = True if continueInput=="yes" else False
                    
                elif(updateOptions=="2"):
                    while True:
                        name = input("Please input product name: ")
                        if(len(inventory.findBy("name", name))>0):
                            break
                        print("Please enter a valid product.")
                    inventory.removeProduct(name)
                    print("")
                    print(f"Product {name} successfully removed.")
                    continueInput = getInput(["yes", "no"], "Continue with another action? (yes/no): ")
                    continueAction = True if continueInput=="yes" else False
                    
                elif(updateOptions=="3"):
                    while True:
                        name = input("Please input product name: ")
                        if(len(inventory.findBy("name", name))>0):
                            break
                        print("Please enter a valid product.")
                    amount = getInput([], "Please enter amount to increase: ", "int")
                    inventory.increaseStock(name, amount)
                    print("")
                    print(f"Product {name} successfully increased by {amount}.")
                    continueInput = getInput(["yes", "no"], "Continue with another action? (yes/no): ")
                    continueAction = True if continueInput=="yes" else False

                elif(updateOptions=="4"):
                    while True:
                        name = input("Please input product name: ")
                        if(len(inventory.findBy("name", name))>0):
                            break
                        print("Please enter a valid product.")
                    amount = getInput([], "Please enter amount to increase: ", "int")
                    inventory.decreaseStock(name, amount)
                    print("")
                    print(f"Product {name} successfully decreased by {amount}.")
                    continueInput = getInput(["yes", "no"], "Continue with another action? (yes/no): ")
                    continueAction = True if continueInput=="yes" else False

                elif(updateOptions=="5"):
                    break

        elif(userAction=="3"):
            while True:
                name = input("Please input product name: ")
                if(len(inventory.findBy("name", name))>0):
                    break
                print("Please enter a valid product.")
            amount = getInput([], "Please enter amount to increase: ", "int")
            salesAmount = inventory.makeSales(name, amount)
            print(f"The total sales amount is RM{salesAmount:.2f}")

        elif(userAction=="4"):
            lowStock = inventory.lowStock()
            inventory.outputProductsList(lowStock)
        
        elif(userAction=="5"):
            lowStockList = inventory.lowStock()
            sortedList = inventory.sortBy('sales', 'DESC')
            print(sortedList)
            report = Report(inventory.convertToList(inventory.productsDict), lowStockList, sortedList)
            report.produceReport()
            report.outputReport()
            report.outputToFile()

        elif(userAction=="6"):
            print("Thank you for using the system.")
            inventory.outputToFile()
            break        