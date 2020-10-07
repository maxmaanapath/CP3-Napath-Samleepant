from tkinter import *
import math

def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))

MainWindow = Tk()
labelHeight = Label(MainWindow, text = "ส่วนสูง(Cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
textBoxHeight.get()

labelWeight = Label(MainWindow, text = "น้ำหนัก(Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
textBoxWeight.get()

calculateButton = Button(MainWindow, text = "คำนวณค่า BMI")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)

labelResult = Label(MainWindow, text = "ผลลัพธ์")
labelResult.grid(row=2,column=1)
MainWindow.mainloop()