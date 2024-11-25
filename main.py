#importing inventory class and report class
from classes.Inventory import * 
from classes.Report import *


#function to validate input
def getInput(inputValues, display, type="str"):
    #if string, checks input for list of input values
    if(type=="str"):
        while True:
            userInput = input(display).lower()
            for i in inputValues:
                if userInput == i.lower():
                    return i
            print("Input not recognised, please input a valid selection.")
    #if int, check that it is positive int
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

    #initialize inventory object with user
    inventory = Inventory(user)

    while True:
        userAction = getInput(["1", "2", "3", "4", "5", "6"], "Please enter your option: (1) See Inventory, (2) Update Inventory, (3) Make Sales, (4) See Low Stock, (5) Produce Report, (6) Exit: ")
        print("")

        #option 1 - display inventory
        if(userAction == "1"):
            #call inventory object method to display inventory list
            inventory.outputProductsList()
            print("")

            #get second set of action (sort, find)
            outputOptions = getInput(["1", "2", "3"], "Please enter your option: (1) Sort Inventory, (2) Find By Attribute, (3) Return: ")
            
            #option 1 - sort
            if(outputOptions=="1"):
                #input attribute to sort by
                attribute = getInput(["price", "amount", "sales"], "Please input attribute to sort by (price/amount/sales): ")
                #input order for sorting
                order = getInput(["ASC","DESC"], "Please input order to sort by (ASC/DESC): ")
                #display sorted list
                inventory.outputProductsList(inventory.sortBy(attribute, order))

            #option 2 - find
            elif(outputOptions=="2"):
                #input attribute to find by
                attribute = getInput(["name", "supplier", "petType"], "Please input attribute to find (name/supplier/pettype): ")
                #input value to match
                value = input("Please input value to find: ")
                foundList = inventory.findBy(attribute, value)
                #check if value exists
                if(len(foundList)<1):
                    print("The item you are looking for does not exist.")
                #if value exists, display value
                else:
                    inventory.outputProductsList(foundList)

        #option 2 - update inventory
        elif(userAction=="2"):
            #initialize variable to check repeat action
            continueAction=True
            while continueAction==True:

                #get second set of actions, add, remove, increase, decrease
                updateOptions = getInput(["1", "2", "3", "4", "5"], "Please enter your option: (1) Add Product, (2) Remove Product, (3) Increase Stock, (4) Reduce Stock, (5) Back: ")
                
                #option 1 - add product
                if(updateOptions=="1"):

                    #input all properties for product class
                    productType = getInput(["Accessories", "Edibles"], "Please input the type of product (Accessories/Edibles): ")
                    productName = input("Please input the product name: ")
                    supplier = input("Please input the supplier: ")
                    price = input("Please input the price of the product: ")
                    amount = getInput([], "Please input the amount: ", "int")
                    minAmount = getInput([], "Please input the minimum stock amount: ", "int")
                    sales = getInput([], "Please input the amount sold: ", "int")

                    #check if product should be accessory class or edible class to get additional inputs
                    if(productType=="Accessories"):
                        opt1_temp = getInput(["yes", "no"], "Please input yes or no if the product is chewable (yes/no): ")
                        opt1 = False if opt1_temp=="no" else True
                        opt2 = input("Please enter the color of the product: ")
                    elif(productType=="Edibles"):
                        opt1 = getInput([], "Please enter the expiry date in the format (YYYYMMDD): ", "int")
                        opt2 = input("Please enter the type of animal that this is suited for (cat/dog/etc): ")

                    #call method to create product object and add to list in inventory
                    inventory.addProduct(productType, productName, supplier, amount, minAmount, price, sales, opt1, opt2)

                    #output success message
                    print("")
                    print(f"Product {productName} successfully added.")

                    #check if user continues
                    continueInput = getInput(["yes", "no"], "Continue with another action? (yes/no): ")
                    continueAction = True if continueInput=="yes" else False

                #option 2 - remove product   
                elif(updateOptions=="2"):
                    #get product name input and check if product is existing in list
                    while True:
                        name = input("Please input product name: ")
                        #calls find method to find product by name from inventory list
                        find = inventory.findBy("name", name)
                        if(len(find)>0):
                            break
                        print("Please enter a valid product.")

                    #call remove method to remove product
                    inventory.removeProduct(find[0]['name'])

                    #output success message
                    print("")
                    print(f"Product {name} successfully removed.")

                    #check if user continues
                    continueInput = getInput(["yes", "no"], "Continue with another action? (yes/no): ")
                    continueAction = True if continueInput=="yes" else False
                    

                #option 3 - increase stock
                elif(updateOptions=="3"):
                    #get product name input and check if product is existing in list
                    while True:
                        name = input("Please input product name: ")
                        #calls find method to find product by name from inventory list
                        find = inventory.findBy("name", name)
                        if(len(find)>0):
                            break
                        print("Please enter a valid product.")

                    #input amount to increase
                    amount = getInput([], "Please enter amount to increase: ", "int")

                    #call method to increase stock of object within list
                    inventory.increaseStock(find[0]['name'], amount)

                    #output success message
                    print("")
                    print(f"Product {name} successfully increased by {amount}.")

                    #checks if user continues
                    continueInput = getInput(["yes", "no"], "Continue with another action? (yes/no): ")
                    continueAction = True if continueInput=="yes" else False

                #option 4 - remove stock
                elif(updateOptions=="4"):
                    #get product name input and check if product is existing in list
                    while True:
                        name = input("Please input product name: ")
                        #calls find method to find product by name from inventory list
                        find = inventory.findBy("name", name)
                        if(len(find)>0):
                            break
                        print("Please enter a valid product.")

                    #input amount to remove
                    amount = getInput([], "Please enter amount to remove: ", "int")

                    #call method to remove stock of object within list
                    inventory.decreaseStock(find, amount)

                    #output success message
                    print("")
                    print(f"Product {name} successfully decreased by {amount}.")

                    #check if user continues
                    continueInput = getInput(["yes", "no"], "Continue with another action? (yes/no): ")
                    continueAction = True if continueInput=="yes" else False

                #option 5 - user exits
                elif(updateOptions=="5"):
                    break

        #option 3 - make sales
        elif(userAction=="3"):
                #get product name input and check if product is existing in list
            while True:
                name = input("Please input product name, enter blank to cancel: ")
                find = inventory.findBy("name", name)
                if name=="":
                    break
                if(len(find)>0):
                    while True:
                        #get amount of sales
                        amount = getInput([], "Please enter amount to be sold: ", "int")

                        #check if product stock amount is enough for sales
                        if(amount>find[0]['amount']):
                            print("Sales amount exceeded stock, please enter amount again.")
                            continue

                        #calls method to make sales
                        salesAmount = inventory.makeSales(find[0]['name'], amount)

                        #output success message
                        print(f"The total sales amount is RM{salesAmount:.2f}")
                        break
                    break
                #output error if product cannot be found
                print("Please enter a valid product.")

        #option 4 - display low stock
        elif(userAction=="4"):
            #call method to return list of low stock
            lowStock = inventory.lowStock()
            #display list of low stock
            inventory.outputProductsList(lowStock)
        
        #option 5 - produce report
        elif(userAction=="5"):
            #call method to return list of low stock
            lowStockList = inventory.lowStock()
            #call method to return sorted list of highest sales
            sortedList = inventory.sortBy('sales', 'DESC')
            #initialize report object, passing product list, low stock list, sorted highest sales list
            report = Report(inventory.convertToList(inventory.productsDict), lowStockList, sortedList)
            #call produce report method
            report.produceReport()
            #display report
            report.outputReport()
            #output report to file
            report.outputToFile()

        #option 6 - user exits
        elif(userAction=="6"):
            #output thank you message
            print("Thank you for using the system.")
            #saves user data to file
            inventory.outputToFile()
            break        