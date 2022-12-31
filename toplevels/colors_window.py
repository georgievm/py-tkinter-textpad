from tkinter import Toplevel, Frame, Label, Button
from tkinter import colorchooser

class ColorsWindow():
    def __init__(self, app):
        self.app = app
        self.toplevel = Toplevel(app.master)
        self.toplevel.title('Adjust Colors')
        self.toplevel.iconbitmap(app.icon_path)

        main_fr = Frame(self.toplevel, padx=30, pady=10)
        main_fr.pack(expand=True, fill='both')

        Label(main_fr, text='Background').grid(row=0, column=0, sticky='W', pady=5)
        Label(main_fr, text='Foreground').grid(row=1, column=0, sticky='W', pady=5)
        Label(main_fr, text='Select Background').grid(row=2, column=0, pady=5)
        Label(main_fr, text='Select Foreground').grid(row=3, column=0, pady=5)

        self.bg_lbl = Label(main_fr, bg=app.config_data.get('Colors', 'background'), width=2)
        self.fg_lbl = Label(main_fr, bg=app.config_data.get('Colors', 'foreground'), width=2)
        self.bg_sel_lbl = Label(main_fr, bg=app.config_data.get('Colors', 'selectbackground'), width=2)
        self.fg_sel_lbl = Label(main_fr, bg=app.config_data.get('Colors', 'selectforeground'), width=2)

        self.bg_lbl.grid(row=0, column=1, padx=18)
        self.fg_lbl.grid(row=1, column=1, padx=18)
        self.bg_sel_lbl.grid(row=2, column=1, padx=18)
        self.fg_sel_lbl.grid(row=3, column=1, padx=18)

        self.pick0 = Button(main_fr, command=lambda: self.change_color(bg=self.pick_color()))
        self.pick1 = Button(main_fr, command=lambda: self.change_color(fg=self.pick_color()))
        self.pick2 = Button(main_fr, command=lambda: self.change_color(sel_bg=self.pick_color()))
        self.pick3 = Button(main_fr, command=lambda: self.change_color(sel_fg=self.pick_color()))

        for i in range(4):
            exec(f'self.pick{i}.grid(row={i}, column=2)')
            exec(f"self.pick{i}.config(text='Pick', relief='groove')")

        Button(self.toplevel, text='Reset All', command=self.reset, width=12, relief='groove').pack(side='left', padx=30, pady=10)
        Button(self.toplevel, text='OK', command=self.toplevel.destroy, width=5, relief='groove').pack(side='right', padx=30, pady=10)

    def pick_color(self):
        new_color = colorchooser.askcolor(title='New color')[1]
        return new_color

    def change_color(self, bg=None, fg=None, sel_bg=None, sel_fg=None):
        if bg:
            self.app.textbox.config(bg=bg)
            self.bg_lbl.config(bg=bg)
            self.app.config_data.set('Colors', 'background', bg)
        if fg:
            self.app.textbox.config(fg=fg)
            self.fg_lbl.config(bg=fg)
            self.app.config_data.set('Colors', 'foreground', fg)
        if sel_bg:
            self.app.textbox.config(selectbackground=sel_bg)
            self.bg_sel_lbl.config(bg=sel_bg)
            self.app.config_data.set('Colors', 'selectbackground', sel_bg)
        if sel_fg:
            self.app.textbox.config(selectforeground=sel_fg)
            self.fg_sel_lbl.config(bg=sel_fg)
            self.app.config_data.set('Colors', 'selectforeground', sel_fg)
        
        self.toplevel.focus()

    def reset(self):
        bg = self.app.config_data.get('DefaultColors', 'background')
        fg = self.app.config_data.get('DefaultColors', 'foreground')
        sel_bg = self.app.config_data.get('DefaultColors', 'selectbackground')
        sel_fg = self.app.config_data.get('DefaultColors', 'selectforeground')

        self.change_color(bg=bg, fg=fg, sel_bg=sel_bg, sel_fg=sel_fg)
    