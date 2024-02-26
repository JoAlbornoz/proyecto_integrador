import tkinter as tk
from .conexion_db import ConexionDB
from tkinter import messagebox

#OPERACIONES Y CONSULTAS A LA BASE DE DATOS - TABLA ARTISTAS

class Artista:
    def __init__(self, nombre, alias, campo, genero, grupo, contacto):
        self.id_artista = None
        self.nombre = nombre
        self.alias = alias
        self.campo_artistico = campo
        self.genero_artistico = genero
        self.grupo = grupo
        self.contacto = contacto
    
    def __str__(self):
        return f'Artista[{self.nombre}, {self.alias}, {self.campo_artistico}, {self.genero_artistico}, {self.self.grupo}, {self.contacto}]'


def guardar_artista(artista):
    conexion = ConexionDB()

    sql = f"""INSERT INTO artistas (nombre, alias, campo_artistico, genero_artistico, grupo, contacto)
    VALUES('{artista.nombre}', '{artista.alias}', '{artista.campo_artistico}','{artista.genero_artistico}', '{artista.grupo}', '{artista.contacto}')"""
    
    try:
        conexion.cursor.execute(sql)
        # Confirmar los cambios en la base de datos
        conexion.conexion.commit()
        conexion.cerrar()
    except Exception as e:
        messagebox.showerror('Guardar Artista', f'Error al guardar el artista: {str(e)}')

def listar_artistas():
    conexion = ConexionDB()

    lista_artistas = []
    sql = 'SELECT * FROM artistas'

    try:
        conexion.cursor.execute(sql)
        lista_artistas = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception as e:
        messagebox.showwarning('Listar Artistas', f'Error al listar los artistas: {str(e)}')
    
    return lista_artistas

def editar_artista(artista, id_artista): 
    conexion = ConexionDB()

    sql = f"""UPDATE artistas
    SET nombre = '{artista.nombre}', alias = '{artista.alias}', campo_artistico = '{artista.campo_artistico}', genero_artistico = '{artista.genero_artistico}', grupo = '{artista.grupo}', contacto = '{artista.contacto}'
    WHERE id_artista = {id_artista}"""

    try:
        conexion.cursor.execute(sql)
        # Confirmar los cambios en la base de datos
        conexion.conexion.commit()
        conexion.cerrar()
    except Exception as e:
        messagebox.showerror('Editar Artista', f'Error al actualizar el artista: {str(e)}')

def eliminar_artista(id_artista):
    conexion = ConexionDB()
    sql = f'DELETE FROM artistas WHERE id_artista = {id_artista}'

    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()
        conexion.cerrar()
    except Exception as e:
        messagebox.showerror('Eliminar Artista', f'Error al eliminar el artista: {str(e)}')

def obtener_artistas():
    conexion = ConexionDB()
    sql = 'SELECT id_artista, nombre FROM artistas'  # Añadir el ID del artista a la consulta
    try:
        print("Ejecutando consulta SQL:", sql)
        conexion.cursor.execute(sql)
        artistas = conexion.cursor.fetchall()
        print("Artistas obtenidos:", artistas)
        conexion.cerrar()
        return artistas  # Devolver la lista de artistas con sus IDs
    except Exception as e:
        print("Error al obtener artistas:", e)
        return []