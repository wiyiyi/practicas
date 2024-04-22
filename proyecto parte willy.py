import tkinter as tk
from tkinter import messagebox
import subprocess

def validar_login():
    usuario = entry_usuario.get()
    clave = entry_clave.get()

    if usuario == "doc1" and clave == "1234":
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso") 
        abrir_proyecto()

    elif usuario == "doc1" and clave != "1234":
        mostrar_error("Contraseña Incorrecta")
    elif usuario != "doc1" and clave == "1234":
        mostrar_error("Usuario Incorrecto")
    elif not usuario or not clave:
        messagebox.showerror("Error de inicio de sesión", "Por favor, ingrese usuario y contraseña")

def mostrar_error(mensaje):
    messagebox.showerror("Intente de Nuevo", mensaje)
    entry_clave.config(bg="red") if mensaje == "Contraseña Incorrecta" else entry_usuario.config(bg="red")

def abrir_proyecto():
    ruta_archivo = "proyecto_parte_willy.py"
    subprocess.run(["python", ruta_archivo])
    ventana.destroy()

def recuperar():
    ventana_recuperacion = tk.Toplevel(ventana)
    ventana_recuperacion.title("Recuperar contraseña")
    ventana_recuperacion.geometry("300x150")
    ventana_recuperacion.transient(ventana)
    ventana_recuperacion.grab_set()

    tk.Label(ventana_recuperacion, text="Introduce tu correo electrónico:", font=("Arial", 12)).pack(pady=5)
    correo_entry = tk.Entry(ventana_recuperacion, font=("Arial", 12))
    correo_entry.pack(pady=5, padx=10)

    def enviar_correo():
        correo = correo_entry.get()
        if correo:
            messagebox.showinfo("Recuperar contraseña", f"Se ha enviado un correo de recuperación a {correo}")
            ventana_recuperacion.destroy()
        else:
            messagebox.showerror("Recuperar contraseña", "Por favor, introduce tu correo electrónico")

    enviar_button = tk.Button(ventana_recuperacion, text="Enviar Mensaje", command=enviar_correo, font=("Arial", 12))
    enviar_button.pack(pady=5)

# Ventana de inicio
ventana = tk.Tk()
ventana.title("Bienvenido a la clínica dd")
ventana.configure(bg="#E0E0E0")

bienvenido_label = tk.Label(ventana, text="Bienvenido", font="Arial 16 bold", bg="#E0E0E0", fg="#460202")
bienvenido_label.pack(pady=20)

# Marco para etiquetas e inputs
marco = tk.LabelFrame(ventana, text="Inicio de Sesión", bg="#BDBDBD", relief=tk.RAISED, padx=20, pady=20)
marco.pack(padx=50, pady=20)

etiquetas = [("Usuario:", 0, 0), ("Contraseña:", 1, 0)]

for etiqueta, fila, columna in etiquetas:
    tk.Label(marco, text=etiqueta, bg="#BDBDBD", font=("Arial", 12)).grid(row=fila, column=columna, pady=5, sticky="w")

entry_usuario = tk.Entry(marco, font=("Arial", 12))
entry_usuario.grid(row=0, column=1, padx=10, pady=5, sticky="w")

entry_clave = tk.Entry(marco, show="*", font=("Arial", 12))
entry_clave.grid(row=1, column=1, padx=10, pady=5, sticky="w")

boton_login = tk.Button(marco, text="Iniciar Sesión", command=validar_login, font=("Arial", 12), bg="#4CAF50", fg="white") 
boton_login.grid(row=2, columnspan=2, pady=10)

recuperar_button = tk.Button(marco, text="Recuperar contraseña", font=("Arial", 10), fg="blue", command=recuperar)
recuperar_button.grid(row=3, columnspan=2, pady=10)

ventana.bind('<Return>', lambda event=None: boton_login.invoke())

ventana.mainloop()