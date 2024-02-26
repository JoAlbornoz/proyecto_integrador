#evento_dao.py
import tkinter as tk
from .conexion_db import ConexionDB
from tkinter import messagebox

class Evento:
    def __init__(self, nombre, tipo, fecha, precio, id_lugar, id_artista):
        self.id_evento = None
        self.nombre = nombre
        self.tipo = tipo
        self.fecha = fecha
        self.precio = precio
        self.id_lugar = id_lugar
        self.id_artista = id_artista
    
    def __str__(self):
        return f'Evento[{self.nombre}, {self.tipo}, {self.fecha}, {self.precio}, {self.id_lugar}, {self.id_artista}]'
    

def guardar(evento):
    conexion = ConexionDB()

    sql = f"""INSERT INTO eventos (nombre, tipo, fecha, precio)
    VALUES('{evento.nombre}','{evento.tipo}', '{evento.fecha}', '{evento.precio}')"""
    
    try:
        conexion.cursor.execute(sql)
        evento_id = conexion.cursor.lastrowid

        sql_artistas_eventos = f"""INSERT INTO artistas_eventos (id_artista, id_evento)
        VALUES('{evento.id_artista}', '{evento_id}')"""
        conexion.cursor.execute(sql_artistas_eventos)

        sql_eventos_lugares = f"""INSERT INTO eventos_lugares (id_evento, id_lugar)
        VALUES('{evento_id}', '{evento.id_lugar}')"""
        conexion.cursor.execute(sql_eventos_lugares)

        conexion.conexion.commit()
        conexion.cerrar()
    except Exception as e:
        messagebox.showerror('Guardar Evento', f'Error al guardar el evento: {str(e)}')


def listar():
    conexion = ConexionDB()

    lista_eventos = []
    sql = 'SELECT * FROM eventos'

    try:
        conexion.cursor.execute(sql)
        lista_eventos = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception as e:
        messagebox.showwarning('Listar Eventos', f'Error al listar los eventos: {str(e)}')
    
    return lista_eventos

def editar(evento, id_evento): 
    conexion = ConexionDB()

    sql = f"""UPDATE eventos
    SET nombre = '{evento.nombre}', tipo = '{evento.tipo}', fecha = '{evento.fecha}', precio = '{evento.precio}'
    WHERE id_evento = {id_evento}"""

    try:
        conexion.cursor.execute(sql)
        sql_artista_evento = f"""UPDATE artistas_eventos
        SET id_artista = '{evento.id_artista}'
        WHERE id_evento = {id_evento}"""

        sql_eventos_lugares = f"""UPDATE eventos_lugares
        SET id_lugar = '{evento.id_lugar}'
        WHERE id_evento = {id_evento}"""
        conexion.cursor.execute(sql_artista_evento)
        conexion.cursor.execute(sql_eventos_lugares)
        conexion.conexion.commit()
        conexion.cerrar()
    except Exception as e:
        titulo = 'Edición de datos'
        mensaje = f'Falló la actualización del registro: {str(e)}'
        messagebox.showerror(titulo, mensaje)


def eliminar(id_evento):
    conexion = ConexionDB()
    sql = f'DELETE FROM eventos WHERE id_evento = {id_evento}'

    try:
        conexion.cursor.execute(sql)
        sql_eliminar_artista = f"DELETE FROM artistas_eventos WHERE id_evento = {id_evento}"
        conexion.cursor.execute(sql_eliminar_artista)
        
        sql_eliminar_lugar = f"DELETE FROM eventos_lugares WHERE id_evento = {id_evento}"
        conexion.cursor.execute(sql_eliminar_lugar)
        
        conexion.conexion.commit()
        conexion.cerrar()
    except Exception as e:
            messagebox.showerror('Eliminar Evento', f'Error al eliminar el evento: {str(e)}')

def obtener_eventos():
    conexion = ConexionDB()
    sql = 'SELECT nombre FROM eventos'
    try:
        print("Ejecutando consulta SQL:", sql)
        conexion.cursor.execute(sql)
        eventos = conexion.cursor.fetchall()
        print("Eventos obtenidos:", eventos)
        conexion.cerrar()
        return [evento[0] for evento in eventos]
    except Exception as e:
        print("Error al obtener eventos:", e)
        return []
    
# Función para obtener el ID del artista asociado a un evento
def obtener_id_artistas_eventos(id_evento):
    conexion = ConexionDB()
    try:
        sql = f"SELECT id_artista FROM artistas_eventos WHERE id_evento = {id_evento}"
        conexion.cursor.execute(sql)
        id_artista = conexion.cursor.fetchone()[0]
        conexion.cerrar()
        return id_artista
    except Exception as e:
        messagebox.showerror('Obtener ID Artista Evento', f'Error al obtener el ID del artista asociado al evento: {str(e)}')

# Función para obtener el ID del lugar asociado a un evento
def obtener_id_eventos_lugares(id_evento):
    conexion = ConexionDB()
    try:
        sql = f"SELECT id_lugar FROM eventos_lugares WHERE id_evento = {id_evento}"
        conexion.cursor.execute(sql)
        id_lugar = conexion.cursor.fetchone()[0]
        conexion.cerrar()
        return id_lugar
    except Exception as e:
        messagebox.showerror('Obtener ID Lugar Evento', f'Error al obtener el ID del lugar asociado al evento: {str(e)}')