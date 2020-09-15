number = int(input())
for i in range(number):
    pyramid = ("*"*((i*2)+1))
    print(pyramid.center(21," "))