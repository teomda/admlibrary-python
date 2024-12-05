import tkinter as tk
from tkinter import ttk, messagebox
from db.genre_repository import add_genre, get_genres,delete_genre
from gui.shared_helpers import update_genre_combobox

def configure_genres_tab(tabGenres, inputBookGenre):
    
    def list_genres():         
        update_genre_combobox(inputBookGenre)
        for item in tree_genres.get_children():
            tree_genres.delete(item)
        
        list_genres = get_genres()
        for genre in list_genres:
            tree_genres.insert("", tk.END, values=(genre[0], genre[1], genre[2]))
            
    def cmd_addGenre():
        nombre = input_genreName.get("1.0", tk.END).strip()
        descripcion = input_genreDescription.get("1.0", tk.END).strip()
        if not (nombre and descripcion):
            messagebox.showwarning("Campos requeridos","Debes completar todos los campos para agregar un genero!")
            return
        add_genre(nombre, descripcion)
        input_genreName.delete("1.0", tk.END)
        input_genreDescription.delete("1.0", tk.END)
        list_genres()        
        
    def cmd_delete_genre():
        try:
            selected_item = tree_genres.selection()[0]
            selected_genre = tree_genres.item(selected_item)['values']
            idGenre = int(selected_genre[0])
            delete_genre(idGenre)
            tree_genres.delete(selected_item)
            list_genres()
        except IndexError:
            messagebox.showerror("Seleccion", "No se ha seleccionado ningún género.")
    
    ttk.Label(tabGenres, text="Nombre del género").pack(pady=(5, 2))    
    input_genreName = tk.Text(tabGenres, height=1, width=30)
    input_genreName.pack()
        
    ttk.Label(tabGenres, text="Descripción del género").pack(pady=(2, 2))
    input_genreDescription = tk.Text(tabGenres, height=3, width=20)
    input_genreDescription.pack(fill=tk.BOTH, expand=False)
    
    btn_addauthor = ttk.Button(tabGenres, text="Agregar género", command=cmd_addGenre)
    btn_addauthor.pack(pady=7)
    
    ttk.Label(tabGenres, text="Listado de géneros").pack(pady=(2, 2))

    # Tablita con géneros
    tree_genres = ttk.Treeview(tabGenres, columns=("ID", "Genre", "Descripción"), show='headings')
    tree_genres.heading("ID", text="ID")
    tree_genres.heading("Genre", text="Género", anchor=tk.W)
    tree_genres.heading("Descripción", text="Descripción", anchor=tk.W)
    tree_genres.pack(fill=tk.BOTH, expand=False, pady=2)
    tree_genres.column("ID", width=30, anchor='center', stretch=False)
    tree_genres.column("Genre", width=90, anchor='w', stretch=False)
    tree_genres.column("Descripción", minwidth=150, width=210)
    
    btn_delete = ttk.Button(tabGenres, text="Eliminar género", command=cmd_delete_genre)
    btn_delete.pack()
    
    list_genres()
    