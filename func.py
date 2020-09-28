import webbrowser
import codecs
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename,asksaveasfilename
from tkinter import messagebox
from tkinter.messagebox import askyesno, showerror
from settings import *


app = Tk()
text = Text(app, width=WIDTH-100, height=HEIGHT, wrap='word')

class Text_editor():
    def __init__(self):
        self.file_name = tkinter.NONE

    def new_file(self):
        self.file_name = 'Безымянный'
        text.delete('1.0', tkinter.END)


    def open_file(self):
        inp = askopenfilename()
        if inp == '':
            return
        with codecs.open(inp, encoding="utf-8") as file:
            data = file.read()
            text.delete('1.0', tkinter.END)
            text.insert('1.0', data)

    def save_file(self):
        name_save_file = 'Безымянный'
        data = text.get('1.0', tkinter.END)
        output = open(name_save_file, 'w', encoding="utf-8")
        output.write(data)
        output.close()

    def save_as_file(self):
        output = asksaveasfile(mode='w', defaultextension='txt')
        data = text.get('1.0', tkinter.END)
        try:
            output.write(data.rstrip())
        except Exception:
            showerror(title='Ошибка!', message='Невозможно сохранить файл')

    def get_info(self):
        message = askyesno('Справка','Это текстовый редактор v 1.0\nМой github:\nhttps://github.com/NikolayTolkovanov?tab=repositories\nПерейти по ссылке? ')
        if message == True:
            webbrowser.open('https://github.com/NikolayTolkovanov?tab=repositories',new=2)