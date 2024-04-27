import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
from conexion2 import *
from clientes import *

global entry_precio
entry_precio = None

global entry_meses 
entry_meses = None

global entry_peso
entry_peso = None

global entry_nombre
entry_nombre = None

global combo_tipo_sangre
combo_tipo_sangre = None

global entry_edad
entry_edad = None

global combo_tratamiento
combo_tratamiento = None



# Función para validar el inicio de sesión
def validar_login():
    usuario = entry_usuario.get()
    clave = entry_clave.get()

    # Comprobar las credenciales
    if usuario == "" and clave == "":
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
        abrir_ventana_enfermedades()
    else:
        messagebox.showerror("Inicio de sesión", "Usuario o contraseña incorrectos")

# Función para abrir la ventana de enfermedades
def abrir_ventana_enfermedades():
    # Cerrar la ventana de inicio de sesión
    ventana_login.destroy()

    # Crear la ventana de enfermedades
    ventana_enfermedades = tk.Tk()
    ventana_enfermedades.title("Selección de Enfermedad")
    ventana_enfermedades.geometry("")

    # Crear un marco para organizar los widgets
    frame_enfermedades = ttk.LabelFrame(ventana_enfermedades, text="Enfermedades", labelanchor="n")
    frame_enfermedades.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Lista de enfermedades
    enfermedades = ["Cáncer de Mama", "Cáncer de Pulmón", "Cáncer de Colon", "Cáncer de Páncreas", "Cáncer de Próstata"]

    # Variable de control para la selección de la enfermedad
    selected_disease = tk.StringVar()
    selected_disease.set(enfermedades[0])

    # Menú desplegable para seleccionar la enfermedad
    #ENTRY 1
    dropdown_enfermedades = ttk.Combobox(frame_enfermedades, textvariable=selected_disease, values=enfermedades)
    dropdown_enfermedades.grid(row=0, column=0, padx=5, pady=5)

    # Botón para confirmar la selección y abrir la ventana de tratamiento
    button_seleccionar = ttk.Button(frame_enfermedades, text="Seleccionar", command=lambda: abrir_ventana_tratamiento(ventana_enfermedades, selected_disease.get()))
    button_seleccionar.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    ventana_enfermedades.bind('<Return>', lambda event=None: button_seleccionar.invoke())

    ventana_enfermedades.mainloop()

# Función para abrir la ventana de tratamiento
def abrir_ventana_tratamiento(ventana_enfermedades, enfermedad):
    # Cerrar la ventana de enfermedades
    ventana_enfermedades.destroy()

    # Crear la ventana de tratamiento
    ventana_tratamiento = tk.Tk()
    ventana_tratamiento.title("Tratamiento para " + enfermedad)
    ventana_tratamiento.geometry("")
    ventana_tratamiento.config(background="#FFFFFF")

    # Crear un marco para organizar los widgets
    frame_tratamiento = ttk.LabelFrame(ventana_tratamiento, text="Tratamiento para " + enfermedad, labelanchor="n")
    frame_tratamiento.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Campos de entrada para datos del paciente
    ttk.Label(frame_tratamiento, text="Nombre del paciente:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_nombre = ttk.Entry(frame_tratamiento)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    ttk.Label(frame_tratamiento, text="Edad:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_edad = ttk.Entry(frame_tratamiento)
    entry_edad.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    # Combobox para el sexo
    ttk.Label(frame_tratamiento, text="Sexo:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    combo_sexo = ttk.Combobox(frame_tratamiento, values=["Masculino", "Femenino"])
    combo_sexo.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    # Combobox para el tipo de sangre
    ttk.Label(frame_tratamiento, text="Tipo de Sangre:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    combo_tipo_sangre = ttk.Combobox(frame_tratamiento, values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
    combo_tipo_sangre.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    ttk.Label(frame_tratamiento, text="Peso:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
    entry_peso = ttk.Entry(frame_tratamiento)
    entry_peso.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    ttk.Label(frame_tratamiento, text="Estatura:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
    entry_estatura = ttk.Entry(frame_tratamiento)
    entry_estatura.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    # Combobox para el tratamiento
    ttk.Label(frame_tratamiento, text="Tratamiento:").grid(row=6, column=0, padx=5, pady=5, sticky="w")
    combo_tratamiento = ttk.Combobox(frame_tratamiento, values=["Terapia hormonal", "Quimioterapia", "Hiperterapia", "Terapia láser", "Crioterapia", "Terapia de células madre", "Radioterapia", "Cirugía"])
    combo_tratamiento.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    ttk.Label(frame_tratamiento, text="Precio:").grid(row=7, column=0, padx=5, pady=5, sticky="w")
    #ENTRY 2 PRECIO
    entry_precio = tk.Entry(frame_tratamiento)
    entry_precio.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    ttk.Label(frame_tratamiento, text="Meses:").grid(row=8, column=0, padx=5, pady=5, sticky="w")
    #ENTRY 3 MESES
    entry_meses = tk.Entry(frame_tratamiento)
    entry_meses.grid(row=8, column=1, padx=5, pady=5, sticky="w")

    # Botón para cobrar el tratamiento
    button_cobrar = ttk.Button(frame_tratamiento, text="Cobrar", command=lambda: cobrar_tratamiento(ventana_tratamiento, entry_nombre.get(), int(entry_edad.get()), combo_sexo.get(), combo_tipo_sangre.get(), entry_peso.get(), entry_estatura.get(), combo_tratamiento.get(), entry_precio.get(), entry_meses.get()))
    button_cobrar.grid(row=9, columnspan=2, padx=5, pady=10, sticky="ew")

    ventana_tratamiento.bind('<Return>', lambda event=None: button_cobrar.invoke())

    
    ventana_tratamiento.mainloop()

# Función para calcular los intereses
def calcular_intereses(monto, meses):
    intereses = 0
    for mes in range(1, meses + 1):
        tasa = min(mes * 5, 5) / 100  # Tasa de interés escalonada
        intereses += monto * tasa
    return intereses

# Función para cobrar el tratamiento
def cobrar_tratamiento(ventana_tratamiento, nombre, edad, sexo, tipo_sangre, peso, estatura, tratamiento, precio, meses):
    guardar_registro()
    # Validar si se ingresaron datos
    if nombre and edad and sexo and tipo_sangre and peso and estatura and tratamiento and precio and meses:
        monto = float(precio)
        meses = int(meses)
        intereses = calcular_intereses(monto, meses)
        monto_total = monto + intereses
        CCLIENTES.ingresar_clientes(nombre,edad,tipo_sangre,peso,precio,meses,tratamiento)
        # Mostrar el ticket de cobro
       
        mostrar_ticket(nombre, edad, sexo, tipo_sangre, peso, estatura, tratamiento, monto, intereses, monto_total)
        #guardar_registro()
        # Mostrar mensaje de éxito
        messagebox.showinfo("Cobro", f"El cobro se realizó con éxito.\nTotal a pagar: ${monto_total:.2f}")
        
        ventana_tratamiento.destroy()
        graficar_gastos(monto, intereses, monto_total, meses)
        graficar_vida1(int(edad))
        graficar_vida2(int(edad))
    else:
        messagebox.showerror("Error", "Por favor ingrese todos los datos del paciente y del tratamiento.")

# Función para mostrar el ticket de cobro
def mostrar_ticket(nombre, edad, sexo, tipo_sangre, peso, estatura, tratamiento, monto, intereses, monto_total):
    ticket_info = f"Datos del Paciente:\n"
    ticket_info += f"Nombre: {nombre}\n"
    ticket_info += f"Edad: {edad}\n"
    ticket_info += f"Sexo: {sexo}\n"
    ticket_info += f"Tipo de Sangre: {tipo_sangre}\n"
    ticket_info += f"Peso: {peso}\n"
    ticket_info += f"Estatura: {estatura}\n\n"
    ticket_info += f"Tratamiento: {tratamiento}\n\n"
    ticket_info += f"Subtotal: ${monto:.2f}\n"
    ticket_info += f"Intereses: ${intereses:.2f}\n"
    ticket_info += f"Total a pagar: ${monto_total:.2f}"
    
    messagebox.showinfo("Ticket de Cobro", ticket_info)

# Función para graficar los gastos mensuales
def graficar_gastos(monto, intereses, monto_total, meses):
    # Crear los datos para la gráfica de línea
    x = np.arange(1, meses + 1)
    y = [monto + calcular_intereses(monto, mes) for mes in range(1, meses + 1)]

    # Crear la figura y el gráfico de línea
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-')

    # Configurar etiquetas
    ax.set_xlabel('Meses', fontsize=12)
    ax.set_ylabel('Monto ($)', fontsize=12)
    ax.set_title('INTERESES MENSUALES', fontsize=14)

    plt.show()


# Función para graficar la esperanza de vida
def graficar_vida1(edad):
    # Crear los datos para la gráfica de línea
    
    y=[]
    cantidad=0
    probabilidad=90
    while(probabilidad>=0):
        y.append(probabilidad)
        probabilidad-=14.25
        cantidad+=1
    x = np.arange(edad, edad+cantidad)

    # Crear la figura y el gráfico de línea
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-')

    # Configurar etiquetas
    ax.set_xlabel('Años', fontsize=12)
    ax.set_ylabel('porcentaje de vida', fontsize=12)
    ax.set_title('años de vida extra', fontsize=14)

    plt.show()


# Función para graficar la esperanza de vida
def graficar_vida2(edad):
    # Crear los datos para la gráfica de línea
    
    y=[]
    cantidad=0
    probabilidad=150
    while(probabilidad>=0):
        y.append(probabilidad)
        probabilidad-=14.25
        cantidad+=1
    x = np.arange(edad, edad+cantidad)

    # Crear la figura y el gráfico de línea
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-')

    # Configurar etiquetas
    ax.set_xlabel('Años', fontsize=12)
    ax.set_ylabel('porcentaje de vida', fontsize=12)
    ax.set_title('años de vida extra', fontsize=14)

    plt.show()

#def prueba 
def guardar_registro():
     
  global entry_precio,entry_meses,entry_edad,entry_peso,combo_tratamiento,combo_tipo_sangre,entry_nombre

  try:
     if  entry_precio is None or entry_meses is None:
         print("no estan inizializados")
         return

     nombre =entry_nombre.get()
     edad=entry_edad.get()
     peso= entry_peso.get()
     precio = entry_precio.get()
     meses = entry_meses.get()
     tipo_sangre = combo_tipo_sangre.get()
     tratamiento = combo_tratamiento.get()

     CCLIENTES.ingresar_clientes(nombre,edad,tipo_sangre,peso,precio,meses,tratamiento)
     messagebox.showinfo("informacion","los datos fueron ingresados")

     #limpiar campos

     entry_precio.delete(0,tk.END)
     entry_meses.delete(0,tk.END)
     entry_nombre.delete(0,tk.END)
     entry_edad.delete(0,tk.END)
     entry_peso.delete(0,tk.END)
     combo_tipo_sangre.delete(0,tk.END)
     combo_tratamiento.delete(0,tk.END)


  except ValueError:
     print("Error al ingresar los datos")
     


# Configuración de la ventana de inicio de sesión
ventana_login = tk.Tk()
ventana_login.title("Inicio de Sesión")
ventana_login.geometry("") 
ventana_login.config(background="#FDFEFE")

# Etiqueta de bienvenida
bienvenida_label = tk.Label(ventana_login, text="BIENVENIDO A CLINICA MART", font=("Georgia", 12,"bold"), fg="#85C1E9", background="#FDFEFE")
bienvenida_label.pack(padx=(30),fill="both")  

# Marco para el formulario de inicio de sesión
marco = tk.LabelFrame(ventana_login, text="INICIO DE SESION", bg="#D6EAF8", relief=tk.RAISED, font="Arial 8")
marco.pack(padx=20, pady=10)


etiquetas = [("Usuario:", 0, 0), ("Contraseña:", 1, 0)]

for etiqueta, fila, columna in etiquetas:
    tk.Label(marco, text=etiqueta, bg="#D6EAF8", font=("Centaur", 15)).grid(row=fila, column=columna, pady=5, sticky="we")

entry_usuario = tk.Entry(marco, font=("Arial", 12),relief=tk.FLAT)
entry_usuario.grid(row=0, column=1, padx=10, pady=5, sticky="w")

entry_clave = tk.Entry(marco, show="*", font=("Arial", 12),relief=tk.FLAT)
entry_clave.grid(row=1, column=1, padx=10, pady=5, sticky="w")

boton_login = tk.Button(marco, text="Iniciar Sesión", command=validar_login, font=("Arial", 12), bg="#48C9B0", fg="white")
boton_login.grid(row=2, columnspan=2, sticky="") 

recuperar_button = tk.Button(marco, text="Recuperar contraseña", font=("Arial", 10), fg="#922B21", bg="#E6B0AA", command="")
recuperar_button.grid(row=3, columnspan=2, pady=10, sticky="")  

ventana_login.bind('<Return>', lambda event=None: boton_login.invoke())

# Iniciar el bucle principal

ventana_login.mainloop()



