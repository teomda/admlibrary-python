# src/main.py

import tkinter as tk
from tkinter import ttk, messagebox
from authors_funcs import add_author, get_authors
from dbp import setup_db

def main():
    setup_db()  # Por las dudas que no exista la base

    window = tk.Tk()
    window.title("Gestor de Biblioteca")
    window.geometry("600x300")
    tController = ttk.Notebook(window)
    tabMain = ttk.Frame(tController)
    tabBooks = ttk.Frame(tController)
    tabAuthors = ttk.Frame(tController)
    tabGenres = ttk.Frame(tController)    
    tController.add(tabMain, text='Listado')
    tController.add(tabBooks, text='Libros')
    tController.add(tabAuthors, text='Autores')
    tController.add(tabGenres, text='Generos')
    tController.pack(expand=1, fill="both")

    def cmd_addAuthor():
        nombre = input_name.get()
        nacionalidad = input_citizen.get()
        fecha_nacimiento = input_birthdate.get()
        if not (nombre and nacionalidad and fecha_nacimiento):
            messagebox.showwarning("Campos requeridos","Debes completar todos los campos para agregar un autor!")
            return
        add_author(nombre, nacionalidad, fecha_nacimiento)
        input_name.delete(0, tk.END)
        input_citizen.delete(0, tk.END)
        input_birthdate.delete(0, tk.END)
        list_authors()

    # # Función para mostrar autores
    def list_authors():
        list_authors = get_authors()
        listbox_authors.delete(0, tk.END)  # Limpiar la lista para recargarla
        for autor in list_authors:
            listbox_authors.insert(tk.END, f"{autor[1]} ({autor[2]})")

    # # Entradas para autores (tabAuthors)
    tk.Label(tabAuthors, text="Nombre autor:").pack()
    input_name = tk.Entry(tabAuthors)
    input_name.pack()

    tk.Label(tabAuthors, text="Nacionalidad:").pack(pady=(0,2))
    input_citizen = tk.Entry(tabAuthors)
    input_citizen.pack()

    tk.Label(tabAuthors, text="Fecha de Nacimiento:").pack(pady=(0,2))
    input_birthdate = tk.Entry(tabAuthors)
    input_birthdate.pack()

    # # Botón para agregar autor
    btn_addauthor = tk.Button(tabAuthors, text="Agregar Autor", command=cmd_addAuthor)
    btn_addauthor.pack(pady=7)

    # # Listbox para mostrar autores
    listbox_authors = tk.Listbox(tabAuthors)
    listbox_authors.pack(fill=tk.BOTH, expand=True,pady=5)

    list_authors()

    window.mainloop()

if __name__ == "__main__":
    main()
