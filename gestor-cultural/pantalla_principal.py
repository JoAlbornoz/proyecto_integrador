import tkinter as tk
from tkinter import Label, PhotoImage, Button
import os

class PantallaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bienvenido - Gestor Cultural")
        self.geometry("900x550")
        self.configure(bg='purple')
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self, bg='purple')
        frame.pack(side='right', padx=20)

        imagen = PhotoImage(file='imagenes/nevado.png')
        label_imagen = Label(self, image=imagen, bg='purple', padx=0, pady=0)
        label_imagen.photo = imagen
        label_imagen.pack(side='left', pady=0, padx=0, expand=tk.YES, fill=tk.Y)

        texto1 = tk.Label(frame, text='Ingrese a las listas', font=('Arial', 12), fg='white', bg='purple')
        texto2 = tk.Label(frame, text='Ingrese a los editores', font=('Arial', 12), fg='white', bg='purple')

        buscar_boton = Button(frame, text='Listas', width=20, height=2, font=('Arial', 15), bg='orange', fg='white', cursor='hand2')
        artistas_boton = Button(frame, text='Artistas', width=20, height=2, font=('Arial', 15), bg='blue', fg='white', cursor='hand2', command=self.abrir_editor_artista)
        lugares_boton = Button(frame, text='Lugares', width=20, height=2, font=('Arial', 15), bg='green', fg='white', cursor='hand2', command=self.abrir_editor_lugar)
        eventos_boton = Button(frame, text='Eventos', width=20, height=2, font=('Arial', 15), bg='red', fg='white', cursor='hand2', command=self.abrir_editor_evento)

        texto1.grid(row=0, column=1, padx=10, pady=(20))
        buscar_boton.grid(row=1, column=1, padx=10, pady=10, sticky="e")
        texto2.grid(row=2, column=1, padx=10, pady=(20))
        artistas_boton.grid(row=3, column=1, padx=10, pady=(20), sticky="e")
        lugares_boton.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        eventos_boton.grid(row=5, column=1, padx=10, pady=10, sticky="e")

    #Tkinter tiene problemas para abrir distintas ventanas, por lo que al trabajar desde mi compu
    # para poder visualizarlas preferí llamar a la ruta exacta de mis archivos

    def abrir_editor_artista(self):
        try:
            os.system("python C:/Users/josef/proyectos/proyecto-integrador/gestor-cultural/client/editor_artista.py")
            print("Script editor_artista.py se está ejecutando")
        except Exception as e:
            print("Error al abrir editor_artista.py:", e)

    def abrir_editor_lugar(self):
        try:
            os.system("python C:/Users/josef/proyectos/proyecto-integrador/gestor-cultural/client/editor_lugar.py")
            print("Script editor_lugar.py se está ejecutando")
        except Exception as e:
            print("Error al abrir editor_lugar.py:", e)

    def abrir_editor_evento(self):
        try:
            os.system("python C:/Users/josef/proyectos/proyecto-integrador/gestor-cultural/client/editor_evento.py")
            print("Script editor_evento.py se está ejecutando")
        except Exception as e:
            print("Error al abrir editor_evento.py:", e)