class Seller:
    def __init__ (self):
        self.product_quantity = {}
        self.product_price = {}
        self.profit = 0

    def update(self):
        item_name = input("ENTER NAME:")
        item_quantity = input("ENTER QUANTITY:")
        item_price = int(input("ENTER SELLING PRICE:"))
        self.product_quantity[item_name] = item_quantity
        self.product_price[item_price] = item_price

    def show(self):
        print("showing items...")
        for i, j in self.product_quantity.items():
            print(i, j)

    def buy(self,item_name,quantity):
        if quantity > self.product_quantity.get(item_name):
            print("Sorry we don't have that quantity")
        else:
            self.product_quantity[item_name] = self.product_quantity.get(item_name) - quantity
            self.profit = self.product_price.get(item_name)*quantity
            #i+=1 -> i=i+1

class Buyer:
    def __init__(self):
        self.cart = {}
        self.quantity = {}
        self.total_amount = 0

    def search(self,seller,item_name):
        if seller.product_quantity.get(item_name):
            print("Quantity: "+ str(seller.product_quantity.get(item_name)))
            print("Price per product: "+ str(seller.product_quantity.get(item_name)))
            choice = input("Do you want to add this in cart? y/n: ")
            if choice == "y":
                quantity = int(input("Enter quantity:"))
                if quantity > seller.products_quantity.get(item_name):
                    print("That quantity does not exist")
                    self.search(seller,item_name)
                else:
                    self.cart[item_name] = seller.products_proice.get(item_name)*quantity
                    self.quantity[item_name] = quantity
                    self.total_amount += seller.product_price.get(item_name)*quantity
            else:
                pass
        else:
            return ("Your requested product does not exist")

    def show(self):
        print("showing items...")
        for i, j in self.cart.items():
            print(i, j)

    def buy(self,seller):
        print("These are the items in your cart....")
        self.show()
        print("Total payable amount is: "+ str(self.total_amount))
        for item,quantity in self.quantity.items():
            seller.buy(item,quantity)

out_option = True
seller = Seller()
buyer = Buyer()
while out_option:
    choice = input("Are you buyer ot seller? b/s:")
    if choice == "s":
        option = True
        while option:
            print("1.Update items")
            print("2.Show items")
            print("3. Exit")
            choice = input("ENTER OPTION:")
            if choice == "1":
                seller.update()
            elif choice == "2":
                seller.show()
            elif choice == "3":
                option = False
            else:
                print("Enter valid choice of move out....")
    elif choice == "b":
        option = True
        while option:
            print("1.Search items")
            print("2.Buy items")
            print("3. Exit")
            choice = input("ENTER OPTION:")
            if choice == "1":
                item_name = input("Enter name of product:")
                buyer.search(seller,item_name)
            elif choice == "2":
                buyer.search(seller)
            elif choice == "3":
                option = False
            else:
                print("Enter valid choice of move out....")
else:
    out_option = False
    print("Exiting system...thank you for staying...")