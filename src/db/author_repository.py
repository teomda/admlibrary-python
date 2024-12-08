from db.controller import query

def delete_author(idAuthor):
    query("DELETE FROM autores WHERE id = ?", (idAuthor,))  # no me funca si no es tupla

def add_author(nombre, nacionalidad, fecha_nacimiento):
    query("INSERT INTO autores (nombre, nacionalidad, fecha_nacimiento) VALUES (?, ?, ?)", (nombre, nacionalidad, fecha_nacimiento))

def get_authors():    
    sql = 'SELECT * FROM autores'
    authors = query(sql)
    return authors

def update_author(idAuthor, nombre, nacionalidad, fecha_nacimiento):
    query("UPDATE autores SET nombre = ?, nacionalidad = ?, fecha_nacimiento = ? WHERE id = ?", 
          (nombre, nacionalidad, fecha_nacimiento, idAuthor))