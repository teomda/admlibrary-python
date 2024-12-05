import tkinter as tk
from tkinter import messagebox

def create_menu(root):
    def cmd_show_about():
        messagebox.showinfo("Acerca de", "-- Gestor de libros --\nCreado por Teo Madariaga, para nuestro Gurú! \nGracias Gabriel ! \nVersión 1.0B1")
    
    def cmd_exit_app():
        root.quit() 
        
    menu_bar = tk.Menu(root)
    
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Salir", command=cmd_exit_app)
    menu_bar.add_cascade(label="Archivo", menu=file_menu)

    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="Acerca de", command=cmd_show_about)
    menu_bar.add_cascade(label="Ayuda", menu=help_menu)

    root.config(menu=menu_bar)