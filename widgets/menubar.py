from tkinter import Menu, BooleanVar
import webbrowser

class Menubar():
    def __init__(self, app):
        self.menubar = Menu(app.master)
        app.master.config(menu=self.menubar)

        # Create menus
        file_menu = Menu(self.menubar, tearoff=0)
        edit_menu = Menu(self.menubar, tearoff=0)
        format_menu = Menu(self.menubar, tearoff=0)
        options_menu = Menu(self.menubar, tearoff=0)
        help_menu = Menu(self.menubar, tearoff=0)

        # Add cascades
        self.menubar.add_cascade(label="File", menu=file_menu)
        self.menubar.add_cascade(label="Edit", menu=edit_menu)
        self.menubar.add_cascade(label="Format", menu=format_menu)
        self.menubar.add_cascade(label="Options", menu=options_menu)
        self.menubar.add_cascade(label="Help", menu=help_menu)

        # Add menu items
        file_menu.add_command(label="New File", command=app.new_file, accelerator='(Ctrl+N)')
        file_menu.add_command(label="Open...", command=app.open_file, accelerator='(Ctrl+O)')
        file_menu.add_command(label="Save", command=app.save_file, accelerator='(Ctrl+S)')
        file_menu.add_command(label="Save As", command=app.save_file_as, accelerator='(Ctrl+Shift+S)')
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=app.on_close)

        edit_menu.add_command(label="Undo", command=app.textbox.edit_undo, accelerator='(Ctrl+Z)')
        edit_menu.add_command(label="Redo", command=app.textbox.edit_redo, accelerator='(Ctrl+Y)')
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=app.textbox.cut_text, accelerator='(Ctrl+X)')
        edit_menu.add_command(label="Copy", command=app.textbox.copy_text, accelerator='(Ctrl+C)')
        edit_menu.add_command(label="Paste", command=app.textbox.paste_text, accelerator='(Ctrl+V)')
        edit_menu.add_command(label="Delete", command=app.textbox.delete_text, accelerator='(Del)')
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=app.textbox.select_all, accelerator='(Ctrl+A)')
        edit_menu.add_command(label="Time/Date", command=app.textbox.insert_time, accelerator='(F5)')

        format_menu.add_command(label='Font...', command=app.open_font_window)
        format_menu.add_separator()
        format_menu.add_command(label='Colors...', command=app.open_colors_window)
        
        app.textbox.word_wrap = BooleanVar(value=True)
        options_menu.add_checkbutton(label='Word Wrap', variable=app.textbox.word_wrap, command=app.textbox.toggle_wrap)
        options_menu.add_separator()

        app.autosave_var = BooleanVar(value=app.config_data.get('AutoSave', 'state'))
        options_menu.add_checkbutton(label='AutoSave', variable=app.autosave_var, command=app.change_autosave, onvalue=True, offvalue=False)

        help_menu.add_command(label='View Shortcuts', command=app.view_shortcuts, accelerator='(F1)')
        help_menu.add_separator()
        help_menu.add_command(label='View Project on GitHub', command=lambda: webbrowser.open('https://github.com/georgievm/py-tkinter-textpad'))