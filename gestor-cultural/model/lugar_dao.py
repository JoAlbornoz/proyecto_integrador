#lugar_dao.py
import tkinter as tk
from .conexion_db import ConexionDB
from tkinter import messagebox

#OPERACIONES Y CONSULTAS A LA BASE DE DATOS para Lugares
class Lugar:
    def __init__(self, nombre, tipo, direccion, capacidad):
        self.id_lugar = None
        self.nombre = nombre
        self.tipo = tipo
        self.direccion = direccion
        self.capacidad = capacidad
    
    def __str__(self):
        return f'Lugar[{self.nombre}, {self.tipo}, {self.direccion}, {self.capacidad}]'

def guardar_lugar(lugar):
    conexion = ConexionDB()

    sql = f"""INSERT INTO lugares (nombre, tipo, direccion, capacidad)
    VALUES('{lugar.nombre}', '{lugar.tipo}', '{lugar.direccion}', '{lugar.capacidad}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()  # Confirmar los cambios
        conexion.cerrar()
    except Exception as e:
        titulo = 'Guardar Lugar'
        mensaje = f'Error al guardar lugar: {str(e)}'
        messagebox.showerror(titulo, mensaje)

def listar_lugares():
    conexion = ConexionDB()

    lista_lugares = []
    sql = 'SELECT * FROM lugares'

    try:
        conexion.cursor.execute(sql)
        lista_lugares = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception as e:
        titulo = 'Listar Lugares'
        mensaje = f'Error al listar lugares: {str(e)}'
        messagebox.showerror(titulo, mensaje)
    
    return lista_lugares

def editar_lugar(lugar, id_lugar): 
    conexion = ConexionDB()

    sql = f"""UPDATE lugares
    SET nombre = '{lugar.nombre}', tipo = '{lugar.tipo}', direccion = '{lugar.direccion}', capacidad = '{lugar.capacidad}'
    WHERE id_lugar = {id_lugar}"""

    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()  # Confirmar los cambios
        conexion.cerrar()
    except Exception as e:
        titulo = 'Editar Lugar'
        mensaje = f'Error al editar lugar: {str(e)}'
        messagebox.showerror(titulo, mensaje)

def eliminar_lugar(id_lugar):
    conexion = ConexionDB()
    sql = f'DELETE FROM lugares WHERE id_lugar = {id_lugar}'

    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()  # Confirmar los cambios
        conexion.cerrar()
    except Exception as e:
        titulo = 'Eliminar Lugar'
        mensaje = f'Error al eliminar lugar: {str(e)}'
        messagebox.showerror(titulo, mensaje)

def obtener_lugares():
    conexion = ConexionDB()
    sql = 'SELECT id_lugar, nombre FROM lugares'  # Añadir el ID del lugar a la consulta
    try:
        print("Ejecutando consulta SQL:", sql)
        conexion.cursor.execute(sql)
        lugares = conexion.cursor.fetchall()
        print("Lugares obtenidos:", lugares)
        conexion.cerrar()
        return lugares  # Devolver la lista de lugares con sus IDs
    except Exception as e:
        print("Error al obtener lugares:", e)
        return []