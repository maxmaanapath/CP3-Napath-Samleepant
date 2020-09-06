print("Welcome to Magma Shop")
print("-- Please Login --")

usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == "admin" and passwordInput == "1234":
    print("Done!!")
    print("---Magma Shop---")
    print("1. Milk : 20 THB (press 1)")
    print("2. Coffee : 40 THB (press 2)")
    print("3. Tea : 30 THB (press 3)")
    print("4. Lemonade : 30 THB (press 4)")
    item = int(input("Choose drink : "))
    if item == 1:
        amount = int(input("Amount : "))
        price = 20*amount
        print("Milk 20 THB x",amount)
        print("Price : ",price,"THB")
        print("Thank you")
    elif item == 2:
        amount = int(input("Amount : "))
        price = 40*amount
        print("Coffee 40 THB x",amount)
        print("Price : ",price,"THB")
        print("Thank you")
    elif item == 3:
        amount = int(input("Amount : "))
        price = 30*amount
        print("Tea 30 THB x",amount)
        print("Price : ",price,"THB")
        print("Thank you")
    elif item == 4:
        amount = int(input("Amount : "))
        price = 30*amount
        print("Lemonade 30 THB x",amount)
        print("Price : ",price,"THB")
        print("Thank you")
    else:
        print("Error!! Wrong number")
else:
    print("!!Wrong Username or Password!!")
    print("Please Login Again")