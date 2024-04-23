import tkinter as tk

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Navegador de Páginas")
        self.geometry("400x300")

        self.paginas_visitadas = []
        self.pagina_actual = None

        self.pagina_inicial()

    def pagina_inicial(self):
        self.pagina_actual = Pagina(self, "Página Inicial")
        self.pagina_actual.pack(expand=True, fill="both")

    def mostrar_pagina(self, nombre_pagina):
        if self.pagina_actual is not None:
            self.pagina_actual.pack_forget()  # Oculta la página actual
            self.paginas_visitadas.append(self.pagina_actual)

        self.pagina_actual = Pagina(self, nombre_pagina)
        self.pagina_actual.pack(expand=True, fill="both")

    def volver_pagina_anterior(self):
        if self.paginas_visitadas:
            pagina_anterior = self.paginas_visitadas.pop()
            self.pagina_actual.pack_forget()
            self.pagina_actual = pagina_anterior
            self.pagina_actual.pack(expand=True, fill="both")


class Pagina(tk.Frame):
    def __init__(self, master, nombre):
        super().__init__(master)
        self.nombre = nombre
        self.config(bg="white")
        label = tk.Label(self, text=f"Esta es la {self.nombre}", font=("Arial", 18))
        label.pack(pady=50)

        if nombre != "Página Inicial":
            boton_volver = tk.Button(self, text="Volver", command=master.volver_pagina_anterior)
            boton_volver.pack()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()