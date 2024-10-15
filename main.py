from tkinter import *
import calendar

root=Tk()
root.geometry("250x150")

root.title("Calendar")
root.config(bg="black")

def showCal():
    newGUI=Tk()
    newGUI.geometry("1000x1000")
    newGUI.config(bg="white")
    newGUI.title("CalendarCalendar")
    fetch_year=int(calendar_entry.get())
    calendar_content=calendar.calendar(fetch_year)
    calendar_year_label=Text(newGUI,font="Consolas 10 bold")
    calendar_year_label.insert(END,calendar_content)
    calendar_year_label.grid(row=5,column=1,padx=20)
    newGUI.mainloop()


calendar_label=Label(root,text="CALENDAR")
calendar_label.grid(row=1,column=1)

enteryear_label=Label(root,text="Enter Year: ")
enteryear_label.grid(row=2,column=1)

calendar_entry=Entry(root,width=30)
calendar_entry.grid(row=3,column=1)

btn=Button(root,text="Show Calendar",command=showCal)
btn.grid(row=6,column=1)

exbtn=Button(root,text="Exit",command=exit)
exbtn.grid(row=5,column=1)



root.mainloop()