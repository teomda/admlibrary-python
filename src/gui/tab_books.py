import tkinter as tk
from tkinter import ttk, messagebox
from db.genre_repository import get_genres
from db.author_repository import get_authors
from gui.shared_helpers import update_genre_combobox,get_author_names,update_author_combobox, get_genres_names

def configure_books_tab(tabBooks):
    ttk.Label(tabBooks, text="Título del libro").pack(pady=(5, 2))
    input_bookTitle = tk.Text(tabBooks, height=1, width=30)
    input_bookTitle.pack()
    
    ttk.Label(tabBooks, text="Año publicación (numérico)").pack(pady=(5, 2))
    input_bookYear = tk.Entry(tabBooks, width=30)  # Usar Entry para el año
    input_bookYear.pack()

    ttk.Label(tabBooks, text="¿Disponible?").pack(pady=(5, 2))
    var_available = tk.BooleanVar()  # Variable para almacenar el estado
    check_available = tk.Checkbutton(tabBooks, text="Sí", variable=var_available)
    check_available.pack()
    
    # def get_author_names():
    #     list_authors = get_authors()
    #     return {author[1]: author[0] for author in list_authors}    
    
    # def update_author_combobox():
    #     author_names = get_author_names()
    #     inputBookAuthor['values'] = list(author_names.keys())
    #     inputBookAuthor.set('')

    ttk.Label(tabBooks, text="Autor").pack(pady=(7, 2))
    author_names = get_author_names()
    inputBookAuthor = ttk.Combobox(tabBooks, values=list(author_names.keys()), width=30)
    inputBookAuthor.pack() 
    
    # def get_genres_names():
    #     list_genres = get_genres()
    #     return {genre[1]: genre[0] for genre in list_genres}
    
    # def update_genre_combobox():
    #     genre_names = get_genres_names()
    #     inputBookGenre['values'] = list(genre_names.keys())
    #     inputBookGenre.set('')
    
    ttk.Label(tabBooks, text="Género").pack(pady=(7, 2))
    genre_names = get_genres_names()
    inputBookGenre = ttk.Combobox(tabBooks, values=list(genre_names.keys()), width=30)
    inputBookGenre.pack()

    def cmd_addBook():
        title = input_bookTitle.get("1.0", tk.END).strip()
        year = input_bookYear.get().strip()
        available = var_available.get()
                
        selected_author_name = inputBookAuthor.get()
        author_id = author_names[selected_author_name]
        
        selected_genre_name = inputBookGenre.get()        
        genre_id = genre_names[selected_genre_name]    
        
        print(f"Título: {title}, Año: {year}, Disponible: {available}, Autor ID: {author_id}, Género ID: {genre_id}")
        

    btn_addBook = ttk.Button(tabBooks, text="Agregar Libro", command=cmd_addBook)
    btn_addBook.pack(pady=(10, 0))
    
     # Tablita con géneros
    tree_books = ttk.Treeview(tabBooks, columns=("ID", "Title", "Author", "Genre", "Year","Avalible"), show='headings')
    tree_books.heading("ID", text="ID")
    tree_books.heading("Title", text="Titulo", anchor=tk.W)
    tree_books.heading("Author", text="Autor", anchor=tk.W)
    tree_books.heading("Genre", text="Género", anchor=tk.W)
    tree_books.heading("Year", text="Publicado", anchor=tk.W)
    tree_books.heading("Avalible", text="Disponible", anchor=tk.W)
    tree_books.pack(fill=tk.BOTH, expand=False, pady=2)
    tree_books.column("ID", width=30, anchor='center', stretch=False)
    tree_books.column("Title", width=90, anchor='w', stretch=False)
    tree_books.column("Author", width=90, anchor='w', stretch=False)
    tree_books.column("Genre", width=90, anchor='w', stretch=False)
    tree_books.column("Year", width=60, anchor='w')
    tree_books.column("Avalible",width=10)
    
    return inputBookGenre,inputBookAuthor