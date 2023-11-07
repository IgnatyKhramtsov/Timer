from tkinter import *
from tkinter import messagebox
import time

cd_id= ''

# def clicked():
#     global tre
#     tre = False
#
#     try:
#         hour = int(hours.get())
#     except:
#         hour = 0
#         h.set(0)
#
#     try:
#         minute = int(minutes.get())
#     except:
#         minute = 0
#         m.set(0)
#
#     try:
#         second = int(seconds.get())
#     except:
#         second = 0
#         s.set(0)
#
#     clockTime = hour * 3600 + minute * 60 + second
#
#     lbl.place(relx=.5, rely=.1, anchor='n')
#
#     while clockTime > -1:
#
#         totalMin, totalSec = divmod(clockTime, 60)
#
#         totalHours = 0
#         if totalMin > 60:
#             totalHours, totalMin = divmod(totalMin, 60)
#
#         lbl.configure(text=f'{totalHours:02d}:{totalMin:02d}:{totalSec:02d}', font=("Arial Bold", 20))
#
#         if tre:
#             break
#
#         window.update()
#         time.sleep(1)
#
#         if clockTime == 0:
#             messagebox.showinfo('', 'Time is over!')
#
#         clockTime -= 1


def start_timer():
    try:
        hour = int(hours.get())
    except:
        hour = 0
        h.set(0)

    try:
        minute = int(minutes.get())
    except:
        minute = 0
        m.set(0)

    try:
        second = int(seconds.get())
    except:
        second = 0
        s.set(0)

    clockTime = hour * 3600 + minute * 60 + second

    lbl.place(relx=.5, rely=.1, anchor='n')

    # cd_id = ''

    def megdu():
        global cd_id
        nonlocal clockTime
        cd_id = window.after(1000, megdu)
        totalMin, totalSec = divmod(clockTime, 60)

        totalHours = 0
        if totalMin > 60:
            totalHours, totalMin = divmod(totalMin, 60)

        lbl.configure(text=f'{totalHours:02d}:{totalMin:02d}:{totalSec:02d}', font=("Arial Bold", 20))
        if clockTime == 0:
            window.after_cancel(cd_id)
            messagebox.showinfo('', 'Time is over!')

        clockTime -= 1

    megdu()



def stop():
    global cd_id
    window.after_cancel(cd_id)


window = Tk()
window.title("Timer")
window.geometry('400x300')
window.resizable(0, 0)

h = IntVar()
m = IntVar()
s = IntVar()


lbl = Label(window, text='Введите время таймера', font=("Arial Bold", 15), compound="center", background='orange')
lbl.place(relx=.5, rely=0, anchor='n')

# showTime = Label(window, text=, font=("Arial Bold", 15), compound="center", background='orange')
# showTime.place(relx=.5, rely=.15, anchor='n')

hours = Entry(width=15, textvariable=h)
hours.place(x=50, y=100)

minutes = Entry(width=15, textvariable=m)
minutes.place(x=150, y=100)

seconds = Entry(width=15, textvariable=s)
seconds.place(x=250, y=100)

btn = Button(window, text="Старт", font=("Arial Bold", 10), command=start_timer, compound='left', width=10)
btn.place(x=100, y=200)

stop_btn = Button(window, text="Стоп", font=("Arial Bold", 10), command=stop, compound='left', width=10)
stop_btn.place(x=200, y=200)



window.mainloop()
