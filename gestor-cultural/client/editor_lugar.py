import tkinter as tk
import sys
sys.path.append("C:/Users/josef/proyectos/proyecto-integrador/gestor-cultural")
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from model.lugar_dao import Lugar, guardar_lugar, listar_lugares, editar_lugar, eliminar_lugar

class EditorLugaresFrame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg='purple')
        
        self.id_lugar = None
        self.lugares()
        self.deshabilitar_campos()
        self.tabla_lugares()
        self.entry_buscar.bind("<KeyRelease>", self.buscar_datos)
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_lugar)
        
    def lugares(self):
        self.label_nombre = tk.Label(self, text='Nombre del lugar:')
        self.label_nombre.config(font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.label_nombre.grid(row=2, column=0, padx=10, pady=10)

        self.label_tipo = tk.Label(self, text='Tipo de lugar:')
        self.label_tipo.config(font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.label_tipo.grid(row=3, column=0, padx=10, pady=10)

        self.label_direccion = tk.Label(self, text='Dirección:')
        self.label_direccion.config(font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.label_direccion.grid(row=4, column=0, padx=10, pady=10)

        self.label_capacidad = tk.Label(self, text='Capacidad:')
        self.label_capacidad.config(font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.label_capacidad.grid(row=5, column=0, padx=10, pady=10)

#--------------------------------------------------------------------------
        self.lugar_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.lugar_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10)

        self.lugar_tipo = tk.StringVar()
        self.entry_tipo = tk.Entry(self, textvariable = self.lugar_tipo)
        self.entry_tipo.config(width=50, font=('Arial', 12))
        self.entry_tipo.grid(row=3, column=1, padx=10, pady=10)

        self.lugar_direccion = tk.StringVar()
        self.entry_direccion = tk.Entry(self, textvariable = self.lugar_direccion)
        self.entry_direccion.config(width=50, font=('Arial', 12))
        self.entry_direccion.grid(row=4, column=1, padx=10, pady=10)

        self.lugar_capacidad = tk.StringVar()
        self.entry_capacidad = tk.Entry(self, textvariable = self.lugar_capacidad)
        self.entry_capacidad.config(width=50, font=('Arial', 12))
        self.entry_capacidad.grid(row=5, column=1, padx=10, pady=10)
#--------------------------------------------------------------------------
        self.boton_nuevo = tk.Button(self, text="Crear lugar", command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='blue', cursor='hand2', activebackground='#D2302E')
        self.boton_nuevo.grid(row=2, column=3, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar lugar", command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', activebackground='#2ED231')
        self.boton_guardar.grid(row=3, column=3, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text="Cancelar", command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='blue', cursor='hand2', activebackground='#D2302E')
        self.boton_cancelar.grid(row=4, column=3, padx=10, pady=10)

    def habilitar_campos(self):
        self.boton_nuevo.config(state='disabled')
        self.lugar_nombre.set('')
        self.lugar_tipo.set('')
        self.lugar_direccion.set('')
        self.lugar_capacidad.set('')

        self.entry_nombre.config(state='normal')
        self.entry_tipo.config(state='normal')
        self.entry_direccion.config(state='normal')
        self.entry_capacidad.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')
        
    def deshabilitar_campos(self):
        self.entry_nombre.delete(0, END)
        self.entry_tipo.delete(0, END)
        self.entry_direccion.delete(0, END)
        self.entry_capacidad.delete(0, END)

        self.entry_nombre.config(state='disabled')
        self.entry_tipo.config(state='disabled')
        self.entry_direccion.config(state='disabled')
        self.entry_capacidad.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
        self.boton_nuevo.config(state='normal')

    def desactivar_botones(self):
        self.editar.config(state='disabled')
        self.eliminar.config(state='disabled')

    def seleccionar_lugar(self, event):
        seleccionado = self.tabla.selection()
        if seleccionado:
            self.editar.config(state='normal')
            self.eliminar.config(state='normal')
        else:
            self.desactivar_botones()

    def guardar_datos(self):
         lugar = Lugar(
            self.lugar_nombre.get(),
            self.lugar_tipo.get(),
            self.lugar_direccion.get(),
            self.lugar_capacidad.get(),
         )

         if self.id_lugar == None:
            guardar_lugar(lugar)
            self.tabla_lugares()
            self.deshabilitar_campos()
            
         else:
            editar_lugar(lugar, self.id_lugar)
            self.tabla_lugares()
            self.deshabilitar_campos()

         self.desactivar_botones()
         self.boton_nuevo.config(state='normal')
            
         titulo = 'Guardar lugar'
         mensaje = 'Lugar guardado con éxito'
         messagebox.showinfo(titulo, mensaje)

         self.entry_buscar.bind("<KeyRelease>", self.buscar_datos)
         self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_lugar)

    def tabla_lugares(self):
        self.lista_lugares = listar_lugares()

        self.tabla = ttk.Treeview(self, column=('Nombre', 'Tipo', 'Direccion', 'Capacidad'))
        self.tabla.grid(row=1, column=0, columnspan=6, sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=1, column=6, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Tipo')
        self.tabla.heading('#3', text='Dirección')
        self.tabla.heading('#4', text='Capacidad')
        
        for lugar in self.lista_lugares:
            self.tabla.insert('', 0, text=lugar[0], values=(lugar[1], lugar[2], lugar[3], lugar[4]))

#--------------------------Editar y eliminar---------------------------
        self.editar = tk.Button(self, text="Editar lugar", command=self.editar_lugar, state='disabled')
        self.editar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', activebackground='#2ED231')
        self.editar.grid(row=5, column=3, padx=10, pady=10)

        self.eliminar = tk.Button(self, text="Eliminar lugar", command=self.eliminar_lugar , state='disabled')
        self.eliminar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='blue', cursor='hand2', activebackground='#D2302E')
        self.eliminar.grid(row=6, column=3, padx=10, pady=10)

        self.label_buscar = tk.Label(self, text="Buscar:")
        self.label_buscar.config(font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.label_buscar.grid(row=0, column=0, padx=10, pady=10)

        self.entry_buscar = tk.Entry(self)
        self.entry_buscar.config(width=30, font=('Arial', 12))
        self.entry_buscar.grid(row=0, column=1, padx=10, pady=10)

    def editar_lugar(self):  # Corregido
            try:
                self.desactivar_botones()
                self.id_lugar = self.tabla.item(self.tabla.selection())['text']
                self.nombre_lugar = self.tabla.item(self.tabla.selection())['values'][0]
                self.tipo_lugar = self.tabla.item(self.tabla.selection())['values'][1]
                self.direccion_lugar = self.tabla.item(self.tabla.selection())['values'][2]
                self.capacidad_lugar = self.tabla.item(self.tabla.selection())['values'][3]

                self.habilitar_campos()

                self.entry_nombre.insert(0, self.nombre_lugar)
                self.entry_tipo.insert(0, self.tipo_lugar)  
                self.entry_direccion.insert(0, self.direccion_lugar) 
                self.entry_capacidad.insert(0, self.capacidad_lugar) 
            except:
                messagebox.showerror('Editar Lugar', 'No se ha seleccionado ningún registro.')

    def eliminar_lugar(self):
        try:
            seleccionado = self.tabla.selection()
            if seleccionado:
                confirmar = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este lugar?")
                if confirmar:
                    self.desactivar_botones()
                    self.id_lugar = self.tabla.item(seleccionado)['text']
                    eliminar_lugar(self.id_lugar)
                    self.tabla_lugares()
                    self.id_lugar = None
                    messagebox.showinfo("Lugar eliminado", "El lugar ha sido eliminado correctamente.")

                    self.entry_buscar.bind("<KeyRelease>", self.buscar_datos)
                    self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_lugar)
            else:
                messagebox.showerror("Eliminar un Lugar", "No se ha seleccionado ningún lugar para eliminar.")
        except Exception as e:
            print(e)

    def buscar_datos(self, event):
        valor_busqueda = self.entry_buscar.get().lower() 
        
        if not valor_busqueda:
            self.tabla.selection_remove(self.tabla.selection())
            return
        
        self.tabla.selection_remove(self.tabla.selection())
        
        for item in self.tabla.get_children():
            valores_fila = self.tabla.item(item)['values']
            if any(valor_busqueda in str(valor).lower() for valor in valores_fila):
                self.tabla.selection_add(item)



root = tk.Tk()
root.title('Gestor Cultural - Editor de Lugares')
root.resizable(0, 0)

app = EditorLugaresFrame(root)
root.mainloop()
