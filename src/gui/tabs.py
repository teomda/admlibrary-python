# gui/tabs.py
import tkinter as tk
from tkinter import ttk

def create_tabs(root):
    tController = ttk.Notebook(root)
    
    tabMain = ttk.Frame(tController)
    tabBooks = ttk.Frame(tController)
    tabAuthors = ttk.Frame(tController)
    tabGenres = ttk.Frame(tController)
    
    tController.add(tabGenres, text='Géneros')
    tController.add(tabAuthors, text='Autores')
    tController.add(tabBooks, text='Libros')
    tController.add(tabMain, text='Listado')
    tController.pack(expand=1, fill="both")

    # Asegúrate de devolver las pestañas
    return tabMain, tabBooks, tabAuthors, tabGenres

def add_tab(notebook, tab_frame, title):
    notebook.add(tab_frame, text=title)