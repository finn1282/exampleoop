# Report = sales performance, stock levels, trend
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
import textwrap

class Report:

    def __init__(self, productList, lowStockList, sortedList):
        self.reportContent = []
        self.accessoriesReports = []
        self.ediblesReports = []
        self.accessoriesLowStock = []
        self.ediblesLowStock = []
        self.sales = []
        self.names = []
        self.reversedNames = []
        self.productList = productList
        self.lowStockList = lowStockList
        self.sortedList = sortedList

    def produceReport(self):

        for item in self.productList:
            typeOfProduct = item["productType"]

            if typeOfProduct == "Accessories":
                a_name = item["name"]
                a_supplier = item["supplier"]
                a_price = item["price"]
                a_amount = item["amount"]
                a_minAmount = item["minAmount"]
                a_sales = item["sales"]
                a_isChewable = item["isChewable"]
                a_color = item["color"]
                a_list = [a_name, a_price, a_supplier, a_amount, a_minAmount, a_sales, a_isChewable, a_color]
                self.accessoriesReports.append(a_list)

            elif typeOfProduct == "Edibles":
                e_name = item["name"]
                e_supplier = item["supplier"]
                e_price = item["price"]
                e_amount = item["amount"]
                e_minAmount = item["minAmount"]
                e_sales = item["sales"]
                e_expiryDate = item["expiryDate"]
                e_petType = item["petType"]
                e_list = [e_name, e_price, e_supplier, e_amount, e_minAmount, e_sales, e_expiryDate, e_petType]
                self.ediblesReports.append(e_list)

        for item in self.lowStockList:
            typeOfProduct = item["productType"]

            if typeOfProduct == "Accessories":
                a_name = item["name"]
                a_supplier = item["supplier"]
                a_price = item["price"]
                a_amount = item["amount"]
                a_minAmount = item["minAmount"]
                a_sales = item["sales"]
                a_isChewable = item["isChewable"]
                a_color = item["color"]
                a_list = [a_name, a_price, a_supplier, a_amount, a_minAmount, a_sales, a_isChewable, a_color]
                self.accessoriesLowStock.append(a_list)

            elif typeOfProduct == "Edibles":
                e_name = item["name"]
                e_supplier = item["supplier"]
                e_price = item["price"]
                e_amount = item["amount"]
                e_minAmount = item["minAmount"]
                e_sales = item["sales"]
                e_expiryDate = item["expiryDate"]
                e_petType = item["petType"]
                e_list = [e_name, e_price, e_supplier, e_amount, e_minAmount, e_sales, e_expiryDate, e_petType]
                self.ediblesLowStock.append(e_list)


        for item in self.sortedList[0:5]:
            name = item["name"]
            self.names.append(name)
            sale = item["sales"]
            self.sales.append(sale)
        for item in self.sortedList[:-6:-1]:
            name = item["name"]
            self.reversedNames.append(name)

        
        a_rowReport = tabulate(self.accessoriesReports, headers=["Product Name", "Price (RM)", "Supplier", "Amount", "Minimum Amount", "Sales", "Chewable", "Color"], floatfmt=".2f")
        e_rowReport = tabulate(self.ediblesReports, headers=["Product Name", "Price (RM)", "Supplier", "Amount", "Minimum Amount", "Sales", "Expiry Date", "Pet Type"], floatfmt=".2f")
        a_lowStock = tabulate(self.accessoriesLowStock, headers=["Product Name", "Price (RM)", "Supplier", "Amount", "Minimum Amount", "Sales", "Chewable", "Color"], floatfmt=".2f")
        e_lowStock = tabulate(self.ediblesLowStock, headers=["Product Name", "Price (RM)", "Supplier", "Amount", "Minimum Amount", "Sales", "Expiry Date", "Pet Type"], floatfmt=".2f")

        self.reportContent.append("All Accessories:")
        self.reportContent.append("\n")
        self.reportContent.append(a_rowReport)
        self.reportContent.append("\n")
        self.reportContent.append("\nAll Edibles:")
        self.reportContent.append("\n")
        self.reportContent.append(e_rowReport)
        self.reportContent.append("\n")
        self.reportContent.append("\n")
        self.reportContent.append("\nAccessories Low Stock:")
        self.reportContent.append("\n")
        self.reportContent.append(a_lowStock)
        self.reportContent.append("\n")
        self.reportContent.append("\n")
        self.reportContent.append("\nEdibles Low Stock:")
        self.reportContent.append("\n")
        self.reportContent.append(e_lowStock)
        self.reportContent.append("\n")
        self.reportContent.append("\n")
        self.reportContent.append("\n")
        self.reportContent.append("\nCurrent Trends")
        self.reportContent.append("\n")
        self.reportContent.append("\nMost Popular Products:")
        self.reportContent.append("\n")

        return self.reportContent

    def outputReport(self):
        for i in self.reportContent:
            if i == "\n":
                continue
            print(i)
        number = 1
        for i in self.names:
            print(str(number) + ". " + str(i))
            number += 1
        number = 1
        print("\nLeast Popular Products:")
        for i in self.reversedNames:
            print(str(number) + ". " + str(i))
            number += 1

    def outputToFile(self):
        with open("report.txt", "w") as file:
            file.writelines(self.reportContent)
            number = 1 
            for i in self.names:
                    file.writelines(str(number) + ". " + str(i))
                    file.write("\n")
                    number += 1
            file.write("\nLeast Popular Products:")
            file.write("\n")
            number = 1 
            for i in self.reversedNames:
                file.writelines(str(number) + ". " + str(i))
                file.write("\n")
                number += 1

        # # Code for creating barchart
        
        x = np.arange(5)
        ya = np.array(self.sales)

        plt.figure(figsize=(10,9))
        plt.bar(x,ya, color='aqua', edgecolor='black', alpha=0.8)
        for i in range(len(self.names)):
            plt.text(i, self.sales[i]+1, self.sales[i], ha = 'center')
        plt.title("Popular Products",fontname='Serif',fontsize=20,pad=30)
        plt.ylabel("Sales",fontname='Serif', fontsize=14)
        plt.xlabel("Product Name",fontname='Serif',fontsize=14)

        # Wrap text for multi-line labels
        wrapped_names = ['\n'.join(textwrap.wrap(name, 10)) for name in self.names]

        plt.xticks(ticks=np.arange(len(self.names)), labels=wrapped_names,fontname='Serif')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.savefig("Sales_performance.png",dpi=300)
        plt.show()