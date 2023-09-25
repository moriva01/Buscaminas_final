import tkinter as tk #interfaz grafica


class BuscaminasVista: #clase de vista del buscaminas (netamente grafica)
    def __init__(self, root, modelo):
        self.root = root
        self.root.title("Buscaminas - proyecto final")
        self.root.iconbitmap("img/logo.ico")
        self.root.geometry("350x350")
        self.modelo = modelo
        self.botones = []
        self.inicializar_interfaz()
        self.actualizar_tablero()


    def inicializar_interfaz(self):
        for i in range(self.modelo.filas):
            fila_botones = []
            for j in range(self.modelo.columnas):
                boton = tk.Button(self.root, width=2, height=1,
                                  command=lambda i=i, j=j: self.desvelar_celda(i, j))
                boton.grid(row=i, column=j)
                fila_botones.append(boton)
            self.botones.append(fila_botones)

        self.reiniciar_boton = tk.Button(self.root, text="Reiniciar juego", command=self.reiniciar_juego)
        self.reiniciar_boton.grid(row=self.modelo.filas, columnspan=self.modelo.columnas)

        self.etiqueta_ganadas = tk.Label(self.root, text=f"Partidas Ganadas: {self.modelo.partidas_ganadas}")
        self.etiqueta_ganadas.grid(row=self.modelo.filas + 1, column=0, columnspan=self.modelo.columnas // 2)
        self.etiqueta_perdidas = tk.Label(self.root, text=f"Partidas Perdidas: {self.modelo.partidas_perdidas}")
        self.etiqueta_perdidas.grid(row=self.modelo.filas + 1, column=self.modelo.columnas // 2,
                                    columnspan=self.modelo.columnas // 2)

    def actualizar_tablero(self):
        for i in range(self.modelo.filas):
            for j in range(self.modelo.columnas):
                valor = self.modelo.tablero_visible[i][j]
                if valor == -1:
                    self.botones[i][j].config(text="*", state=tk.DISABLED)
                elif valor == -2:
                    self.botones[i][j].config(text="", state=tk.NORMAL)
                else:
                    self.botones[i][j].config(text=str(valor), state=tk.DISABLED)
        self.etiqueta_ganadas.config(text=f"Partidas Ganadas: {self.modelo.partidas_ganadas}")
        self.etiqueta_perdidas.config(text=f"Partidas Perdidas: {self.modelo.partidas_perdidas}")

    def desvelar_celda(self, fila, columna):
        resultado = self.modelo.desvelar_celda(fila, columna)
        if resultado == "perdiste":
            self.mostrar_mensaje("¡Perdiste!")
        elif resultado == "ganaste":
            self.mostrar_mensaje("¡Ganaste!")
        self.actualizar_tablero()

    def reiniciar_juego(self):
        self.modelo.inicializar_juego()
        self.actualizar_tablero()
        self.ocultar_mensaje()

    def mostrar_mensaje(self, mensaje):
        mensaje_popup = tk.Toplevel(self.root)
        mensaje_popup.title("Mensaje")
        mensaje_label = tk.Label(mensaje_popup, text=mensaje)
        mensaje_label.pack(padx=20, pady=20)

    def ocultar_mensaje(self):
        self.root.wm_attributes("-topmost", 1)
        self.root.wm_attributes("-topmost", 0)
