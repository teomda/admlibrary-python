import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from db.author_repository import add_author, get_authors, delete_author
from constants.paises import paises
from gui.shared_helpers import update_author_combobox

def configure_authors_tab(tabAuthors,inputBookAuthor):
    
    def cmd_delete_author():
        try:
            selected_item = tree_authors.selection()[0]
            selected_author = tree_authors.item(selected_item)['values']
            idAuthor = int(selected_author[0])
            delete_author(idAuthor)
            tree_authors.delete(selected_item)
            list_authors()
        except IndexError:
            messagebox.showerror("Seleccion", "No se ha seleccionado ningún autor.")

    def cmd_add_author():
        nombre = input_name.get("1.0", tk.END).strip()
        nacionalidad = input_citizen.get()
        fecha_nacimiento = input_birthdate.get()
        if not (nombre and nacionalidad and fecha_nacimiento):
            messagebox.showwarning("Campos requeridos", "Debes completar todos los campos para agregar un autor!")
            return
        add_author(nombre, nacionalidad, fecha_nacimiento)
        input_name.delete("1.0", tk.END)
        input_citizen.delete(0, tk.END)
        input_birthdate.delete(0, tk.END)
        list_authors()

    def list_authors():
        update_author_combobox(inputBookAuthor)
        for item in tree_authors.get_children():
            tree_authors.delete(item)
        authors = get_authors()
        for author in authors:
            tree_authors.insert("", tk.END, values=(author[0], author[1], author[2], author[3]))

    ttk.Label(tabAuthors, text="Nombre autor:").pack(pady=(7, 2))
    input_name = tk.Text(tabAuthors, height=1, width=30)
    input_name.pack()

    ttk.Label(tabAuthors, text="Nacionalidad:").pack(pady=(7, 2))
    input_citizen = ttk.Combobox(tabAuthors, values=paises, width=30, height=10, justify='center')
    input_citizen.pack()
    input_citizen.current(0)

    ttk.Label(tabAuthors, text="Fecha de Nacimiento:").pack(pady=(7, 2))
    input_birthdate = DateEntry(
        tabAuthors, width=25, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy'
    )
    input_birthdate.pack()

    btn_add_author = ttk.Button(tabAuthors, text="Agregar Autor", command=cmd_add_author, width=20)
    btn_add_author.pack(pady=7)

    tree_authors = ttk.Treeview(tabAuthors, columns=("ID", "Author", "Country", "Year"), show='headings')
    tree_authors.heading("ID", text="ID")
    tree_authors.heading("Year", text="Año", anchor=tk.W)
    tree_authors.heading("Author", text="Autor", anchor=tk.W)
    tree_authors.heading("Country", text="País", anchor=tk.W)
    tree_authors.pack(fill=tk.BOTH, expand=False, pady=5)
    tree_authors.column("ID", width=30, anchor='center', stretch=False)
    tree_authors.column("Year", width=60, anchor='w')
    tree_authors.column("Author", minwidth=100, width=120)
    tree_authors.column("Country", minwidth=100, width=120)

    btn_delete = ttk.Button(tabAuthors, text="Eliminar Autor", command=cmd_delete_author, width=20)
    btn_delete.pack(pady=(3, 0))
    
    list_authors()
