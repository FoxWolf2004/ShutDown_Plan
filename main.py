import os
from tkinter import Tk
from tkinter import *
from tkinter import messagebox

hour = 3600
min686  = 60
fullTime = 0

def Plan():
    f = int(selecter.get())
    os.system(f'shutdown -s -t {f}')
    messagebox.showinfo('успех', f'запланировали выключение через {int(f / hour)} часа')
    print(f)

def offPlan():

    os.system('shutdown -a')
    messagebox.showinfo('успех', f'отмена выключения ')



window = Tk()
window.title("PowerTimer V1,1")
window.geometry('400x250')
window.resizable(width=False, height=False)



lbl = Label(window, text="запланированое выключение", font=("Arial Bold", 10))
lbl.grid(column=2, row=30)

selecter = IntVar()

#выбор кол во часов
rad1 = Radiobutton(window, text='через 1 час', value=(hour * 1),variable=selecter)
rad2 = Radiobutton(window, text='через 2 часа', value=(hour * 2),variable=selecter)
rad3 = Radiobutton(window, text='через 5 часов', value=(hour * 5),variable=selecter)
rad1.grid(column=1, row=40)
rad2.grid(column=2, row=40)
rad3.grid(column=3, row=40)


btn = Button(window, text="Запланировать ",command=Plan)
btn.grid(column=2, row=50)

btn = Button(window, text="отменить",command=offPlan)
btn.grid(column=2, row=55)

window.mainloop()



#h = int(input("часы >>>"))
#m = int(input("минуты >>"))
#fullTime = (h * hour)+(m * min)
#os.system(f'shutdown -s -t {fullTime}')
#os.system('shutdown -a')q23124214