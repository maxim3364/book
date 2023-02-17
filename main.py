from tkinter import *
import mysql.connector as mysql
from tkinter import ttk

db= mysql.connect(host='localhost', user='root', password='112233445566778899Oo', database='fff')
mycursor = db.cursor()

root = Tk()
root.geometry ('800x800')


id = Label(root, text='Номер')
book = Label(root, text='Название книги')
author = Label(root, text='Автор')
Year_of_publication = Label(root, text='Год выпуска издания')


id.grid(row=1, column=2)
book.grid(row=2, column=2)
author.grid(row=3, column=2)
Year_of_publication.grid(row=4, column=2)


e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)


e1.grid(row=1, column=3)
e2.grid(row=2, column=3)
e3.grid(row=3, column=3)
e4.grid(row=4, column=3)


def Add():
        id = e1.get()
        book = e2.get()
        author = e3.get()
        Year_of_publication = e4.get()


        sql = 'INSERT INTO ccc (id, book, author, Year_of_publication) VALUES(%s,%s,%s,%s)'
        value = (id, book, author, Year_of_publication)
        mycursor.execute(sql, value)
        db.commit()

def Edit():
        id = e1.get()
        book = e2.get()
        author = e3.get()
        Year_of_publication = e4.get()

        sql = 'update ccc set book=%s, author=%s, Year_of_publication=%s, where id=%s'
        value = (book, author, Year_of_publication, id)
        mycursor.execute(sql, value)
        db.commit()


Button(root, text ='Добавить', command=Add, height=3, width=10).place(x=100, y=450)
Button(root, text ='Изменить', command=Edit, height=3, width=10).place(x=200, y=450)
Button(root, text ='Удалить', command='', height=3, width=10).place(x=300, y=450)


column1 = ('id', 'book', 'author', 'Year_of_publication',)
listbox = ttk.Treeview(root, columns=column1,show='headings')

for col in column1:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=2)
        listbox.place(x=15, y=150)

root.mainloop()