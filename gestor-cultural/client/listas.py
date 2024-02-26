import tkinter as tk
from tkinter import ttk
import sqlite3

#Visualizador de mis listas

class VisualizacionTablas(tk.Tk):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg='purple')
        self.title("Visualización de Tablas")

        self.conexion_db = sqlite3.connect('database/gestion_cultural.db')
        self.cursor = self.conexion_db.cursor()

        self.frame_botones = ttk.Frame(self)
        self.frame_botones.pack()

        self.btn_artistas = ttk.Button(self.frame_botones, text="Artistas", command=self.mostrar_artistas)
        self.btn_artistas.grid(row=0, column=0, padx=5, pady=5)

        self.btn_eventos = ttk.Button(self.frame_botones, text="Eventos", command=self.mostrar_eventos)
        self.btn_eventos.grid(row=0, column=1, padx=5, pady=5)

        self.btn_lugares = ttk.Button(self.frame_botones, text="Lugares", command=self.mostrar_lugares)
        self.btn_lugares.grid(row=0, column=2, padx=5, pady=5)

        self.btn_artistas_eventos = ttk.Button(self.frame_botones, text="Artistas_Eventos", command=self.mostrar_artistas_eventos)
        self.btn_artistas_eventos.grid(row=0, column=3, padx=5, pady=5)

        self.btn_eventos_lugares = ttk.Button(self.frame_botones, text="Eventos_Lugares", command=self.mostrar_eventos_lugares)
        self.btn_eventos_lugares.grid(row=0, column=4, padx=5, pady=5)

        self.frame_tablas = ttk.Frame(self)
        self.frame_tablas.pack()

        self.contenidos_artistas = None
        self.contenidos_eventos = None
        self.contenidos_lugares = None
        self.contenidos_artistas_eventos = None
        self.contenidos_eventos_lugares = None

    def obtener_contenido_tabla(self, nombre_tabla):
        self.cursor.execute(f"SELECT * FROM {nombre_tabla};")
        return self.cursor.fetchall()

    def mostrar_artistas(self):
        if self.contenidos_artistas is None:
            self.contenidos_artistas = self.obtener_contenido_tabla('artistas')
            self.mostrar_contenidos('Artistas', self.contenidos_artistas)
        else:
            self.mostrar_contenidos('Artistas', self.contenidos_artistas)

    def mostrar_eventos(self):
        if self.contenidos_eventos is None:
            self.contenidos_eventos = self.obtener_contenido_tabla('eventos')
            self.mostrar_contenidos('Eventos', self.contenidos_eventos)
        else:
            self.mostrar_contenidos('Eventos', self.contenidos_eventos)

    def mostrar_lugares(self):
        if self.contenidos_lugares is None:
            self.contenidos_lugares = self.obtener_contenido_tabla('lugares')
            self.mostrar_contenidos('Lugares', self.contenidos_lugares)
        else:
            self.mostrar_contenidos('Lugares', self.contenidos_lugares)

    def mostrar_artistas_eventos(self):
        if self.contenidos_artistas_eventos is None:
            self.contenidos_artistas_eventos = self.obtener_contenido_artistas_eventos()
            self.mostrar_contenidos('Artistas_Eventos', self.contenidos_artistas_eventos)
        else:
            self.mostrar_contenidos('Artistas_Eventos', self.contenidos_artistas_eventos)

    def mostrar_eventos_lugares(self):
        if self.contenidos_eventos_lugares is None:
            self.contenidos_eventos_lugares = self.obtener_contenido_eventos_lugares()
            self.mostrar_contenidos('Eventos_Lugares', self.contenidos_eventos_lugares)
        else:
            self.mostrar_contenidos('Eventos_Lugares', self.contenidos_eventos_lugares)

    def obtener_contenido_artistas_eventos(self):
        self.cursor.execute("SELECT artistas.nombre, eventos.nombre FROM artistas_eventos "
                            "INNER JOIN artistas ON artistas_eventos.id_artista = artistas.id_artista "
                            "INNER JOIN eventos ON artistas_eventos.id_evento = eventos.id_evento;")
        return self.cursor.fetchall()

    def obtener_contenido_eventos_lugares(self):
        self.cursor.execute("SELECT eventos.nombre, lugares.nombre FROM eventos_lugares "
                            "INNER JOIN eventos ON eventos_lugares.id_evento = eventos.id_evento "
                            "INNER JOIN lugares ON eventos_lugares.id_lugar = lugares.id_lugar;")
        return self.cursor.fetchall()

    def mostrar_contenidos(self, nombre_tabla, contenido_tabla):
        for widget in self.frame_tablas.winfo_children():
            widget.destroy()

        tk.Label(self.frame_tablas, text="Tabla").pack()
        tabla = ttk.Treeview(self.frame_tablas, show='headings')

        if nombre_tabla == 'Artistas_Eventos':
            tabla["columns"] = ("#0", "#1", "#2")
            tabla.heading("#0", text="ID")
            tabla.heading("#1", text="Nombre Artista")
            tabla.heading("#2", text="Nombre Evento")
        elif nombre_tabla == 'Eventos_Lugares':
            tabla["columns"] = ("#0", "#1", "#2")
            tabla.heading("#0", text="ID")
            tabla.heading("#1", text="Nombre Evento")
            tabla.heading("#2", text="Nombre Lugar")
        else:
            # Obtener los nombres de las columnas
            column_names = [description[0] for description in self.cursor.description]
            tabla["columns"] = tuple(column_names)
            for i, columna in enumerate(column_names):
                tabla.heading(columna, text=columna)

        for fila in contenido_tabla:
            tabla.insert('', 'end', values=fila)
        tabla.pack()


if __name__ == "__main__":
    app = VisualizacionTablas(None)
    app.mainloop()