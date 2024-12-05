import sqlite3

def connect_db():
    db = sqlite3.connect('db/database.db')
    return db
    
def query(sql, params=()):
    # la funcion mas jodida!!
    dbc = connect_db()
    qry = dbc.cursor()
    try:
        qry.execute(sql, params)
        if sql.strip().upper().startswith("SELECT"):
            return qry.fetchall()
        else:
            dbc.commit()
    except sqlite3.Error as e:
        print(f"Error en la consulta: {e}")
        return None 
    finally:
        qry.close()
        dbc.close()


def setup_db():
    dbc = connect_db()
    query = dbc.cursor()    
    
    query.execute('''
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            nacionalidad TEXT,
            fecha_nacimiento TEXT
        )
    ''')
    
    query.execute('''
        CREATE TABLE IF NOT EXISTS generos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT
        )
    ''')
    
    query.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor_id INTEGER,
            genero_id INTEGER,
            anio_publicacion INTEGER,
            disponible BOOLEAN,
            FOREIGN KEY (autor_id) REFERENCES autores (id),
            FOREIGN KEY (genero_id) REFERENCES generos (id)
        )
    ''')
    
    dbc.commit()
    dbc.close()
