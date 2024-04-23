import tkinter as tk
from tkinter import messagebox
import subprocess

def regreso():
    # Cierra la ventana actual
    ventana.destroy()
    vent2= "proyecto_parte_willy.py"
    subprocess.run(["python",vent2])

def agregar_Gastos_medicos():    #producto
    Dni = entry_nombre.get().strip()
    precio = entry_precio.get().strip()
    pago = metodo_pago.get()

    if Dni != '' and precio != '':
        item = f"COST0: {Dni}, USUARIO: {precio}, PAGO: {pago}"
        if item not in lista_Gastos_medicos.get(0, tk.END):   #producto
            lista_Gastos_medicos.insert(tk.END, item)      #producto
            entry_nombre.delete(0, tk.END)
            entry_precio.delete(0, tk.END)
            metodo_pago.set("Contado")
        else:
            messagebox.showwarning(
                "Error", "Ya existe un producto con es nombre.")
    else:
        messagebox.showwarning(
            "Error", "Debes ingresar el nombre y precio del producto.")

def eliminar_Gastos_medicos():    #producto
    seleccionado = lista_Gastos_medicos.curselection() #producto
    if seleccionado:
        entry_nombre.delete(seleccionado)   #producto
        entry_nombre.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        metodo_pago.set("Contado")
    else:
        messagebox.showwarning(
            "Error", "Debes seleccionar un producto para eliminar.")

def actualizar_Gastos_medicos(): #producto
    nombre = entry_nombre.get().strip()
    precio = entry_precio.get().strip()
    pago = metodo_pago.get()

    if nombre != '' and precio != '':
        nuevo_item = f"Gastos medicos: {nombre}, Precio: {precio}, Pago: {pago}"   #producto
        seleccionado = lista_Gastos_medicos.curselection()    #producto

        if seleccionado:
            lista_Gastos_medicos.delete(seleccionado)  #producto
            lista_Gastos_medicos.insert(seleccionado, nuevo_item)     #producto
        else:
            messagebox.showwarning(
                "Error", "Debes seleccionar un producto para actualizar.")
    else:
        messagebox.showwarning(
            "Error", "Debes ingresar el nombre y precio del producto.")

def obtener_datos_item(item):
    partes = item.split(", ")
    nombre = partes[0].split(": ")[1]
    precio = partes[1].split(": ")[1]
    pago = partes[2].split(": ")[1]
    return nombre, precio, pago

ventana = tk.Tk()
ventana.title("Hospital")

frame_datos = tk.Frame(ventana)
frame_datos.place(x=20, y=20)

label_nombre = tk.Label(frame_datos, text="Monto:")
label_nombre.grid(row=0, column=0)
entry_nombre = tk.Entry(frame_datos)
entry_nombre.grid(row=0, column=1)

label_precio = tk.Label(frame_datos, text="Codigo De Usuario:")
label_precio.grid(row=1, column=0)
entry_precio = tk.Entry(frame_datos)
entry_precio.grid(row=1, column=1)
frame_datos.pack()

frame_pago = tk.Frame(ventana)
frame_pago.place(x=20, y=70)

metodo_pago = tk.StringVar(value="Contado")

label_pago = tk.Label(frame_pago, text="Método de pago:")
label_pago.pack()

radio_contado = tk.Radiobutton(
    frame_pago, text="Contado", variable=metodo_pago, value="Contado")
radio_contado.pack()

radio_credito = tk.Radiobutton(
    frame_pago, text="Crédito", variable=metodo_pago, value="Crédito")
radio_credito.pack()
frame_pago.pack()

regreso=tk.Button(ventana,text="REGRESAR",command=regreso)
regreso.pack()


frame_botones = tk.Frame(ventana)
frame_botones.place(x=200, y=130)

boton_agregar = tk.Button(
    frame_botones, text="Agregar", command=agregar_Gastos_medicos)  #producto
boton_agregar.pack()

boton_eliminar = tk.Button( 
    frame_botones, text="Eliminar", command=eliminar_Gastos_medicos)    #producto
boton_eliminar.pack()


frame_botones.pack()

frame_lista = tk.Frame(ventana)
frame_lista.place(x=20, y=220)

def calculate_total(self):
        total = sum(product.price * product.quantity for product in self.products)
        self.total_label.config(text=f"Total: ${total:.2f}")

lista_Gastos_medicos = tk.Listbox(frame_lista, width=50, height=10)
lista_Gastos_medicos.pack()
frame_lista.pack()
ventana.mainloop()