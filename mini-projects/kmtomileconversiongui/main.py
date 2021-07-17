from tkinter import *
from math import *

window = Tk()
window.title = "Miles to km Converter"
window.minsize(width=350, height=200)
window.config(padx= 50, pady=50)

def convert_miles_to_km():
    miles = int(miles_entry.get())
    kilometers = round(miles*1.6)
    output_label.config(text = kilometers)

miles_entry = Entry(width = 15)
miles_entry.grid(row=0, column= 1)

miles_label = Label(text="miles")
miles_label.grid(row=0, column= 2)

output_label = Label(text = "0")
output_label.grid(row = 1,column = 1)

is_equal_to_label = Label(text ="is equal to ")
is_equal_to_label.grid(row =1,column= 0)

km_label = Label(text = "km")
km_label.grid(row =1, column = 2)

button = Button(text = "Calculate", command=convert_miles_to_km)
button.grid(row = 2, column = 1)



window.mainloop()