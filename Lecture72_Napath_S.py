menuList = []
def showBill():
    totalPrice = 0
#set texts to center
    textShowmenu = "My Food"
    print(textShowmenu.center(21,"-"))

    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1], "THB")
        totalPrice += int(menuList[number][1])
    print("Total Price(THB) :",totalPrice)

while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price(THB) :")
        menuList.append([menuName,menuPrice])
showBill()