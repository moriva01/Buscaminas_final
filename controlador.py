import tkinter as tk
from modelo import BuscaminasModelo
from vista import BuscaminasVista

class BuscaminasControlador:
    def __init__(self, root, modelo, vista):
        self.root = root
        self.modelo = modelo
        self.vista = vista
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.vista.reiniciar_boton.config(command=self.reiniciar_juego)
        self.vista.mostrar_mensaje("¡Bienvenido al Buscaminas!")

    def cerrar_ventana(self):
        self.root.destroy()

    def reiniciar_juego(self):
        self.modelo.inicializar_juego()
        self.vista.actualizar_tablero()
        self.vista.ocultar_mensaje()

if __name__ == "__main__":
    filas = 10
    columnas = 10
    num_minas = 20

    modelo = BuscaminasModelo(filas, columnas, num_minas)
    root = tk.Tk()
    vista = BuscaminasVista(root, modelo)
    controlador = BuscaminasControlador(root, modelo, vista)

    root.mainloop()


