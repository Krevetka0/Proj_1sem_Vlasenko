from tkinter import *
from tkinter.font import BOLD
root = Tk()
var = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
root.title('Обработка формы')
root.geometry('592x642')
Label(text="Форма регистрации пользователя", width=50, fg='black', font=('arial', 15, BOLD)).place(x=20, y=30)
Label(text="Ваше имя:", width=25, fg='black', font='arial 11').place(x=18, y=100)
Entry(width=25, bd=0, bg='#C0C0C0', font='arial 15').place(x=250, y=100)
Label(text="Пароль:", width=25, fg='black', font='arial 11').place(x=11, y=140)
Entry(width=25, bd=0, bg='#C0C0C0', font='arial 15').place(x=250, y=140)
Label(text="Возраст:", width=25, fg='black', font='arial 11').place(x=13, y=180)
Entry(width=25, bd=0, bg='#C0C0C0', font='arial 15').place(x=250, y=180)
Label(text="Пол:", width=25, fg='black', font='arial 11').place(x=0, y=220)
Radiobutton(root, text="Мужской", variable=var, value=1).place(x=245, y=220)
Radiobutton(root, text="Женский", variable=var, value=2).place(x=375, y=220)
Label(text="Ваши увлечения:", width=25, fg='black', font='arial 11').place(x=42, y=260)
Checkbutton(text="Музыка", variable=var1).place(x=245, y=260)
Checkbutton(text="Видео", variable=var2).place(x=350, y=260)
Checkbutton(text="Рисование", variable=var3).place(x=450, y=260)
Label(text="Ваша страна:", width=25, fg='black', font='arial 11').place(x=30, y=300)




root.mainloop()
