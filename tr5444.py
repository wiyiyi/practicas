import tkinter as tk
from tkinter import ttk,messagebox
import subprocess

def login():
    usuario = entry_usuario.get()
    clave = entry_clave.get()

    if usuario == "doc1" and clave == "1234":
        ventana.destroy()
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso") 
        ruta_archivo = "proyecto_parte_willy.py"
        subprocess.run(["python", ruta_archivo]) 

    elif usuario == "doc1" and clave != "1234":
        error("Contraseña Incorrecta")
    elif usuario != "doc1" and clave == "1234":
        error("Usuario Incorrecto")
    elif not usuario or not clave:
        messagebox.showerror("Error de inicio de sesión", "Por favor, ingrese usuario y contraseña")

def error(mensaje):
    messagebox.showerror("Intente de Nuevo", mensaje)
    entry_clave.config(bg="red") if mensaje == "Contraseña Incorrecta" else entry_usuario.config(bg="red")

def recuperar():
    ventana_recuperacion = tk.Toplevel(ventana)
    ventana_recuperacion.title("Recuperar contraseña")
    ventana_recuperacion.geometry("300x150")
    ventana_recuperacion.transient(ventana)
    ventana_recuperacion.grab_set()

    tk.Label(ventana_recuperacion, text="Introduce tu correo electrónico:", font=("Arial", 12)).pack(pady=5)
    correo_entry = tk.Entry(ventana_recuperacion, font=("Arial", 12))
    correo_entry.pack(pady=5, padx=10)

    def enviar():
        correo = correo_entry.get()
        if correo:
            messagebox.showinfo("Recuperar contraseña", f"Se ha enviado un correo de recuperación a {correo}")
            ventana_recuperacion.destroy()
        else:
            messagebox.showerror("Recuperar contraseña", "Por favor, introduce tu correo electrónico")
        enviar_button = tk.Button(ventana_recuperacion, text="Enviar Mensaje", command=enviar, font=("Arial", 12))
        enviar_button.pack(pady=5)

# Ventana de inicio
ventana = tk.Tk()
ventana.title("Bienvenido a la clínica dd")


bienvenido_label = tk.Label(ventana, text="CLINICA DEDE", font=("cocogoose 29"), fg="#85C1E9")
bienvenido_label.pack(pady=20)

marco = tk.LabelFrame(ventana, text="INICIO DE SESION", bg="#D6EAF8", relief=tk.RAISED, padx=20, pady=20,font="arial 9")
marco.pack(padx=50, pady=1)

etiquetas = [("Usuario:",0, 0), ("Contraseña:", 1, 0)]

for etiqueta, fila, columna in etiquetas:
    tk.Label(marco, text=etiqueta, bg="#D6EAF8", font=("Arial", 12)).grid(row=fila, column=columna, pady=5, sticky="w")

entry_usuario = tk.Entry(marco, font=("Arial", 12))
entry_usuario.grid(row=0, column=1, padx=10, pady=5, sticky="w")

entry_clave = tk.Entry(marco, show="*", font=("Arial", 12))
entry_clave.grid(row=1, column=1, padx=10, pady=5, sticky="w")

boton_login = tk.Button(marco, text="Iniciar Sesión", command= login, font=("Arial", 12), bg="#48C9B0", fg="white") 
boton_login.grid(row=2, columnspan=2, pady=10)

recuperar_button = tk.Button(marco, text="Recuperar contraseña", font=("Arial", 10), fg="#922B21",background="#E6B0AA", command=recuperar)
recuperar_button.grid(row=3, columnspan=2, pady=10)

ventana.bind('<Return>', lambda event=None: boton_login.invoke())

for widget in (bienvenido_label,ventana):
    widget.config(bg="#FDFEFE")


ventana.mainloop()
