import sqlite3

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
