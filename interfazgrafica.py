from tkinter import *
from ControladorProducto import *
from tkinter import ttk
root = Tk()
root.configure(background='white')
root.title("Sistema para la pinturería Elite S.A")
root.geometry('400x400')
entry = ttk.Entry()
def mostrar_bienvenida():
    #entry.insert(0, "Bienvenido al Sistema de Pago de Pasajes")
    texto = Label(root, text="Bienvenido al programa").grid(row=1,column=0)
    #texto = Label(root, text="Seleccione el tipo de pasaje").grid(row=1,column=0)
#entry.insert(0, "Usted ha seleccionado el pasaje convencional" )
boton1 = Button(root, text="Gestionar compra", bg="orange", padx=100,
                pady=25, command=mostrar_bienvenida).grid(row=0, column=0 )
boton2 = Button(root, text="Salir", bg="orange", padx=100,
                pady=25, command=mostrar_bienvenida).grid(row=0, column=0 )

root.mainloop()
