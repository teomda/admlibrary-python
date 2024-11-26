
from dbp import connect_db

def add_author(nombre, nacionalidad, fecha_nacimiento):
    dbc = connect_db()
    query = dbc.cursor()
    query.execute('''
        INSERT INTO autores (nombre, nacionalidad, fecha_nacimiento)
        VALUES (?, ?, ?)
    ''', (nombre, nacionalidad, fecha_nacimiento))
    dbc.commit()
    dbc.close()

def get_authors():
    dbc = connect_db()
    query = dbc.cursor()
    query.execute('SELECT * FROM autores')
    autores = query.fetchall()
    dbc.close()
    return autores
