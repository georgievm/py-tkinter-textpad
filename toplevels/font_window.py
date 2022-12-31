import tkinter as tk
from tkinter import font

class FontWindow():
    def __init__(self, app):
        self.app = app
        self.toplevel = tk.Toplevel(app.master)
        self.toplevel.title('Adjust Font')
        self.toplevel.iconbitmap(app.icon_path)

        # StringVars
        global font_family
        global font_size
        global font_weight
        global font_slant
        font_family = tk.StringVar(value=app.config_data.get('Font', 'family'))
        font_size = tk.StringVar(value=app.config_data.get('Font', 'size'))
        font_weight = tk.StringVar(value=app.config_data.get('Font', 'weight'))
        font_slant = tk.StringVar(value=app.config_data.get('Font', 'slant'))
        
        main_fr = tk.Frame(self.toplevel, padx=20, pady=20)
        main_fr.pack(expand=True, fill='both')

        # Font family
        self.all_families = font.families()
        family_ind = self.get_family_index(font_family.get())

        tk.Label(main_fr, text='Family:').grid(row=0, column=0, sticky='w')

        family_fr = tk.Frame(main_fr)
        family_fr.grid(row=1, column=0)

        self.family_list = tk.Listbox(family_fr)
        self.family_list.pack(side='left')
        for i, f in enumerate(self.all_families):
            self.family_list.insert(i+1, f)
        
        family_scr = tk.Scrollbar(family_fr, command=self.family_list.yview)
        family_scr.pack(side='right', fill='y')
        self.family_list.config(yscrollcommand=family_scr.set)
        
        self.family_list.selection_set(family_ind)
        self.family_list.see(family_ind)
        self.family_list.bind("<<ListboxSelect>>", lambda e: self.change_font(family=(self.family_list.get(self.family_list.curselection()))))

        sec_fr = tk.Frame(main_fr)
        sec_fr.grid(row=0, column=1, rowspan=2, padx=15, sticky='n')

        # Font size
        tk.Label(sec_fr, text='Size:').pack(anchor='w')
        self.size_box = tk.Spinbox(sec_fr, width=10, from_=1, to=100, textvariable=font_size, command=lambda: self.change_font(size=font_size.get()))
        self.size_box.pack()

        # Font weight
        self.bold_chb = tk.Checkbutton(sec_fr, text='Bold')
        self.bold_chb.config(onvalue='bold', offvalue='normal', variable=font_weight, command=lambda: self.change_font(weight=font_weight.get()))
        self.bold_chb.pack(pady=5)

        # Font slant
        self.italic_chb = tk.Checkbutton(sec_fr, text='Italic')
        self.italic_chb.config(onvalue='italic', offvalue='roman', variable=font_slant, command=lambda: self.change_font(slant=font_slant.get()))
        self.italic_chb.pack()

        tk.Button(sec_fr, text='OK', width=10, relief='groove', command=self.toplevel.destroy).pack(pady=15.5)
        tk.Button(sec_fr, text='Reset All', width=10, relief='groove', command=self.reset).pack()
    
    def get_family_index(self, name):
        return self.all_families.index(name)
    
    def change_font(self, family=None, size=None, weight=None, slant=None):
        global font_family, font_size, font_weight, font_slant

        if family:
            # update listbox to show current
            font_family.set(family)
            family_ind = self.get_family_index(family)
            self.family_list.select_clear(0, 'end')
            self.family_list.selection_set(family_ind)
            self.family_list.see(family_ind)

            self.app.textbox.font_family = family
            self.app.config_data.set('Font', 'family', family)
        if size:
            font_size.set(size)
            self.app.textbox.font_size = size
            self.app.config_data.set('Font', 'size', size)
        if weight:
            font_weight.set(weight)
            self.app.textbox.font_weight = weight
            self.app.config_data.set('Font', 'weight', weight)
        if slant:
            font_slant.set(slant)
            self.app.textbox.font_slant = slant
            self.app.config_data.set('Font', 'slant', slant)
        
        self.app.textbox.update_font()
        self.toplevel.focus()

    def reset(self):
        family = self.app.config_data.get('DefaultFont', 'family')
        size = self.app.config_data.get('DefaultFont', 'size')
        weight = self.app.config_data.get('DefaultFont', 'weight')
        slant = self.app.config_data.get('DefaultFont', 'slant')

        self.change_font(family=family, size=size, weight=weight, slant=slant)
    