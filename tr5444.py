import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk

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
    ventana_enfermedades.geometry("300x150")

    

    # Crear un marco para organizar los widgets
    frame_enfermedades = ttk.LabelFrame(ventana_enfermedades, text="Enfermedades", labelanchor="n")
    frame_enfermedades.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Lista de enfermedades
    enfermedades = ["Cáncer de Mama", "Cáncer de Pulmón", "Cáncer de Colon", "Cáncer de Páncreas", "Cáncer de Próstata"]

    # Variable de control para la selección de la enfermedad
    selected_disease = tk.StringVar()
    selected_disease.set(enfermedades[0])

    # Menú desplegable para seleccionar la enfermedad
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
    ventana_tratamiento.geometry("400x250")
    ventana_tratamiento.config(background="#FFFFFF")

    # Crear un marco para organizar los widgets
    frame_tratamiento = ttk.LabelFrame(ventana_tratamiento, text="Tratamiento para " + enfermedad, labelanchor="n")
    frame_tratamiento.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Etiqueta y campo de entrada para el tratamiento
    label_tratamiento = ttk.Label(frame_tratamiento, text="Tratamiento:")
    label_tratamiento.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_tratamiento = ttk.Entry(frame_tratamiento)
    entry_tratamiento.grid(row=0, column=1, padx=5, pady=5)

    # Etiqueta y campo de entrada para el precio
    label_precio = ttk.Label(frame_tratamiento, text="Precio:")
    label_precio.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_precio = ttk.Entry(frame_tratamiento)
    entry_precio.grid(row=1, column=1, padx=5, pady=5)

    # Etiqueta y campo de entrada para los meses
    label_meses = ttk.Label(frame_tratamiento, text="Meses:")
    label_meses.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entry_meses = ttk.Entry(frame_tratamiento)
    entry_meses.grid(row=2, column=1, padx=5, pady=5)

    # Botón para cobrar el tratamiento
    button_cobrar = ttk.Button(frame_tratamiento, text="Cobrar", command=lambda: cobrar_tratamiento(ventana_tratamiento, entry_tratamiento.get(), entry_precio.get(), entry_meses.get()))
    button_cobrar.grid(row=3, columnspan=2, padx=5, pady=10, sticky="ew")

    ventana_tratamiento.bind('<Return>', lambda event=None: button_cobrar.invoke())

    ventana_tratamiento.mainloop()

# Función para calcular los intereses
def calcular_intereses(monto, meses):
    intereses = 0
    for mes in range(1, meses + 1):
        tasa = min(mes * 5, 25) / 100  # Tasa de interés escalonada
        intereses += monto * tasa
    return intereses

# Función para cobrar el tratamiento
def cobrar_tratamiento(ventana_tratamiento, tratamiento, precio, meses):
    # Validar si se ingresaron datos
    if tratamiento and precio and meses:
        monto = float(precio)
        meses = int(meses)
        intereses = calcular_intereses(monto, meses)
        monto_total = monto + intereses
        
        # Mostrar el ticket de cobro
        mostrar_ticket(tratamiento, monto, intereses, monto_total)
        
        # Mostrar mensaje de éxito
        messagebox.showinfo("Cobro", f"El cobro se realizó con éxito.\nTotal a pagar: ${monto_total:.2f}")
        
        ventana_tratamiento.destroy()
        graficar_gastos(monto, intereses, monto_total, meses)
    else:
        messagebox.showerror("Error", "Por favor ingrese el tratamiento, el precio y los meses.")

# Función para mostrar el ticket de cobro
def mostrar_ticket(tratamiento, monto, intereses, monto_total):
    ticket_info = f"Tratamiento: {tratamiento}\n\n"
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

# Configuración de la ventana de inicio de sesión
import tkinter as tk


# Crear ventana principal
ventana_login = tk.Tk()
ventana_login.title("Inicio de Sesión")
ventana_login.geometry("410x400") 
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


imagen = Image.open("h.png")
imagen = imagen.resize((50, 50))  # Redimensionar la imagen si es necesario
imagen_tk = ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(marco, image=imagen_tk,bg="#D6EAF8")
label_imagen.grid(padx=30, pady=2,row=3,column=0)

imagen2 = Image.open("pacman.png")
imagen2 = imagen2.resize((50, 50))  # Redimensionar la imagen si es necesario
imagen_tk2 = ImageTk.PhotoImage(imagen2)
label_imagen2 = tk.Label(ventana_login, image=imagen_tk2,bg="#FFFFFF")
label_imagen2.pack()


ventana_login.bind('<Return>', lambda event=None: boton_login.invoke())

# Iniciar el bucle principal
ventana_login.mainloop()
