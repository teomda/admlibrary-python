import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from db.controller import setup_db
# from gui.main_frame import Frame
from gui.menu import create_menu
from gui.tabs import create_tabs
from gui.tab_authors import configure_authors_tab
from gui.tab_genres import configure_genres_tab
from gui.tab_books import configure_books_tab

def main():
    setup_db()    
    # window = ThemedTk(theme="aquativo")
    window = ThemedTk(theme="breeze")
    window.title("Gestor de libros")
    window.geometry("600x520")
    window.tk.call("wm", "iconphoto", window._w, tk.PhotoImage(file="assets/favicon.png"))    
    window.resizable(False,False) 
     
    create_menu(window)
    # app = Frame(root=window)
    tabBooks, tabAuthors, tabGenres, tController = create_tabs(window)
        
    inputBookGenre,inputBookAuthor = configure_books_tab(tabBooks) # Retorno los combos para poder usarlos en tabGenres y Authors que son principales
    configure_genres_tab(tabGenres, inputBookGenre)
    configure_authors_tab(tabAuthors,inputBookAuthor)
    
    tController.select(tabBooks)
    
    window.mainloop()

if __name__ == "__main__":
    main()
