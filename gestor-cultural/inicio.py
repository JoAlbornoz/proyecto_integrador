import tkinter as tk
from tkinter import *
from tkinter import messagebox
from pantalla_principal import PantallaPrincipal

class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Iniciar sesión")
        self.master.geometry("900x500")
        self.master.configure(bg='purple')

        self.frame = Frame(self.master, bg='purple')

        self.inicio_label = Label(self.frame, text="Iniciar sesión", bg='purple', fg="white", font=("Arial", 40))
        self.sub_label = Label(self.frame, text="Gestion cultural - Jujuy", bg='purple', fg="white", font=("Arial", 25))
        self.usuario_label = Label(self.frame, text="Usuario", bg='purple', fg="#FFFFFF", font=("Arial", 16))
        self.usuario_entry = Entry(self.frame, font=("Arial", 16))
        self.contraseña_entry = Entry(self.frame, show="*", font=("Arial", 16))
        self.contraseña_label = Label(self.frame, text="Contraseña", bg='purple', fg="#FFFFFF", font=("Arial", 16))
        self.boton_login = Button(self.frame, text="Ingresar", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.login)

        self.inicio_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        self.sub_label.grid(row=1, column=0, columnspan=2, sticky="news", pady=40)
        self.usuario_label.grid(row=2, column=0, padx=5)
        self.usuario_entry.grid(row=2, column=1, pady=10)
        self.contraseña_label.grid(row=3, column=0, padx=5)
        self.contraseña_entry.grid(row=3, column=1, pady=10)
        self.boton_login.grid(row=4, column=0, columnspan=2, pady=30)

        self.frame.pack()

    def login(self):
        usuario_correcto = "admin"
        contraseña_correcta = "1234"

        usuario = self.usuario_entry.get()
        contraseña = self.contraseña_entry.get()

        if usuario == usuario_correcto and contraseña == contraseña_correcta:
            self.master.destroy()
            PantallaPrincipal()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
