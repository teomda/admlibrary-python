import tkinter as tk
from tkinter import ttk, messagebox
from modulo.vista import Frame, create_menu
from ttkthemes import ThemedTk
from db.controller import setup_db

def main():
    setup_db()
    dialog = ThemedTk(theme="aquativo")
    dialog.title('Libreria')    
    dialog.tk.call("wm", "iconphoto", dialog._w, tk.PhotoImage(file="assets/favicon.png"))    
    dialog.resizable(False,False)    
    
    app = Frame(root=dialog)
    
    dialog.mainloop()

if __name__ == "__main__":
    main()
