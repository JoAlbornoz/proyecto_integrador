import tkinter as tk
from tkinter import messagebox

#Falta migrar la parte visual

class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x150")

        self.label_user = tk.Label(self.master, text="Usuario:")
        self.label_user.pack()
        self.entry_user = tk.Entry(self.master)
        self.entry_user.pack()

        self.label_password = tk.Label(self.master, text="Contraseña:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_password.pack()

        self.btn_login = tk.Button(self.master, text="Iniciar sesión", command=self.login)
        self.btn_login.pack()

    def login(self):
        # Validar usuario y contraseña
        usuario_correcto = "admin"
        contraseña_correcta = "1234"

        usuario = self.entry_user.get()
        contraseña = self.entry_password.get()

        if usuario == usuario_correcto and contraseña == contraseña_correcta:
            self.master.destroy()
            from pantalla_principal import PantallaPrincipal
            PantallaPrincipal()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")


if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
