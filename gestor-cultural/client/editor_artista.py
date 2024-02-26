import tkinter as tk
import sys
sys.path.append("C:/Users/josef/proyectos/proyecto-integrador/gestor-cultural")
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from model.artista_dao import Artista, guardar_artista, listar_artistas, editar_artista, eliminar_artista

class EditorArtistasFrame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg='purple')
        
        self.id_artista = None
        self.artistas()
        self.deshabilitar_campos()
        self.tabla_artistas()
        self.entry_buscar.bind("<KeyRelease>", self.buscar_datos)
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_artista)
 
    def artistas(self):
        self.label_nombre = tk.Label(self, text='Nombre del artista:')
        self.label_nombre.config(font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.label_nombre.grid(row=2, column=0, padx=10, pady=10)

        self.label_alias = tk.Label(self, text='Seudonimo (Si tuviese):')
        self.label_alias.config(font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.label_alias.grid(row=3, column=0, padx=10, pady=10)

        self.label_campo = tk.Label(self, text='Campo artístico:')
        self.label_campo.config(font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.label_campo.grid(row=4, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text='Genero artístico:')
        self.label_genero.config(font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.label_genero.grid(row=5, column=0, padx=10, pady=10)

        self.label_grupo = tk.Label(self, text='Grupo (si perteneciera):')
        self.label_grupo.config(font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.label_grupo.grid(row=6, column=0, padx=10, pady=10)

        self.label_contacto = tk.Label(self, text='Correo electronico:')
        self.label_contacto.config(font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.label_contacto.grid(row=7, column=0, padx=10, pady=10)


        #--------------------------------------------------------------------------

        self.artista_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.artista_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10)

        self.artista_alias = tk.StringVar()
        self.entry_alias = tk.Entry(self, textvariable = self.artista_alias)
        self.entry_alias.config(width=50, font=('Arial', 12))
        self.entry_alias.grid(row=3, column=1, padx=10, pady=10)

        self.artista_campo = tk.StringVar()
        self.entry_campo = tk.Entry(self, textvariable = self.artista_campo)
        self.entry_campo.config(width=50, font=('Arial', 12))
        self.entry_campo.grid(row=4, column=1, padx=10, pady=10)

        self.artista_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable = self.artista_genero)
        self.entry_genero.config(width=50, font=('Arial', 12))
        self.entry_genero.grid(row=5, column=1, padx=10, pady=10)

        self.artista_grupo = tk.StringVar()
        self.entry_grupo = tk.Entry(self, textvariable = self.artista_grupo)
        self.entry_grupo.config(width=50, font=('Arial', 12))
        self.entry_grupo.grid(row=6, column=1, padx=10, pady=10)

        self.artista_contacto = tk.StringVar()
        self.entry_contacto = tk.Entry(self, textvariable = self.artista_contacto)
        self.entry_contacto.config(width=50, font=('Arial', 12))
        self.entry_contacto.grid(row=7, column=1, padx=10, pady=10)

        #----------------------------------------------------------------------------

        self.boton_nuevo = tk.Button(self, text="Crear artista", command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='blue', cursor='hand2', activebackground='#D2302E')
        self.boton_nuevo.grid(row=2, column=3, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar artista", command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', activebackground='#2ED231')
        self.boton_guardar.grid(row=3, column=3, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text="Cancelar", command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='blue', cursor='hand2', activebackground='#D2302E')
        self.boton_cancelar.grid(row=4, column=3, padx=10, pady=10)

    def habilitar_campos(self):
        self.boton_nuevo.config(state='disabled')
        self.artista_nombre.set('')
        self.artista_alias.set('')
        self.artista_campo.set('')
        self.artista_genero.set('')
        self.artista_grupo.set('')
        self.artista_contacto.set('')

        self.entry_nombre.config(state='normal')
        self.entry_alias.config(state='normal')
        self.entry_campo.config(state='normal')
        self.entry_genero.config(state='normal')
        self.entry_grupo.config(state='normal')
        self.entry_contacto.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')
        
    def deshabilitar_campos(self):
        self.entry_nombre.delete(0, END)
        self.entry_alias.delete(0, END)
        self.entry_campo.delete(0, END)
        self.entry_genero.delete(0, END)
        self.entry_grupo.delete(0, END)
        self.entry_contacto.delete(0, END)

        self.entry_nombre.config(state='disabled')
        self.entry_alias.config(state='disabled')
        self.entry_campo.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.entry_grupo.config(state='disabled')
        self.entry_contacto.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
        self.boton_nuevo.config(state='normal')

    def desactivar_botones(self):
        self.editar.config(state='disabled')
        self.eliminar.config(state='disabled')

    def seleccionar_artista(self, event):
        seleccionado = self.tabla.selection()
        if seleccionado:
            self.editar.config(state='normal')
            self.eliminar.config(state='normal')
        else:
            self.desactivar_botones()

    def guardar_datos(self):
         artista = Artista(
             self.artista_nombre.get(),
             self.artista_alias.get(),
             self.artista_campo.get(),
             self.artista_genero.get(),
             self.artista_grupo.get(),
             self.artista_contacto.get(),
         )

         if self.id_artista == None:
            guardar_artista(artista)
            self.tabla_artistas()
            self.deshabilitar_campos()
            
         else:
            editar_artista(artista, self.id_artista)
            self.tabla_artistas()
            self.deshabilitar_campos()

         self.desactivar_botones()
         self.boton_nuevo.config(state='normal')
            
         titulo = 'Guardar artista'
         mensaje = 'Datos de artista guardados con éxito'
         messagebox.showinfo(titulo, mensaje)

         self.entry_buscar.bind("<KeyRelease>", self.buscar_datos)
         self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_artista)

    def tabla_artistas(self):
        self.lista_artistas = listar_artistas()

        self.tabla = ttk.Treeview(self, column=('Nombre', 'Alias', 'Campo', 'Género', 'Grupo', 'Contacto'))
        self.tabla.grid(row=1, column=0, columnspan=6, sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=1, column=6, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Alias')
        self.tabla.heading('#3', text='Campo')
        self.tabla.heading('#4', text='Género')
        self.tabla.heading('#5', text='Grupo')
        self.tabla.heading('#6', text='Contacto')
        
        for artista in self.lista_artistas:
            self.tabla.insert('', 0, text=artista[0], values=(artista[1], artista[2], artista[3], artista[4], artista[5], artista[6]))

#--------------------------Editar y eliminar---------------------------
        self.editar = tk.Button(self, text="Editar artista", command=self.editar_artista, state='disabled')
        self.editar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', activebackground='#2ED231')
        self.editar.grid(row=5, column=3, padx=10, pady=10)

        self.eliminar = tk.Button(self, text="Eliminar artista", command=self.eliminar_artista , state='disabled')
        self.eliminar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='blue', cursor='hand2', activebackground='#D2302E')
        self.eliminar.grid(row=6, column=3, padx=10, pady=10)

        self.label_buscar = tk.Label(self, text="Buscar:")
        self.label_buscar.config(font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.label_buscar.grid(row=0, column=0, padx=10, pady=10)

        self.entry_buscar = tk.Entry(self)
        self.entry_buscar.config(width=30, font=('Arial', 12))
        self.entry_buscar.grid(row=0, column=1, padx=10, pady=10)

    def editar_artista(self):
            try:
                self.desactivar_botones()
                self.id_artista = self.tabla.item(self.tabla.selection())['text']
                self.nombre_artista = self.tabla.item(self.tabla.selection())['values'][0]
                self.alias_artista = self.tabla.item(self.tabla.selection())['values'][1]
                self.campo_artista = self.tabla.item(self.tabla.selection())['values'][2]
                self.genero_artista = self.tabla.item(self.tabla.selection())['values'][3]
                self.grupo_artista = self.tabla.item(self.tabla.selection())['values'][4]
                self.contacto_artista = self.tabla.item(self.tabla.selection())['values'][5]

                self.habilitar_campos()

                self.entry_nombre.insert(0, self.nombre_artista)
                self.entry_alias.insert(0, self.alias_artista)
                self.entry_campo.insert(0, self.campo_artista) 
                self.entry_genero.insert(0, self.genero_artista)  
                self.entry_grupo.insert(0, self.grupo_artista) 
                self.entry_contacto.insert(0, self.contacto_artista) 
            except:
                messagebox.showerror('Editar artista', 'No se ha seleccionado ningún registro.')

    def eliminar_artista(self):
        try:
            seleccionado = self.tabla.selection()
            if seleccionado:
                confirmar = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este lugar?")
                if confirmar:
                    self.desactivar_botones()
                    self.id_artista = self.tabla.item(seleccionado)['text']
                    eliminar_artista(self.id_artista)
                    self.tabla_artistas()
                    self.id_artista = None
                    messagebox.showinfo("Eliminación exitosa", "El artista ha sido eliminado exitosamente.")
                    
                    # Volver a enlazar la funcionalidad de búsqueda y selección
                    self.entry_buscar.bind("<KeyRelease>", self.buscar_datos)
                    self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_artista)
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
root.title('Gestor Cultural - Editor de Artistas')
root.resizable(0, 0)

app = EditorArtistasFrame(root)
root.mainloop()
