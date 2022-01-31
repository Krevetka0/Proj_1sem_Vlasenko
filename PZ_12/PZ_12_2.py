from tkinter import *
root = Tk()
root.title('Цвет излучения')
root.geometry('600x300')
Label(text='Эта программа показывает цвет излучения в зависимости от длины волны',
      width=65, fg='black', font='arial 11').place(x=1, y=15)
Label(text='Введите длину волны:', width=20, fg='black', font='arial 11').place(x=23, y=100)
A = Entry().place(x=300, y=101)
Label(text='Цвет данной волны:', width=20, fg='black', font='arial 11').place(x=18, y=200)
b1 = Button(root, text='Посчитать!', fg='black', font='arial 11').place(x=250, y=140)

root.mainloop()
