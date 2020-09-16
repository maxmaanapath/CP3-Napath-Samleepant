menuList = []
priceList = []

def showBill():
    totalPrice = 0
    textShowmenu = "My Food"
    print(textShowmenu.center(21,"-"))
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice += int(priceList[number])
    print("Total Price(THB) :",totalPrice)

while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price(THB) :")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()