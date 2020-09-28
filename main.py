import tkinter
from tkinter import *
from settings import *
from func import *


app.title(TITLE)
app.minsize(width=WIDTH, height=HEIGHT)
app.maxsize(width=WIDTH, height=HEIGHT)


scroll = Scrollbar(app, orient='vertical', command=text.yview)

scroll.pack(side='right', fill='y')
text.configure(yscrollcommand=scroll.set)
text.pack()

menuBar = Menu(app)

app_menu = Menu(menuBar)

editor = Text_editor()

app_menu.add_command(label='Новый', command=editor.new_file)
app_menu.add_command(label='Открыть', command=editor.open_file)
app_menu.add_command(label='Сохранить', command=editor.save_file)
app_menu.add_command(label='Сохранить как', command=editor.save_as_file)

menuBar.add_cascade(label="Файл", menu=app_menu)
menuBar.add_cascade(label="Информация", command=editor.get_info)
menuBar.add_cascade(label="Выход", command=app.quit)

app.config(menu=menuBar)

app.mainloop()
