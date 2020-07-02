from tkinter import *
import calendar

window = Tk()
window.title("Calendar")
window.geometry("270x340")

def search():

    months = month.get()
    years = year.get()
    month_int = int(months)
    year_int = int(years)

    cal = calendar.month(year_int, month_int)

    textfield.delete(0.0, END)

    textfield.insert(INSERT, cal)

month_label = Label(window, text = "Select Month : ", font=('monaco', 15, 'bold'))
month_label.place(x = 10, y = 10)

month = Spinbox(window, from_ = 1, to = 12, width = 5, font=("monaco", 15, "bold"))
month.place(x = 160, y = 10)

year_label = Label(window, text = "Select Year : ", font=('monaco', 15, 'bold'))
year_label.place(x = 10, y = 50)


year = Spinbox(window, from_ = 1900, to = 2100, width = 5, font=("monaco", 15, "bold"))
year.place(x = 160, y = 50)


search_button = Button(window, text = "Search", relief=GROOVE, width=10, font=("monaco", 15, "bold"), command = search)
search_button.place(x = 70, y = 100)

textfield = Text(window, height = 10, bd = 5, width = 25, relief=GROOVE, fg = 'red')
textfield.place(x = 17, y = 150)


window.mainloop()

    
search()
