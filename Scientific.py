from tkinter import *
import math

windows = Tk()
windows.minsize(10, 25)
windows.title("Standard Calculator")

#Display Screen:
display = Listbox(windows, height = 10, width = 50)
display.grid(row = 0, column = 0, rowspan = 1, columnspan = 5)

#x^2 button:
xsq = Button(windows, text = f"x\u00b2", height = 2, width = 7, command = lambda:output("sq"))
xsq.grid(row = 1, column = 0)

#1 button:
value1 = StringVar()
one_button = Button(windows, text = "1", height = 2, width = 7, command = lambda:output("1"))
one_button.grid(row = 1, column = 1)

#2 button:
value2 = StringVar()
two_button = Button(windows, text = "2", height = 2, width = 7, command = lambda:output("2"))
two_button.grid(row = 1, column = 2)

#3 button:
value3 = StringVar()
three_button = Button(windows, text = "3", height = 2, width = 7, command = lambda:output("3"))
three_button.grid(row = 1, column = 3)

#4 button:
value4 = StringVar()
four_button = Button(windows, text = "4", height = 2, width = 7, command = lambda:output("4"))
four_button.grid(row = 2, column = 1)

#5 button:
value5 = StringVar()
five_button = Button(windows, text = "5", height = 2, width = 7, command = lambda:output("5"))
five_button.grid(row = 2, column = 2)

#6 button:
value6 = StringVar()
six_button = Button(windows, text = "6", height = 2, width = 7, command = lambda:output("6"))
six_button.grid(row = 2, column = 3)

#7 button:
value7 = StringVar()
seven_button = Button(windows, text = "7", height = 2, width = 7, command = lambda:output("7"))
seven_button.grid(row = 3, column = 1)

#8 button:
value8 = StringVar()
eight_button = Button(windows, text = "8", height = 2, width = 7, command = lambda:output("8"))
eight_button.grid(row = 3, column = 2)

#9 button:
value9 = StringVar()
nine_button = Button(windows, text = "9", height = 2, width = 7, command = lambda:output("9"))
nine_button.grid(row = 3, column = 3)

#0 button:
value0 = StringVar()
zero_button = Button(windows, text = "0", height = 2, width = 7, command = lambda:output("0"))
zero_button.grid(row = 4, column = 2)

#C button:
clear_button = Button(windows, text = "C", height = 2, width = 7, command = clearlistbox)
clear_button.grid(row = 4, column = 1)

#'=' button:
equal_button = Button(windows, text = "=", height = 2, width = 7, command = finalresult)
equal_button.grid(row = 4, column = 3)

#'+' button:
plus_button = Button(windows, text = "+", height = 2, width = 7, command = lambda:output("+"))
plus_button.grid(row = 1, column = 4)

#'-' button:
minus_button = Button(windows, text = "-", height = 2, width = 7, command = lambda:output("-"))
minus_button.grid(row = 2, column = 4)

#'*' button:
into_button = Button(windows, text = "*", height = 2, width = 7, command = lambda:output("*"))
into_button.grid(row = 3, column = 4)

#'/' button:
div_button = Button(windows, text = "/", height = 2, width = 7, command = lambda:output("/"))
div_button.grid(row = 4, column = 4)

windows.mainloop()