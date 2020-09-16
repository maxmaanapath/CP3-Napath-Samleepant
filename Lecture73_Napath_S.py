systemMenu = {"ข้าวหมกไก่":45,"ข้าวมันไก่":40,"ข้าวมันไก่ผสม":50,"ข้าวมันไก่พิเศษ":45,"ข้าวขาหมู":40,"ข้าวหมูแดง":40}
menuList = []

def showBill():
    totalPrice = 0
    # set texts to center
    textShowmenu = "My Food"
    print(textShowmenu.center(21,"-"))

    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1],"THB")
        totalPrice += int(menuList[number][1])
    print("Total Price(THB) :", totalPrice)

while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
showBill()