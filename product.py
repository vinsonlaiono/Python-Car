# Name: Vinson Aiono
# Date: 4/3/2018
# Coding Dojo Python Stack
# Description: Make a store that has certain attributes and methods and keeps track of products

#create a class called products
# set variables for class - {price, item name, weight, brand, status: default to sold}
# create methods for class - 
# Sell() - changes the status to "Sold"
# addTax() - takes a tax as a decimal amount as a parameter and returns the price of the item icluding sales tax
# Return() - tales reason_for_return as a parameter. if defective change status to defective and change price to 0
# if returned in box change status like new if open box change status to used and apply a 20% discount

class Product:

    def __init__(self, price, item_name, weight, brand, tax):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.tax = tax
        self.status = 'For Sale'

        self.display_info()           
    
    def display_info(self):
        print('Bike Cost:', self.price)
        print('Name:', self.item_name)
        print('Weight:', self.weight)
        print('Brand:', self.brand)
        print('Status:', self.status)
        return self

    # Changes the status of the product from sold to for sale
    def sell(self):
        self.status = 'Sold'
        print(self.status)
        return self
    # Add tax to price pf the car
    def AddTax(self, tax):
        tax = self.price * self.tax
        print(self.price + tax)
        return self

    def returnItem(self, reason_for_return):
        if reason_for_return == 'Defective':
            self.status = 'Defective'
            self.price = 0.00
        elif reason_for_return == 'Unopened':
            self.status = 'Like New'
        if reason_for_return == 'Exchange':
            self.status = 'Used'
            discount = self.price * .20
            self.price -= discount
        print(self.status)
        print(self.price)
        return self

bike = Product(1500.00, 'Nimbus2000', 24, 'Mongoose', .10)


# bike.AddTax(.21)
# bike.sell()
# bike.returnItem('Exchange')