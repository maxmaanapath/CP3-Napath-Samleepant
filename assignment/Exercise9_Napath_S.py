usernameInput = input("Username : ")
passwordInput = input("Password : ")
while usernameInput != "admin" or passwordInput != "1234":
    print("Wrong username or password!! Please Login again!!")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
print("Done !!")