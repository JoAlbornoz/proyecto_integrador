import tkinter as tk
from inicio import Login
from model.conexion_db import ConexionDB

def main():
    conexion = ConexionDB()
    conexion.crear_tablas()
    conexion.cerrar()
    
    root = tk.Tk()
    Login(root)
    root.mainloop()

if __name__ == "__main__":
    main()
