import tkinter as tk
import sys
sys.path.append("C:/Users/josef/proyectos/proyecto-integrador/gestor-cultural")
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import *
from tkinter import messagebox
from model.evento_dao import Evento, guardar, listar, editar, eliminar, obtener_id_artistas_eventos,  obtener_id_eventos_lugares
from model.artista_dao import obtener_artistas
from model.lugar_dao import obtener_lugares

class EditorFrame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg='purple')
        
        self.id_evento = None
        self.eventos()
        self.deshabilitar_campos()
        self.tabla_eventos()
        self.entry_buscar.bind("<KeyRelease>", self.buscar_datos)
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_evento)
    
    def eventos(self):
#--------------------------------------------------------Labels de entrada----------------------------------------------
        self.label_nombre = tk.Label(self, text='Nombre del evento: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'), fg='white', bg = 'purple')
        self.label_nombre.grid(row=2, column=0, padx=10, pady=10)

        self.label_tipo = tk.Label(self, text='Tipo de evento: ')
        self.label_tipo.config(font=('Arial', 12, 'bold'), fg='white', bg = 'purple')
        self.label_tipo.grid(row=3, column=0, padx=10, pady=10) 

        self.label_fecha = tk.Label(self, text='Fecha de inicio / Estreno / Apertura : ')
        self.label_fecha.config(font=('Arial', 12, 'bold'), fg='white', bg = 'purple')
        self.label_fecha.grid(row=4, column=0, padx=10, pady=10) 

        self.label_precio = tk.Label(self, text='Precio de entrada (ARS): ')
        self.label_precio.config(font=('Arial', 12, 'bold'), fg='white', bg = 'purple')
        self.label_precio.grid(row=5, column=0, padx=10, pady=10)

        self.label_lugar = tk.Label(self, text='Lugar del evento: ')
        self.label_lugar.config(font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.label_lugar.grid(row=6, column=0, padx=10, pady=10)

        self.label_artistas = tk.Label(self, text='Artistas asistentes: ')
        self.label_artistas.config(font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.label_artistas.grid(row=7, column=0, padx=10, pady=10)

#------------------------------------------- ingreso de datos -----------------------------------------------------

        self.evento_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.evento_nombre)
        self.entry_nombre.config(width= 50, font = ('Arial', 12))
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10)

        self.evento_tipo = tk.StringVar()
        self.entry_tipo = tk.Entry(self, textvariable = self.evento_tipo)
        self.entry_tipo.config(width= 50, font = ('Arial', 12))
        self.entry_tipo.grid(row=3, column=1, padx=10, pady=10)

        self.evento_fecha = tk.StringVar()
        self.entry_fecha = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.entry_fecha.grid(row=4, column=1, padx=10, pady=10)
        self.entry_fecha.config(font=('Arial', 12))

        self.evento_precio = tk.StringVar()
        self.entry_precio = tk.Entry(self, textvariable = self.evento_precio)
        self.entry_precio.config(width=50, font = ('Arial', 12))
        self.entry_precio.grid(row=5, column=1, padx=10, pady=10)

        self.lugares = ttk.Combobox(self)
        self.lugares.config(width=30, font=('Arial', 12))
        self.lugares.grid(row=6, column=1, padx=10, pady=10)
        lugares = obtener_lugares()
        self.lugares['values'] = [lugar[1] for lugar in lugares]

        self.artistas = ttk.Combobox(self)
        self.artistas.config(width=30, font=('Arial', 12))
        self.artistas.grid(row=7, column=1, padx=10, pady=10)
        artistas = obtener_artistas()
        self.artistas['values'] = [artista[1] for artista in artistas]

        self.lugares_dict = {lugar[1]: lugar[0] for lugar in lugares}
        self.artistas_dict = {artista[1]: artista[0] for artista in artistas} 

#-------------------------------------------------------------- Botonera ---------------------------------------------------------
        
        self.boton_nuevo = tk.Button(self, text="Crear evento", command= self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg = 'white', bg = 'blue', cursor = 'hand2', activebackground = '#D2302E')
        self.boton_nuevo.grid(row=2, column=3, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar evento", command = self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'), fg = 'white', bg = 'green', cursor = 'hand2', activebackground = '#2ED231')
        self.boton_guardar.grid(row=3, column=3, padx=10, pady=10)
        
        self.boton_cancelar = tk.Button(self, text="Cancelar", command = self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg = 'white', bg = 'blue', cursor = 'hand2', activebackground = '#D2302E')
        self.boton_cancelar.grid(row=4, column=3, padx=10, pady=10)

    def habilitar_campos(self):
        self.boton_nuevo.config(state='disabled')
        self.evento_nombre.set('')
        self.evento_tipo.set('')
        self.evento_fecha.set('')
        self.evento_precio.set('') 

        self.entry_nombre.config(state='normal')
        self.entry_tipo.config(state='normal')
        self.entry_fecha.config(state='normal')
        self.entry_precio.config(state='normal')
        self.lugares.config(state='normal')
        self.artistas.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):
         self.entry_nombre.delete(0, END)
         self.entry_tipo.delete(0, END)
         self.entry_fecha.delete(0, END)
         self.entry_precio.delete(0, END)     
         
         self.entry_nombre.config(state='disabled')
         self.entry_tipo.config(state='disabled')
         self.entry_fecha.config(state='disabled')
         self.entry_precio.config(state='disabled')

         self.lugares.set('')
         self.artistas.set('')
         self.lugares.config(state='disabled')
         self.artistas.config(state='disabled')

         self.boton_guardar.config(state='disabled')
         self.boton_cancelar.config(state='disabled')
         self.boton_nuevo.config(state='normal')

    def desactivar_botones(self):
        self.editar.config(state='disabled')
        self.eliminar.config(state='disabled')

    def seleccionar_evento(self, event):
        seleccionado = self.tabla.selection()
        if seleccionado:
            self.editar.config(state='normal')
            self.eliminar.config(state='normal')
        else:
            self.desactivar_botones()

    def guardar_datos(self):
         id_artista = self.artistas_dict[self.artistas.get()]
         id_lugar = self.lugares_dict[self.lugares.get()]
         evento = Evento(
              self.evento_nombre.get(),
              self.evento_tipo.get(),
              self.entry_fecha.get(),
              self.evento_precio.get(),
              id_lugar,
              id_artista
         )

         if self.id_evento == None:
            guardar(evento)
            self.tabla_eventos()    
            self.deshabilitar_campos()
            
         else:
            editar(evento, self.id_evento)
            self.tabla_eventos()
            self.deshabilitar_campos()

         self.desactivar_botones()
         self.boton_nuevo.config(state='normal')  
         
         titulo = 'Agregar evento'
         mensaje = 'Evento agregado con éxito'
         messagebox.showinfo(titulo, mensaje)

         self.entry_buscar.bind("<KeyRelease>", self.buscar_datos)
         self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_evento)

    def tabla_eventos(self):
        self.lista_eventos = listar()

        self.tabla = ttk.Treeview(self, column=('Nombre','Tipo','Fecha','Precio'))
        self.tabla.grid(row=1, column=0, columnspan=6, sticky= 'nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=1, column=6, sticky='nse')
        self.tabla.configure(yscrollcommand = self.scroll.set)

        self.tabla.heading('#0', text='ID')      
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Tipo')
        self.tabla.heading('#3', text='Fecha')
        self.tabla.heading('#4', text='Precio')
        
        #Se itera la lista de eventos
        for evento in self.lista_eventos:
            self.tabla.insert('', 0, text=evento[0], values =(evento[1], evento[2], evento[3], evento[4]))

#--------------------------Editar y eliminar---------------------------
        self.editar = tk.Button(self, text="Editar evento", command=self.editar_evento, state='disabled')
        self.editar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='green', cursor='hand2', activebackground='#2ED231')
        self.editar.grid(row=5, column=3, padx=10, pady=10)

        self.eliminar = tk.Button(self, text="Eliminar evento", command=self.eliminar_evento, state='disabled')
        self.eliminar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='blue', cursor='hand2', activebackground='#D2302E')
        self.eliminar.grid(row=6, column=3, padx=10, pady=10)

        self.label_buscar = tk.Label(self, text="Buscar:")
        self.label_buscar.config(font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.label_buscar.grid(row=0, column=0, padx=10, pady=10)

        self.entry_buscar = tk.Entry(self)
        self.entry_buscar.config(width=30, font=('Arial', 12))
        self.entry_buscar.grid(row=0, column=1, padx=10, pady=10)

    def editar_evento(self):
        try:
            self.desactivar_botones()
            seleccion = self.tabla.selection()
            print("Seleccionado:", seleccion)
            if seleccion:
                evento_seleccionado = self.tabla.item(seleccion)
                print("Valores de la selección:", evento_seleccionado)
                self.id_evento = evento_seleccionado['text']
                self.nombre_evento = evento_seleccionado['values'][0]
                self.tipo_evento = evento_seleccionado['values'][1]
                self.fecha_evento = evento_seleccionado['values'][2]
                self.precio_evento = evento_seleccionado['values'][3]

                # Obtener el ID del artista desde la tabla artistas_eventos
                id_artista_evento = obtener_id_artistas_eventos(self.id_evento)
                
                # Obtener el ID del lugar desde la tabla lugares_eventos
                id_lugar_evento = obtener_id_eventos_lugares(self.id_evento)

                self.habilitar_campos()

                self.entry_nombre.insert(0, self.nombre_evento)
                self.entry_tipo.insert(0, self.tipo_evento)
                self.entry_fecha.insert(0, self.fecha_evento)
                self.entry_precio.insert(0, self.precio_evento)

                # Obtener la lista de artistas y lugares
                artistas = obtener_artistas()
                lugares = obtener_lugares()

                print("Artistas:", artistas)
                print("Lugares:", lugares)

                # Establecer los valores del ComboBox de artistas y lugares
                self.artistas['values'] = [artista[1] for artista in artistas]
                self.artistas.set([artista[1] for artista in artistas if artista[0] == id_artista_evento][0])

                self.lugares['values'] = [lugar[1] for lugar in lugares]
                self.lugares.set([lugar[1] for lugar in lugares if lugar[0] == id_lugar_evento][0])
            else:
                messagebox.showerror('Editar evento', 'No se ha seleccionado ningún registro.')
        except Exception as e:
            messagebox.showerror('Editar evento', f'Error al editar evento: {str(e)}')



    def eliminar_evento(self):
        try:
            seleccionado = self.tabla.selection()
            if seleccionado:
                confirmar = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este evento?")
                if confirmar:
                    self.desactivar_botones()
                    self.id_evento = self.tabla.item(seleccionado)['text']
                    eliminar(self.id_evento)
                    self.tabla_eventos()
                    self.id_evento = None
                    messagebox.showinfo("Evento eliminado", "El evento ha sido eliminado correctamente.")

                    self.entry_buscar.bind("<KeyRelease>", self.buscar_datos)
                    self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_evento)
            else:
                messagebox.showerror("Eliminar un Registro", "No ha seleccionado ningún registro para eliminar.")
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
root.title('Gestor Cultural - Editor de Eventos')
root.resizable(0, 0)

app = EditorFrame(root)
root.mainloop()