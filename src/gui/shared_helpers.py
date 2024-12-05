# from gui.tab_genres import get_genres_names
from db.genre_repository import get_genres
from db.author_repository import get_authors

def get_genres_names():
    list_authors = get_genres()
    return {author[1]: author[0] for author in list_authors} 

def update_genre_combobox(inputBookGenre):
    genre_names = get_genres_names()
    inputBookGenre['values'] = list(genre_names.keys())
    inputBookGenre.set('')

def get_author_names():
    list_authors = get_authors()
    return {author[1]: author[0] for author in list_authors}    

def update_author_combobox(inputBookAuthor):
    author_names = get_author_names()
    inputBookAuthor['values'] = list(author_names.keys())
    inputBookAuthor.set('')