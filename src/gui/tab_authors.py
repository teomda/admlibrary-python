import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from tkcalendar import DateEntry
from db.author_repository import add_author, get_authors, delete_author, update_author 
from constants.paises import paises
from gui.shared_helpers import update_author_combobox

def configure_authors_tab(tabAuthors, inputBookAuthor):
    selected_author_id = None  
    tabAuthors.columnconfigure(0, weight=1) 
    tabAuthors.columnconfigure(1, weight=3)

    def cmd_delete_author():
        try:
            selected_item = tree_authors.selection()[0]
            selected_author = tree_authors.item(selected_item)['values']
            idAuthor = int(selected_author[0])
            delete_author(idAuthor)
            tree_authors.delete(selected_item)
            list_authors()
        except IndexError:
            messagebox.showerror("Selección", "No se ha seleccionado ningún autor.")

    def cmd_add_author():
        nombre = input_name.get().strip()
        nacionalidad = input_citizen.get()
        fecha_nacimiento = input_birthdate.get()
        
        if not (nombre and nacionalidad and fecha_nacimiento):
            messagebox.showwarning("Campos requeridos", "Debes completar todos los campos para agregar un autor!")
            return
        
        if selected_author_id is None:  
            add_author(nombre, nacionalidad, fecha_nacimiento)
        else:  
            update_author(selected_author_id, nombre, nacionalidad, fecha_nacimiento)

        clear_fields()  
        list_authors()  

    def list_authors():
        update_author_combobox(inputBookAuthor)
        for item in tree_authors.get_children():
            tree_authors.delete(item)
        
        authors = get_authors()
        for author in authors:
            tree_authors.insert("", tk.END, values=(author[0], author[1], author[2], author[3]))

    def cmd_edit_author():
        nonlocal selected_author_id  
        try:
            selected_item = tree_authors.selection()[0]
            selected_author = tree_authors.item(selected_item)['values']
            selected_author_id = int(selected_author[0])
            input_name.delete(0, tk.END)
            input_name.insert(tk.END, selected_author[1])
            input_citizen.set(selected_author[2])
            input_birthdate.set_date(selected_author[3])
        except IndexError:
            messagebox.showerror("Selección", "No se ha seleccionado ningún autor.")

    def clear_fields():
        input_name.delete(0, tk.END)
        input_citizen.set('')  
        input_birthdate.set_date(date.today())  
        nonlocal selected_author_id
        selected_author_id = None  

    ttk.Label(tabAuthors, text="Nombre autor:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    input_name = ttk.Entry(tabAuthors)
    input_name.grid(column=1, row=0, sticky=tk.W, padx=(7,2), pady=5,ipadx=50)


    ttk.Label(tabAuthors, text="Nacionalidad:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    input_citizen = ttk.Combobox(tabAuthors, values=paises, width=50, height=10, justify='center')
    input_citizen.grid(column=1, row=1, sticky=tk.W, padx=(7,2), pady=5)
    
    input_citizen.current(0)

    ttk.Label(tabAuthors, text="Fecha de Nacimiento:").grid(row=2, column=0, padx=5, pady=(7, 2), sticky=tk.W)
    input_birthdate = DateEntry(
        tabAuthors, width=25, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy'
    )
    input_birthdate.grid(column=1, row=2, sticky=tk.W, pady=(7,2), padx=5)    
    
    btn_add_author = ttk.Button(tabAuthors, text="Guardar", command=cmd_add_author)
    btn_add_author.grid(row=3, column=0, sticky=tk.W,padx=5)  

    btn_cancel = ttk.Button(tabAuthors,text="Cancelar",command=clear_fields)  
    btn_cancel.grid(row=3,column=1, sticky=tk.E,padx=5)  

    tree_authors = ttk.Treeview(tabAuthors, columns=("ID", "Author", "Country", "Year"), show='headings')
    tree_authors.heading("ID", text="ID")
    tree_authors.heading("Year", text="Año", anchor=tk.W)
    tree_authors.heading("Author", text="Autor", anchor=tk.W)
    tree_authors.heading("Country", text="País", anchor=tk.W)
    
    tree_authors.grid(row=4,columnspan=2,pady=(5), sticky="ew", rowspan=1)

    tree_authors.column("ID", width=30, anchor='center', stretch=False)
    tree_authors.column("Year", width=60, anchor='w')
    tree_authors.column("Author", minwidth=100,width=120)
    tree_authors.column("Country", minwidth=100,width=120)

    btn_edit = ttk.Button(tabAuthors,text="Editar seleccionado",command=cmd_edit_author,width=20)
    btn_edit.grid(row=6, column=0, sticky=tk.SW,padx=5)
    
    btn_delete = ttk.Button(tabAuthors,text="Eliminar seleccionado",command=cmd_delete_author,width=20)
    btn_delete.grid(row=6, column=1, sticky=tk.SE,padx=5)


    list_authors()
