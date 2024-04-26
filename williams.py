import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk  

def cerrar():
    ventana.destroy()
    subprocess.run(["python", ventana])

def validar_login():
    usuario = entry_usuario.get()
    clave = entry_clave.get()

    if usuario == "1" and clave == "1":
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
        ventana.destroy()
        ruta_archivo = "luzlistaproductos.py"
        subprocess.run(["python", ruta_archivo])
    else:
        messagebox.showerror("Inicio de sesión", "Usuario o contraseña incorrectos")

ventana = tk.Tk()
ventana.title("El Rincon del Gamer")

# Centrar la ventana
ancho_ventana = 800
alto_ventana = 600
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

imagen3 = Image.open("willy.png")
imagen = imagen3.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()))
imagen_tk3 = ImageTk.PhotoImage(imagen3)
label_imagen3 = tk.Label(ventana, image=imagen_tk3)
label_imagen3.place(x=0, y=0, relwidth=1, relheight=1)

etiqueta = tk.Label(text="Bienvenido", font=("MC Ten Lowercase Alt", 30, "bold"), bg="#2a0b46", fg="#FFFFFF")
etiqueta.pack()

titulo = tk.Label(text="Al Rincon del Gamer", font=("MC Ten Lowercase Alt", 20, "bold"), bg="#2a0b46", fg="#FFFFFF")
titulo.pack()

frame = tk.LabelFrame(ventana)
frame.config(bg="#0E0024", bd=5, relief=tk.RAISED)
frame.pack(expand=True)

def click_u(event):
    if entry_usuario.get() == "Usuario":
        entry_usuario.delete(0, tk.END)
        entry_usuario.config(fg='black')

def sombra_u(event):
    if entry_usuario.get() == '':
        entry_usuario.insert(0, "Usuario")
        entry_usuario.config(fg='grey')

def click_c(event):
    if entry_clave.get() == "Contraseña":
        entry_clave.delete(0, tk.END)
        entry_clave.config(fg='black')

def sombra_c(event):
    if entry_clave.get() == '':
        entry_clave.insert(0, "Contraseña")
        entry_clave.config(fg='grey')

texto_dentro_N = tk.StringVar()
texto_dentro_N.set("Usuario")

texto_dentro_A = tk.StringVar()
texto_dentro_A.set("Contraseña")

entry_style = {"width": 30, "font": ("Arial", 12), "bd": 2, "relief": tk.FLAT}
entry_usuario = tk.Entry(frame, textvariable=texto_dentro_N, **entry_style, fg="black")
entry_usuario.bind("<FocusIn>", click_u)
entry_usuario.bind("<FocusOut>", sombra_u)
entry_usuario.grid(row=0, column=1, padx=20, pady=20,ipady=2)

entry_clave = tk.Entry(frame, textvariable=texto_dentro_A, **entry_style, fg="black")
entry_clave.bind("<FocusIn>", click_c)
entry_clave.bind("<FocusOut>", sombra_c)
entry_clave.grid(row=6, column=1, padx=10, pady=10,ipady=2)

boton_login = tk.Button(frame, text="Iniciar Sesión", command=validar_login, background="#5A5251", font=("white", 14, "bold"), fg="#E8DAEF", relief=tk.SOLID)
boton_login.grid(row=10, column=0, columnspan=2, padx=10, pady=8,ipadx=50)

boton_recu=tk.Button(frame,text="Recuperar contraseña",bg="#5A5251",font=("white", 13, "bold"), fg="#E8DAEF",relief=tk.SOLID,height=1,width=15)
boton_recu.grid(row=11,column=1,padx=10,pady=5,ipadx=30)

ventana.bind('<Return>', lambda event=None: boton_login.invoke())

imagen = Image.open("pacman.png")
imagen = imagen.resize((50, 50))  # Redimensionar la imagen si es necesario
imagen_tk = ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(ventana, image=imagen_tk, bg="white")
label_imagen.pack()

sigue = tk.Label(ventana, text="Siguenos en nuestra pagina de Instagram", bg="#0B001E", fg="white")
sigue.pack()

ventana.mainloop()
