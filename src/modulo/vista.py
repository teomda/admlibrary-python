import tkinter as tk
from tkinter import ttk

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width=480,height=320)
        self.root = root
        self.pack()
        self.config(bg='green')
        self.label_form()
        self.input_form()
        self.action_buttons()
        
    def label_form(self):
        self.label_nombre = tk.Label(self,text='Nombre')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)
        
        self.label_nombre = tk.Label(self,text='Apellido')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=1,column=0,padx=10,pady=10)
        
    def input_form(self):
        self.entry_name = ttk.Entry(self)
        self.entry_name.config(width=50,state='disabled')
        self.entry_name.grid(row=0,column=1,padx=10,pady=10)
        
        self.entry_lastname = ttk.Entry(self)
        self.entry_lastname.config(width=50,state='disabled')
        self.entry_lastname.grid(row=1,column=1,padx=10,pady=10)

        self.entry_genero = ttk.Combobox(self, state="readonly")
        self.entry_genero.config(width=25, state='disabled')
        self.entry_genero.bind("<<ComboboxSelected>>")
        self.entry_genero.grid(row= 2, column=1,padx=10,pady=10)
 
    def action_buttons(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.btn_alta.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,
    bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_alta.grid(row= 3, column=0,padx=10,pady=10)
        self.btn_modi = tk.Button(self, text='Guardar')
        self.btn_modi.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,
    bg='#0D2A83',cursor='hand2',activebackground='#7594F5',activeforeground='#000000')
        self.btn_modi.grid(row= 3, column=1,padx=10,pady=10)
        self.btn_cance = tk.Button(self, text='Cancelar',command=self.bloquear_campos)
        self.btn_cance.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,
    bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_cance.grid(row= 3, column=2,padx=10,pady=10)
    
    def habilitar_campos(self):
        self.entry_name.config(state='normal')
        self.entry_lastname.config(state='normal')
        self.entry_genero.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')
        
    def bloquear_campos(self):
        self.entry_name.config(state='disabled')
        self.entry_lastname.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.btn_alta.config(state='normal')

            
def create_menu(root): 
    rootMenu = tk.Menu(root)
    root.config(menu = rootMenu, width = 300 , height = 300)
    menu_inicio = tk.Menu(rootMenu, tearoff=0)
    # niveles #
    #principal
    rootMenu.add_cascade(label='Inicio', menu = menu_inicio)
    rootMenu.add_cascade(label='Consultas', menu = menu_inicio)
    rootMenu.add_cascade(label='Acerca de.', menu = menu_inicio)
    rootMenu.add_cascade(label='Ayuda', menu = menu_inicio)
    #submenu
    menu_inicio.add_command(label='Conectar DB')
    menu_inicio.add_command(label='Desconectar DB')
    menu_inicio.add_command(label='Salir', command= root.destroy)