import tkinter as tk
from tkinter import messagebox
import subprocess


def cerrar_y_abrir1():
    # Cierra la ventana actual
    ventana.destroy()

def validar_login():
    usuario = entry_usuario.get()
    clave = entry_clave.get()

    
    if usuario == "doc1" and clave == "1234":
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
    else:
        messagebox.showerror("Inicio de sesión", "Usuario o contraseña incorrectos")

def on_button_click():
    ruta_archivo = "proyecto parte willy.py"
    subprocess.run(["python", ruta_archivo])



ventana = tk.Tk()
ventana.title("Bienvenido a la clinica dd")
ventana.geometry("300x400")



etiqueta_usuario = tk.Label(ventana, text="Usuario:")
etiqueta_usuario.grid(row=0, column=0, padx=10, pady=5)

etiqueta_clave = tk.Label(ventana, text="Contraseña:")
etiqueta_clave.grid(row=1, column=0, padx=10, pady=5)


entry_usuario = tk.Entry(ventana)
entry_usuario.grid(row=0, column=1, padx=10, pady=5)

entry_clave = tk.Entry(ventana, show="*")
entry_clave.grid(row=1, column=1, padx=10, pady=5)


boton_login = tk.Button(ventana, text="Iniciar Sesión", command=validar_login)
boton_login.grid(row=2, column=1, columnspan=2, padx=10, pady=5)


button = tk.Button(ventana, text="Haz clic aquí", command=on_button_click and cerrar_y_abrir1)
button.grid(row=3,column=1,columnspan=2,padx=10,pady=5)


ventana.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess


def cerrar_y_abrir():
    # Cierra la ventana actual
    vent.destroy()
    # Abre una nueva ventana
  
    vent2 = "gastosmedicos.py"
    subprocess.run(["python", vent2])


vent= tk.Tk()
vent.title("Segunda")
 
enf = tk.Label(vent, text="Enfermedades:", font=("Arial", 12, "bold"))
enf.grid(row=0, column=0, padx=10, pady=5)

sele = tk.Label(vent, text="Seleccione que busca:", font=("Arial", 12, "bold"))
sele.grid(row=7, column=0, padx=10, pady=5)

pag2=tk.Button(vent,text="Gastos medicos",font=("arial",10,"bold"),fg="red",command=cerrar_y_abrir) 




combo = ttk.Combobox(vent, values=["QUIMIOTERAPIA", "CIRUGIA", "TERAPIA HORMONAL","TERAPIA DIRIGIDA","TERAPIA DE CELULAS MADRES"])
combo.grid(row=9, column=0, sticky="ew", padx=10,columnspan=2)

c1=tk.Checkbutton(vent, text="Cancer de Pancreas")
c2 = tk.Checkbutton(vent, text="Cancer de Pulmon" )
c3 = tk.Checkbutton(vent, text="Cancer de Mama" )
c4 = tk.Checkbutton(vent, text="Cancer de Prostata")
c5 = tk.Checkbutton(vent, text="Cancer de Riñon")
c6 = tk.Checkbutton(vent, text="Cancer de Vejiga")
c7 = tk.Checkbutton(vent, text="Cancer de Higado")
c8 = tk.Checkbutton(vent, text="Cancer de Estomago")
c9 = tk.Checkbutton(vent, text="Cancer de Piel")
c10 = tk.Checkbutton(vent, text="Cancer de Utero")
c11 = tk.Checkbutton(vent, text="Cancer de Vagina")
c12 = tk.Checkbutton(vent, text="Cancer de Colorrectal")
c13 = tk.Checkbutton(vent, text="Cancer de Tiroides")
c14 = tk.Checkbutton(vent, text="Cancer de Colon")


c1.grid(row=1, column=0, sticky="w", padx=10)
c2.grid(row=1, column=1, sticky="w", padx=10)
c3.grid(row=1, column=2, sticky="w", padx=10)
c4.grid(row=2, column=0, sticky="w", padx=10)
c5.grid(row=2, column=1, sticky="w", padx=10)
c6.grid(row=2, column=2, sticky="w", padx=10)
c7.grid(row=3, column=0, sticky="w", padx=10)
c8.grid(row=3, column=1, sticky="w", padx=10)
c9.grid(row=3, column=2, sticky="w", padx=10)
c10.grid(row=4, column=0, sticky="w", padx=10)
c11.grid(row=4, column=1, sticky="w", padx=10)
c12.grid(row=4, column=2, sticky="w", padx=10)
c13.grid(row=5, column=0, sticky="w", padx=10)
c14.grid(row=5, column=1, sticky="w", padx=10)


pag2.grid(row=10,column=3,padx=10,pady=10,columnspan=3)
vent.geometry("")
vent.mainloop()