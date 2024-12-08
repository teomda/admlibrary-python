from db.controller import query

def delete_book(idBook):
    query("DELETE FROM libros WHERE id = ?", (idBook,))
    
def add_book(titulo, autor_id, genero_id, anio_publicacion, disponible):
    query("INSERT INTO libros (titulo, autor_id, genero_id ,anio_publicacion ,disponible) VALUES (?, ?, ?, ?, ?)", 
          (titulo ,autor_id ,genero_id ,anio_publicacion ,disponible))

def get_books():    
    sql = 'SELECT * FROM libros'
    books = query(sql)
    return books

def update_book(idBook,titulo ,autor_id ,genero_id ,anio_publicacion ,disponible):
     query("UPDATE libros SET titulo=?, autor_id=?, genero_id=?, anio_publicacion=?, disponible=? WHERE id=?",
           (titulo ,autor_id ,genero_id ,anio_publicacion ,disponible,idBook))