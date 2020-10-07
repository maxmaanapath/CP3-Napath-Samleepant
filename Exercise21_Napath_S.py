from tkinter import *
import math

def leftClickButton(event):
    Result = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2)
    if Result >= 30.0:
        BMIResult = "อ้วนมาก"
    elif Result >= 25.0 and Result <= 29.9:
        BMIResult = "อ้วน"
    elif Result >= 23.0 and Result <= 24.9:
        BMIResult = "น้ำหนักเกิน"
    elif Result >= 18.6 and Result <= 22.9:
        BMIResult = "น้ำหนักปกติ เหมาะสม"
    else:
        BMIResult = "ผอมเกินไป"

    labelResult.configure(text=BMIResult)

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