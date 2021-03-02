# importing tkinter

from tkinter import*

#importing calendar  module
import calendar
#initializing tkinter 
root = Tk()
# setting title of our GUI
root.title("My Own Gui Calendar ")
# year fow which we want calendar to be shown
year =2021
#storing 2021 year calender data inside myCal
myCal = calendar.calendar(year)
# showing calendar data using label widget
cal_year =Label(root, text=myCal, font="Consolas 10 bold")
# packing the Label widget
cal_year.pack()
#running  the program in ready state 
root.mainloop()





