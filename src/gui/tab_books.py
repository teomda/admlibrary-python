import tkinter as tk
from tkinter import ttk, messagebox
from gui.shared_helpers import get_author_names, get_genres_names,update_author_combobox,update_genre_combobox
from db.books_repository import add_book, update_book, delete_book,get_books
from datetime import datetime

def configure_books_tab(tabBooks):
    selected_book_id = None
    author_names = get_author_names()
    genre_names = get_genres_names()
    yearnow = datetime.now().year
    
    tabBooks.columnconfigure(0, weight=1)
    tabBooks.columnconfigure(1, weight=3)
    
    def refresh_combos():
        nonlocal author_names
        author_names = get_author_names()
        nonlocal genre_names
        genre_names = get_genres_names()
    
    def list_books():
        for item in tree_books.get_children():
            tree_books.delete(item)
        
        books = get_books()
        for book in books:            
            author_id = book[2]  
            genre_id = book[3]   
            author_name = next((name for name, id in author_names.items() if id == author_id), "Desconocido")
            genre_name = next((name for name, id in genre_names.items() if id == genre_id), "Desconocido")
            available_str = "Sí" if book[5] else "No"
            tree_books.insert("", tk.END, values=(book[0], book[1], author_name, genre_name, book[4], available_str,book[2],book[3]))            
        
    def cmd_saveBook():
        nonlocal selected_book_id 
        refresh_combos()
        title = input_bookTitle.get().strip()
        year = input_bookYear.get().strip()
        available = var_available.get()        
        selected_author_name = inputBookAuthor.get()        
        selected_genre_name = inputBookGenre.get()        
        
        if not all([title, year, selected_author_name, selected_genre_name]):
            messagebox.showerror("Error", "Por favor, complete todos los campos")
            return
    
        genre_id = genre_names[selected_genre_name]    
        author_id = author_names[selected_author_name]
        
        if selected_book_id is None:
            add_book(title, author_id, genre_id, year, available)            
        else:
            update_book(selected_book_id, title, author_id, genre_id, year, available)        
        clear_fields()
        list_books()

    def cmd_editBook():
        nonlocal selected_book_id  
        try:
            selected_item = tree_books.selection()[0]
            selected_book = tree_books.item(selected_item)['values']
            selected_book_id = int(selected_book[0])
            input_bookTitle.delete(0, tk.END)
            input_bookTitle.insert(tk.END, selected_book[1])
            input_bookYear.delete(0, tk.END)
            input_bookYear.insert(0, selected_book[4])
            var_available.set(selected_book[5] == "Sí")
            inputBookAuthor.set(selected_book[2])
            inputBookGenre.set(selected_book[3])
        except IndexError:
            messagebox.showerror("Selección", "No se ha seleccionado ningún libro.")

    def cmd_deleteBook():
        try:
            selected_item = tree_books.selection()[0]                
            selected_book = tree_books.item(selected_item)['values']
            selected_book_idref = int(selected_book[0])            
            delete_book(selected_book_idref)
            tree_books.delete(selected_item)
            clear_fields()
            list_books()
          
        except IndexError:
            messagebox.showerror("Selección", "No se ha seleccionado ningún libro.")

    def clear_fields():
        input_bookTitle.delete(0, tk.END)
        input_bookYear.delete(0, tk.END)
        var_available.set(False)
        inputBookAuthor.set('')
        inputBookGenre.set('')  
        nonlocal selected_book_id
        selected_book_id = None  
    
    ttk.Label(tabBooks, text="Título del libro").grid(row=0, column=0, padx=5, pady=(5, 2), sticky=tk.W)    
    input_bookTitle = ttk.Entry(tabBooks)
    input_bookTitle.grid(row=0, column=1, padx=(7, 2), pady=(5, 2), sticky=tk.W, ipadx=80)

    ttk.Label(tabBooks, text="Año publicación").grid(row=1, column=0, padx=5, pady=(5, 2), sticky=tk.W)    
    input_bookYear = ttk.Spinbox(tabBooks, from_=1900, to=2100)
    input_bookYear.grid(row=1, column=1, padx=(7, 2), pady=(5, 2), sticky=tk.W)
    input_bookYear.set(yearnow)

    ttk.Label(tabBooks, text="¿Disponible?").grid(row=2, column=0, padx=5, pady=(5, 2), sticky=tk.W)
    var_available = tk.BooleanVar()
    check_available = tk.Checkbutton(tabBooks, text="Sí", variable=var_available)
    check_available.grid(row=2, column=1, padx=(7, 2), pady=(5, 2), sticky=tk.W)

    ttk.Label(tabBooks, text="Autor").grid(row=3,column=0,padx=5,pady=(7, 2), sticky=tk.W)
    inputBookAuthor = ttk.Combobox(tabBooks, values=list(author_names.keys()), width=30)
    inputBookAuthor.grid(row=3,column=1,padx=(7,2), pady=(7, 2), sticky=tk.W) 

    ttk.Label(tabBooks,text="Género").grid(row=4,column=0,padx=5,pady=(7, 2), sticky=tk.W)

    inputBookGenre = ttk.Combobox(tabBooks, values=list(genre_names.keys()), width=30)
    inputBookGenre.grid(row=4,column=1,padx=(7,2), pady=(7, 2), sticky=tk.W)

    btn_addBook = ttk.Button(tabBooks,text="Guardar",command=cmd_saveBook)
    btn_addBook.grid(row=5, column=0, sticky=tk.W,padx=5)

    btn_cancel = ttk.Button(tabBooks,text="Cancelar",command=clear_fields)      
    btn_cancel.grid(row=5,column=1, sticky=tk.E,padx=5)
    
    tree_books = ttk.Treeview(tabBooks, columns=("ID", "Title", "Author", "Genre", "Year","Available"), show='headings')
    tree_books.configure(height=7)
    tree_books.heading("ID", text="ID")
    tree_books.heading("Title", text="Título")
    tree_books.heading("Author", text="Autor")
    tree_books.heading("Genre", text="Género")
    tree_books.heading("Year", text="Publicado")
    tree_books.heading("Available", text="Disponible")
    
    tree_books.grid(row=6,columnspan=2,pady=(3), sticky="ew")

    tree_books.column("ID", width=5, anchor='center', stretch=True)
    tree_books.column("Title", width=100, anchor='w', stretch=True)
    tree_books.column("Author", width=80, anchor='w', stretch=True)
    tree_books.column("Genre", width=60, anchor='w', stretch=True)
    tree_books.column("Year", width=30, anchor='center', stretch=True)
    tree_books.column("Available", width=20, anchor='center', stretch=True)

    btn_edit = ttk.Button(tabBooks,text="Editar seleccionado",command=cmd_editBook,width=20)
    btn_edit.grid(row=7,column=0, sticky=tk.SW,padx=5,pady=2)
    
    btn_delete = ttk.Button(tabBooks,text="Eliminar seleccionado",command=cmd_deleteBook,width=20)
    btn_delete.grid(row=7,column=1, sticky=tk.SE,padx=5,pady=2)

    list_books()
    return inputBookGenre,inputBookAuthor