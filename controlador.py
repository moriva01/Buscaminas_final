import tkinter as tk #libreria grafica para python
from modelo import BuscaminasModelo #importa la clase de modelo (logca del juego)
from vista import BuscaminasVista #importa la clase vista 

class BuscaminasControlador:
    def __init__(self, root, modelo, vista):#constructor de objetos de tipo controlador
        self.root = root
        self.modelo = modelo
        self.vista = vista
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.vista.reiniciar_boton.config(command=self.reiniciar_juego)
        self.vista.mostrar_mensaje("¡Bienvenido al Buscaminas!")

    def cerrar_ventana(self):#cierra la ventana del juego si asi s ele pide
        self.root.destroy()

    def reiniciar_juego(self): #reinicia el juego al llamar de nuevo las funciones relacionadas a la logica del juego
        self.modelo.inicializar_juego()
        self.vista.actualizar_tablero()
        self.vista.ocultar_mensaje()

if __name__ == "__main__": #main del aplicativo (cantidad de filas, columnas y minas a generar)
    filas = 10
    columnas = 10
    num_minas = 20

    modelo = BuscaminasModelo(filas, columnas, num_minas) #inicial el modelo
    root = tk.Tk() #ventana root para la GUI
    vista = BuscaminasVista(root, modelo) #inicia la vista
    controlador = BuscaminasControlador(root, modelo, vista)#inicia el controlador

    root.mainloop() #maniene activa la ventana d ela GUI


