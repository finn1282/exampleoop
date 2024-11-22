# Report = sales performance, stock levels, trend
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

class Report:

    def __init__(self, productList, lowStockList, sortedList):
        self.reportContent = []
        self.accessoriesReports = []
        self.ediblesReports = []
        self.sorted_list = []
        self.reversesorted_list = []
        self.accessoriesLowStock = []
        self.ediblesLowStock = []
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
        for i in self.sortedList[:5]:
            numbering = str(number) + ". "
            ranks = numbering + str(i['name'])
            self.sorted_list.append(ranks)
            number += 1
        
        number = 1
        for i in self.sortedList[:-6:-1]:
            numbering = str(number) + ". "
            ranks = numbering + str(i['name'])
            self.reversesorted_list.append(ranks)
            number += 1
        
        for i in self.sorted_list:
            print(i)
        
        print("\nLeast Popular Products:")
        for i in self.reversesorted_list:
            print(i)

    def outputToFile(self):
        with open("report.txt", "w") as file:
            file.writelines(self.reportContent)
            for i in self.sorted_list:
                file.writelines(i)
                file.write("\n")
            file.write("\nLeast Popular Products:")
            file.write("\n")
            for i in self.reversesorted_list:
                file.writelines(i)
                file.write("\n")


        a_points = []
        e_points = []

        for item in self.productList:
            typeOfProduct = item["productType"]
            if typeOfProduct == "Accessories":
                a_sales = item["sales"]
                a_points.append(a_sales)
            elif typeOfProduct == "Edibles":
                e_sales = item["sales"]
                e_points.append(e_sales)

        xa_points = np.array([0, 10, 20, 30])
        ya_points = np.array([0, (sum(a_points)/2),(sum(a_points)/1.5),sum(a_points)])

        xe_points = np.array([0, 10, 20, 30])
        ye_points = np.array([0, (sum(e_points)/3), (sum(e_points)/2.4), sum(e_points)])

        plt.subplot(1, 2, 1)
        plt.plot(xa_points, ya_points, marker="o")
        plt.title("Accessories")
        plt.ylabel("Total Sales of Accessories")
        plt.xlabel("Days in a month")

        plt.subplot(1, 2, 2)
        plt.plot(xe_points, ye_points, marker="o")
        plt.title("Edibles")
        plt.ylabel("Total Sales of Edibles")
        plt.xlabel("Days in a month")

        plt.subplots_adjust(
            left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4
        )
        plt.suptitle("Sales Performance")
        plt.savefig("Sales_performance.png")
        plt.show()

