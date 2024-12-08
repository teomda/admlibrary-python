import tkinter as tk
from tkinter import ttk, messagebox
from db.genre_repository import add_genre, get_genres, delete_genre, update_genre
from gui.shared_helpers import update_genre_combobox

def configure_genres_tab(tabGenres, inputBookGenre):
    selected_genre_id = None  # Para poder usarlo como flag al guardar.
    
    tabGenres.columnconfigure(0, weight=1)  # Permitir que la columna 0 se expanda
    tabGenres.columnconfigure(1, weight=3)  # Permitir que la columna 1 se expanda más

    def list_genres():         
        update_genre_combobox(inputBookGenre)
        for item in tree_genres.get_children():
            tree_genres.delete(item)
        
        list_of_genres = get_genres()
        for genre in list_of_genres:
            tree_genres.insert("", tk.END, values=(genre[0], genre[1], genre[2]))

    def cmd_addGenre(): 
        nombre = input_genreName.get().strip()
        descripcion = input_genreDescription.get().strip()
        
        if not (nombre and descripcion):
            messagebox.showwarning("Campos requeridos", "Debes completar todos los campos para agregar un género!")
            return
        
        if selected_genre_id is None: 
            add_genre(nombre, descripcion)
        else: 
            update_genre(selected_genre_id, nombre, descripcion)
        
        clear_fields()
        list_genres()

    def cmd_delete_genre():
        try:
            selected_item = tree_genres.selection()[0]
            selected_genre = tree_genres.item(selected_item)['values']
            idGenre = int(selected_genre[0])
            delete_genre(idGenre)
            tree_genres.delete(selected_item)
            clear_fields()
            list_genres()
        except IndexError:
            messagebox.showerror("Selección", "No se ha seleccionado ningún género.")       

    def cmd_edit_genre():
        nonlocal selected_genre_id  
        try:
            selected_item = tree_genres.selection()[0]
            selected_genre = tree_genres.item(selected_item)['values']
            selected_genre_id = int(selected_genre[0])  
            input_genreName.delete(tk.END)
            input_genreName.insert(tk.END, selected_genre[1])  
            input_genreDescription.delete(tk.END)
            input_genreDescription.insert(tk.END, selected_genre[2])              
        except IndexError:
            messagebox.showerror("Selección", "No se ha seleccionado ningún género.")

    def clear_fields():
        input_genreName.delete(0,tk.END)
        input_genreDescription.delete(0,tk.END)
        nonlocal selected_genre_id
        selected_genre_id = None

    ttk.Label(tabGenres, text="Nombre del género").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)    
    input_genreName = ttk.Entry(tabGenres)
    input_genreName.grid(row=0, column=1, padx=(7, 2), pady=5, ipadx=50)

    ttk.Label(tabGenres, text="Descripción del género").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    input_genreDescription = ttk.Entry(tabGenres)
    input_genreDescription.grid(row=1, column=1, padx=(7, 2), pady=5, ipadx=50)

    btn_addauthor = ttk.Button(tabGenres, text="Guardar", command=cmd_addGenre)
    btn_addauthor.grid(row=2, column=0, sticky=tk.W,padx=5)  

    btn_cancel = ttk.Button(tabGenres,text="Cancelar",command=clear_fields)  
    btn_cancel.grid(row=2,column=1, sticky=tk.E,padx=(10, 5))  

    ttk.Label(tabGenres, text="Listado de géneros").grid(row=3,columnspan=2,pady=(5), sticky=tk.W)

    # Tablita con géneros
    tree_genres = ttk.Treeview(tabGenres, columns=("ID", "Género", "Descripción"), show='headings')
    tree_genres.heading("ID", text="ID")
    tree_genres.heading("Género", text="Género", anchor=tk.W)
    tree_genres.heading("Descripción", text="Descripción", anchor=tk.W)
    
    tree_genres.grid(row=4,columnspan=2,pady=(5), sticky="ew")  # Ocupa dos columnas

    tree_genres.column("ID", width=30, anchor='center', stretch=False)
    tree_genres.column("Género", width=90, anchor='w', stretch=False)
    tree_genres.column("Descripción", minwidth=150,width=210)

    btn_edit = ttk.Button(tabGenres,text="Editar seleccionado",command=cmd_edit_genre,width=20)
    btn_edit.grid(row=5,column=0,pady=(3), sticky=tk.SW,padx=(5))

    btn_delete = ttk.Button(tabGenres,text="Eliminar seleccionado",command=cmd_delete_genre,width=20)
    btn_delete.grid(row=5,column=1,pady=(3), sticky=tk.SE,padx=(5))

    list_genres()