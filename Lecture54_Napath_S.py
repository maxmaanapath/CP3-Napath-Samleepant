def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("Wrong username or password!! Please Login again!!")
        return login()
def showMenu():
    print("---Magma Shop---")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    number = int(input("Choose : "))
    if number == 1:
        return vatCalculate(int(input("Price (THB) : ")))
    elif number == 2:
        return priceCalculate()
    else:
        print("Wrong number!! Choose number again!!")
        return menuSelect()
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return str(result)+" THB"
def priceCalculate():
    price1 = int(input("First Product Price (THB) : "))
    price2 = int(input("Second Product Price (THB) : "))
    return vatCalculate(price1+price2)

print("Welcome to Magma Shop")
print("-- Please Login --")
print(login())
print("-- Thank you --")