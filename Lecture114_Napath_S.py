from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates, CurrencyCodes


rate = CurrencyRates()
code = CurrencyCodes()


def Result(event):
    result = (rate.convert(first_currency_box.get(), convert_currency_box.get(), float(amount.get())))
    convert_result.configure(text = result)

def NameRates(event):
    name = code.get_currency_name(),

main_window = Tk()
main_window.title ("Exchange rate calculator")
main_window.configure(bg = "#34495E")
title = Label(main_window, text = "Exchange rate calculator",
              bg = "#34495E",fg = "White", font=("Saraban",10))
title.grid(row = 0 , column = 1)
first_currency = Label(main_window, text ="From : ",fg = "White" , bg = "#34495E")
first_currency.grid(row = 1 , column = 0)
first_currency_box = ttk.Combobox(main_window)
first_currency_box['values'] = list(rate.get_rates("").keys())
first_currency_box.current(29)
first_currency_box.bind("<<ComboboxSelected>>")
first_currency_box.grid(row = 1 , column = 1)
text = Label(main_window, text = "Amounts", bg = "#34495E")
text.grid(row = 4 , column = 2)
amount = Entry(main_window, text = "Input Amounts : ")
amount.grid(row = 1 , column = 3)
convert_currency = Label(main_window, text = "To : ", bg = "#34495E")
convert_currency.grid(row = 5 , column = 0)
convert_currency_box = ttk.Combobox(main_window)
convert_currency_box['values'] = list(rate.get_rates("").keys())
convert_currency_box.current(10)
convert_currency_box.bind("<<ComboboxSelected>>")
convert_currency_box.grid(row = 5 , column = 1)
convert_result = Label(main_window, text = "Result : ", bg = "#34495E")
convert_result.grid(row = 5 , column = 3)
convert_button = Button(main_window, text = "Convert", width=15)
convert_button.bind('<Button-1>', Result)
convert_button.grid(row = 4 , column = 4)


main_window.mainloop()