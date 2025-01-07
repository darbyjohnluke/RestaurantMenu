menu = {
    "Pixxa":240,
    "Borgaar":360,
    "Paasta":440,
    "Coffee":120,
    "Tea":70
}
x = list(menu.keys())

print("Welcome to Darby's")
for y in x:
    print(y + " =", menu[y])
orderList = []
decision = "Yes"
orderTotal = 0
def takeOrder():
    global orderTotal
    order = input("What item would you like to order?, If you want to see menu again, type 'menu' \n")
    if order == "menu":
        for y in x:
            print(y + " =", menu[y])
    else:
        while order not in menu:
            print("This is not an item we serve")
            order = input("Please enter the correct item, If you want to see menu again, type 'menu': ")
            if order == "menu":
                for y in x:
                    print(y + " =", menu[y])
            else:
                while order not in menu:
                    print("This is not an item we serve")
                    break
                else:
                    orderList.append(order)
                    orderTotal += menu[order]
                    break
                break
        else:
            orderList.append(order)
            orderTotal += menu[order]
            print(f"Ok {order} has been added to the order")
        return 0

while decision == "Yes":
    takeOrder()
    decision = input("Would you like to order more? (Yes or No) ")
else:
    print(f"Your Order is {orderList}")
    print(f"Your Total Bill amount is {orderTotal}")
