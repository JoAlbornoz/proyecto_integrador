import tkinter as tk
from inicio import Login
from model.conexion_db import ConexionDB

def main():
    # Crear las tablas en la base de datos
    conexion = ConexionDB()
    conexion.crear_tablas()
    conexion.cerrar()

    # Iniciar la interfaz gráfica    
    root = tk.Tk()
    Login(root)
    root.mainloop()

if __name__ == "__main__":
    main()
