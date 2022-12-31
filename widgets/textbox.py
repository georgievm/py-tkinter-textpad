from tkinter import Text
from datetime import datetime

class Textbox(Text):
    def __init__(self, app, **kwargs):
        self.app = app

        self.font_family = app.config_data.get('Font', 'family')
        self.font_size = app.config_data.get('Font', 'size')
        self.font_weight = app.config_data.get('Font', 'weight')
        self.font_slant = app.config_data.get('Font', 'slant')

        kwargs['bg'] = app.config_data.get('Colors', 'background')
        kwargs['fg'] = app.config_data.get('Colors', 'foreground')
        kwargs['selectbackground'] = app.config_data.get('Colors', 'selectbackground')
        kwargs['selectforeground'] = app.config_data.get('Colors', 'selectforeground')
        kwargs['bd'] = 0
        kwargs['undo'] = True
        kwargs['wrap'] = 'word'
        kwargs['tabs'] = '0.85c'
        super().__init__(app.master, **kwargs)
        self.update_font()

    def cut_text(self):
        if self.tag_ranges('sel'): # selected text is present
            self.event_generate('<<Cut>>')
            self.app.statusbar.print('CUT')
    
    def copy_text(self):
        if self.tag_ranges('sel'):
            self.event_generate('<<Copy>>')
            self.app.statusbar.print('COPIED')
    
    def paste_text(self):
        self.event_generate('<<Paste>>')
        self.app.statusbar.print('PASTED')
    
    def delete_text(self):
        if self.tag_ranges('sel'):
            self.delete('sel.first', 'sel.last')
            self.app.statusbar.print('DELETED')
    
    def select_all(self):
        self.tag_add('sel', 1.0, 'end')
    
    def insert_time(self):
        local_time = datetime.now().strftime('%X %b %d %Y')

        # delete selected text if present
        if self.tag_ranges('sel'):
            self.delete('sel.first', 'sel.last')
        
        cursor_pos = self.index('insert')
        self.insert(cursor_pos, local_time)
        self.app.statusbar.print('LOCAL TIME')

    def toggle_wrap(self):
        if self.cget('wrap') == 'word':
            self.config(wrap='none')
            self.app.statusbar.print('WRAP: NONE')
            # add horizontal scrollbar
            self.h_scrollbar.pack(side='bottom', fill='x')
        else:
            self.config(wrap='word')
            self.app.statusbar.print('WRAP: WORD')
            # remove horizontal scrollbar
            self.h_scrollbar.pack_forget()
    
    def update_font(self):
        self.config(font=(self.font_family, self.font_size, self.font_weight, self.font_slant))
    
    def change_size(self, by_num):
        self.font_size = str(int(self.font_size) + by_num)
        self.update_font()
        self.app.config_data.set('Font', 'size', self.font_size)
    