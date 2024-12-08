from tkinter import ttk

def create_tabs(root):
    tController = ttk.Notebook(root)
    
    tabBooks = ttk.Frame(tController)
    tabAuthors = ttk.Frame(tController)
    tabGenres = ttk.Frame(tController)
    
    tController.add(tabBooks, text='Libros')    
    tController.add(tabAuthors, text='Autores')
    tController.add(tabGenres, text='Géneros')
    tController.pack(expand=1, fill="both")

    return tabBooks, tabAuthors, tabGenres, tController

def add_tab(notebook, tab_frame, title):
    notebook.add(tab_frame, text=title)