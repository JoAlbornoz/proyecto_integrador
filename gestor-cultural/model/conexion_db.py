import sqlite3

# SE GENERAN LAS TABLAS AUTOMÁTICAMENTE AL INICIAR LA APP

class ConexionDB:
    def __init__(self):
        self.basedatos = 'database/gestion_cultural.db'
        self.conexion = sqlite3.connect(self.basedatos)
        self.cursor = self.conexion.cursor()

    def crear_tablas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS artistas (
                id_artista INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                alias TEXT,           
                campo_artistico TEXT,
                genero_artistico TEXT,
                grupo TEXT,
                contacto TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS eventos (
                id_evento INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                tipo TEXT,
                fecha TEXT,
                precio TEXT                    
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS lugares (
                id_lugar INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                tipo TEXT,
                direccion TEXT,
                capacidad TEXT            
            )
        ''')

    #Están mal nombradas, deberían llamarse evento_artistas y lugar_eventos, y mal ubicadas las columnas
    #Ya que un evento tiene varios artistas, y un lugar tiene varios eventos
    #además, falta artista_eventos, tabla donde un artista puede tener varios eventos

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS artistas_eventos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_artista INTEGER,
                id_evento INTEGER,
                FOREIGN KEY (id_artista) REFERENCES artistas(id_artista),
                FOREIGN KEY (id_evento) REFERENCES eventos(id_evento)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS eventos_lugares (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_evento INTEGER,
                id_lugar INTEGER,
                FOREIGN KEY (id_evento) REFERENCES eventos(id_evento),
                FOREIGN KEY (id_lugar) REFERENCES lugares(id_lugar)
            )
        ''')

        self.conexion.commit()

    def cerrar(self):
        self.conexion.close()
