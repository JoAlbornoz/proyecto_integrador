import tkinter as tk
import os

class PantallaPrincipal:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Pantalla Principal")
        self.master.geometry("400x200")

        self.btn_opcion1 = tk.Button(self.master, text="Opción 1", command=self.abrir_opcion1)
        self.btn_opcion1.pack()

        self.btn_opcion2 = tk.Button(self.master, text="ARTISTAS", command=self.abrir_opcion2)
        self.btn_opcion2.pack()

        self.btn_opcion3 = tk.Button(self.master, text="LUGARES", command=self.abrir_opcion3)
        self.btn_opcion3.pack()

        self.btn_opcion4 = tk.Button(self.master, text="EVENTOS", command=self.abrir_opcion4)
        self.btn_opcion4.pack()

        self.master.mainloop()

    def abrir_opcion1(self):
        print("Ventana 1 abierta")

    def abrir_opcion2(self):
        try:
            os.system("python C:/Users/josef/proyectos/proyecto-integrador/gestor-cultural/client/editor_artista.py")
            print("Script editor_lugar.py se está ejecutando")
        except Exception as e:
            print("Error al abrir editor_lugar.py:", e)


    def abrir_opcion3(self):
        try:
            os.system("python C:/Users/josef/proyectos/proyecto-integrador/gestor-cultural/client/editor_lugar.py")
            print("Script editor_lugar.py se está ejecutando")
        except Exception as e:
            print("Error al abrir editor_lugar.py:", e)


    def abrir_opcion4(self):
        try:
            os.system("python C:/Users/josef/proyectos/proyecto-integrador/gestor-cultural/client/editor_evento.py")
            print("Script editor_lugar.py se está ejecutando")
        except Exception as e:
            print("Error al abrir editor_evento.py:", e)

