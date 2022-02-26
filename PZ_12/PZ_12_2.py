from tkinter import *


def count_num(event):
    a = int(num1.get())
    if a <= 450:
        positive['text'] = 'Цвет излучения ~фиолетовый~'
    elif 450 < a <= 480:
        positive['text'] = 'Цвет излучения ~синий~'
    elif 480 < a <= 510:
        positive['text'] = 'Цвет излучения ~сине-зеленый~'
    elif 510 < a <= 550:
        positive['text'] = 'Цвет излучения ~зеленый~'
    elif 550 < a <= 570:
        positive['text'] = 'Цвет излучения ~желто-зеленый~'
    elif 570 < a <= 590:
        positive['text'] = 'Цвет излучения ~желтый~'
    elif 590 < a <= 630:
        positive['text'] = 'Цвет излучения ~оранжевый~'
    elif a >= 630:
        positive['text'] = 'Цвет излучения ~красный~'


root = Tk()
root.title("Цвет волны излучения")
root.geometry("400x100")

Label(text="Введите длину волны:").grid(row=1, column=0)
num1 = Entry()
num1.grid(row=1, column=1)

button1 = Button(text="Найти цвет!")
button1.grid(row=4, column=1)

positive = Label()
positive.grid(row=5, column=1)

button1.bind('<Button-1>', count_num)

root.mainloop()
