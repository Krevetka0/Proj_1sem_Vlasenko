import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#FFDAB9', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="PZ_16/11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить книгу', command=self.open_dialog, bg='#FFEFD5', bd=0,
                                         compound=tk.TOP, image=self.add_img, width=90)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="PZ_16/12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#FFEFD5',
                                    bd=0, compound=tk.TOP, image=self.update_img, width=90)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="PZ_16/13.gif")
        btn_search_dialog = tk.Button(toolbar, text="Поиск", command=self.open_search_dialog, bg='#FFEFD5',
                                      bd=0, compound=tk.TOP, image=self.search_img, width=90)
        btn_search_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="PZ_16/14.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#FFEFD5',
                               bd=0, compound=tk.TOP, image=self.delete_img, width=90)
        btn_delete.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="PZ_16/15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#FFEFD5',
                                bd=0, compound=tk.TOP, image=self.refresh_img, width=90)
        btn_refresh.pack(side=tk.LEFT)
        self.tree = ttk.Treeview(self, columns=('books_id', 'genre', 'country', 'series', 'author', 'name', 'year',
                                                'annotation'), height=15, show='headings')

        self.tree.column('books_id', width=40, anchor=tk.CENTER)
        self.tree.column('genre', width=120, anchor=tk.CENTER)
        self.tree.column('country', width=120, anchor=tk.CENTER)
        self.tree.column('series', width=70, anchor=tk.CENTER)
        self.tree.column('author', width=120, anchor=tk.CENTER)
        self.tree.column('name', width=120, anchor=tk.CENTER)
        self.tree.column('year', width=70, anchor=tk.CENTER)
        self.tree.column('annotation', width=240, anchor=tk.CENTER)

        self.tree.heading('books_id', text='ID')
        self.tree.heading('genre', text='Жанр')
        self.tree.heading('country', text='Страна')
        self.tree.heading('series', text='Серия')
        self.tree.heading('author', text='Автор')
        self.tree.heading('name', text='Название')
        self.tree.heading('year', text='Год')
        self.tree.heading('annotation', text='Аннотация')

        self.tree.pack()

    def records(self, books_id, genre, country, series, author, name, year, annotation):
        self.db.insert_data(books_id, genre, country, series, author, name, year, annotation)
        self.view_records()

    def update_record(self, books_id, genre, country, series, author, name, year, annotation):
        self.db.cur.execute("""UPDATE books SET books_id=?, genre=?, country=?, series=?, author=?, name=?,
         year=?, annotation=? WHERE books_id=?""", (books_id, genre, country, series, author, name, year, annotation,
                                                    self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM books""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def search_records(self, genre):
        genre = (genre,)
        self.db.cur.execute("""SELECT * FROM books WHERE genre=?""", genre)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM books WHERE books_id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):

    """"Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить книгу')
        self.geometry('400x300+500+250')
        self.resizable(False, False)

        label_number = tk.Label(self, text='Номер')
        label_number.place(x=50, y=25)
        self.entry_number = ttk.Entry(self)
        self.entry_number.place(x=150, y=25)

        label_genre = tk.Label(self, text='Жанр')
        label_genre.place(x=50, y=50)
        self.combobox = ttk.Combobox(self, values=[u'Детектив', u'Приключения', u'Фантастика', u'Роман', u'Комедия',
                                                   u'Драма', u'Фольклор'])
        self.combobox.current(0)
        self.combobox.place(x=150, y=50)

        label_country = tk.Label(self, text='Страна')
        label_country.place(x=50, y=75)
        self.entry_country = ttk.Entry(self)
        self.entry_country.place(x=150, y=75)

        label_series = tk.Label(self, text='Серия')
        label_series.place(x=50, y=100)
        self.entry_series = ttk.Entry(self)
        self.entry_series.place(x=150, y=100)

        label_author = tk.Label(self, text='Автор')
        label_author.place(x=50, y=125)
        self.entry_author = ttk.Entry(self)
        self.entry_author.place(x=150, y=125)

        label_name = tk.Label(self, text='Название')
        label_name.place(x=50, y=150)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=150, y=150)

        label_year = tk.Label(self, text='Год')
        label_year.place(x=50, y=175)
        self.entry_year = ttk.Entry(self)
        self.entry_year.place(x=150, y=175)

        label_annot = tk.Label(self, text='Аннотация')
        label_annot.place(x=50, y=200)
        self.entry_annot = ttk.Entry(self)
        self.entry_annot.place(x=150, y=200)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=250)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=210, y=250)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_number.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_country.get(),
                                                                       self.entry_series.get(),
                                                                       self.entry_author.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_year.get(),
                                                                       self.entry_annot.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=250)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_number.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_country.get(),
                                                                          self.entry_series.get(),
                                                                          self.entry_author.get(),
                                                                          self.entry_name.get(),
                                                                          self.entry_year.get(),
                                                                          self.entry_annot.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Поиск по жанру")
        self.geometry('300x150')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=50)

        self.entry_search = ttk.Entry(self, width=25)
        self.entry_search.place(x=100, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=100, y=100)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=180, y=100)


class DB:
    def __init__(self):

        with sq.connect('PZ_16/library.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS books (
                books_id INTEGER PRIMARY KEY AUTOINCREMENT,
                genre TEXT NOT NULL,
                country TEXT NOT NULL,
                series INTEGER,
                author TEXT NOT NULL,
                name TEXT NOT NULL,
                year INTEGER,
                annotation TEXT NOT NULL
                )""")

    def insert_data(self, books_id, genre, country, series, author, name, year, annotation):
        self.cur.execute("""INSERT INTO books(books_id, genre, country, series, author, name,
        year, annotation) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (books_id, genre, country, series, author, name,
                                                               year, annotation))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Библиотека")
    root.geometry("900x400+400+200")
    root.resizable(False, False)
    root.mainloop()
