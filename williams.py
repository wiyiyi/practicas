import tkinter as tk  
from tkinter import messagebox
def artu ():
    messagebox.showinfo("willy","mi papá me mima")
def wil():
    messagebox.showerror("no","intenta de nuevo")
ventana=tk.Tk()
ventana.title("mi primera vez")
ventana.geometry ("1000x1000")
ventana.option_add ("*Font "," arial 22 told")
ventana.option_add("*Background","black")
etiqueta=tk.Label(ventana, text= "Holi doli",font="arial 25",fg="gold")
etiqueta1=tk.Label (ventana, text= "todo empezo...",font="arial 15", fg="white")
etiqueta2=tk.Label(ventana, text="jijijija",fg="pink", font="arial 15")
etiqueta.pack()  
etiqueta1.pack()
etiqueta2.pack()
botton=tk.Button(ventana, text=("HOLA"),command=artu, fg="pink")
botton1=tk.Button(ventana,text=("PRESIONAR"),command=wil, fg="pink")
botton.pack()
botton1.pack()
ventana.mainloop()
