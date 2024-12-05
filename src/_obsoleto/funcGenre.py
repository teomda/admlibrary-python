from dbp import query

def delete_genre(idGenre):
    query("DELETE FROM generos WHERE id = ?", (idGenre,))  # no me funca si no es tupla

def add_genre(nombre, descripcion):
    query("INSERT INTO generos (nombre, descripcion) VALUES (?, ?)", (nombre, descripcion))

def get_genres():    
    sql = 'SELECT * FROM generos'
    genres = query(sql)
    return genres

