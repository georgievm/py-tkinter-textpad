from tkinter import Label

class Statusbar(Label):
    def __init__(self, master, **kwargs):
        kwargs['text'] = '-'
        kwargs['anchor'] = 'w'
        kwargs['padx'] = 5
        kwargs['pady'] = 1
        super().__init__(master, **kwargs)
    
    def print(self, message):
        self.config(text=message)
        self.after(2000, lambda: self.config(text='-'))