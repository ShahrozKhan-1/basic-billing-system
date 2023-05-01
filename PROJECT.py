import os

prices = [] # list to add prices
items = []  # list to add items
cart = []   # list to add item entered from user 

# Admin domain
def admin():
    print("1.Add item")
    print("2.Add price")
    print("3.Check item")
    print("write user to get into user account")
    value = input("Enter: ")
    os.system("cls")

    match (value):

        # entering items and append the items to the list
        case "1":
            print("Enter the items you want to add")
            print("NOTE: type quit to stop entering data")
            while True:
                item = input("Enter: ")
                item.upper()
                if item.lower() == "quit":
                    break
                items.append(item)
            os.system("cls")
            return admin()
        
        # entering prices and append it to the list

        case "2":
            print("ITEMS")
            print("*" * 50)
            for item in items:
                print(item)
            print("Add price respectively to your items")
            print("NOTE: type quit to stop entering data")
            while True:
                price = input("Enter: ")
                if price.lower() == "quit":
                    break
                prices.append(price)
            os.system("cls")
            return admin()

        # checks item
        case "3":
            print("ITEM\t\tPRICE")
            print("-" * 30)
            for elem1, elem2 in zip(items, prices):
                print(elem1,"\t|\t",elem2)
            a = input("press \'y\' to continue: ")
            if a.lower() == "y":
                os.system("cls")
                return admin()
        
        case "user":
            user()

        case _:
            print("wrog input")
            return admin()
            
        # User domain
def user():
    print("Select following")
    print("1.Check Items")
    print("2.Purchase Item")
    x = input("Enter: ")

    # user to see items and price 
    match x:
        case '1':
            print("Item\t\t\tPrice")
            print("-" * 30)
            for elem1, elem2 in zip(items, prices):
                print(elem1,"\t\t\t|\t\t",elem2)
            x = input("Press '\y'\ to continue: ")
            if x.lower()=='y':
                user()
                print("*" * 50)
            
        # getting item inputs to buy
        case "2":
            os.system("cls")
            total = 0
            print("Enter the product you want to buy")
            print("write quit to exit")
            while True:
                buy = input("Enter: ")
                if buy in items:
                    cart.append(buy)
                elif buy.lower() == "quit":
                    break
                else :
                    print("Sorry we do not have that item")
                    return
            print("*" * 30)
            print("ITEM\t\t\tPRICE")
            print("-"*30)
            for item in cart:
                index = items.index(item)
                price = int(prices[index])
                total += price
                print(f"{item}\t\t{price}")
            print("-"*30)
            print(f"Your total is: {total}")
       
        case _:
            print("Wrong input")
            return user()


# Main body
os.system('cls')
var = "!!!Welcome!!!"
b=var.center(100)
print(b)
print("Admins")
print("User")
get = input("Enter: ")
if get.lower() == "admin":
    x=int(input("Password: "))  # password 1234
    if x == 1234:
        os.system("cls")
        admin()
            
elif get == "user":
    user()
