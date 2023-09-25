import random #ramdom range

class BuscaminasModelo: #clase del modelo del buscaminas
    def __init__(self, filas, columnas, num_minas): #constructor de objetos de tipo buscaminas

        #================================= variables
        self.filas = filas
        self.columnas = columnas
        self.num_minas = num_minas
        self.tablero = None
        self.tablero_visible = None
        self.minas_restantes = 0
        self.partidas_ganadas = 0
        self.partidas_perdidas = 0

        #===========iniciar el juego dentro del objeto del constructor
        self.inicializar_juego()


    def contar_minas_adyacentes(self, fila, columna): # cuenta las nimas cercanas a la celda
        minas_adyacentes = 0
        for i in range(fila - 1, fila + 2):
            for j in range(columna - 1, columna + 2):
                if 0 <= i < self.filas and 0 <= j < self.columnas and self.tablero[i][j] == -1: #te muestra el numero de minas cerca de la celda
                    minas_adyacentes += 1 #suma el numero deminas
        return minas_adyacentes 

    def inicializar_juego(self): #se encarga de crear el tablero, colocar las minas en posiciones aleatorias
                                 #y calcular el número de minas cercanas a cada celda
        self.tablero = [[0 for _ in range(self.columnas)] for _ in range(self.filas)]
        self.tablero_visible = [[-2 for _ in range(self.columnas)] for _ in range(self.filas)]
        self.minas_restantes = self.num_minas

        while self.minas_restantes > 0:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            if self.tablero[fila][columna] != -1:
                self.tablero[fila][columna] = -1
                self.minas_restantes -= 1

        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero[i][j] != -1:
                    self.tablero[i][j] = self.contar_minas_adyacentes(i, j)

    def desvelar_celda(self, fila, columna): #se llama cuando se hace clic en una celda. Puede revelar el contenido de una celda,
                                             #ya sea un número, una mina o un espacio en blanco.
        if 0 <= fila < self.filas and 0 <= columna < self.columnas and self.tablero_visible[fila][columna] == -2:
            self.tablero_visible[fila][columna] = self.tablero[fila][columna]
            if self.tablero[fila][columna] == -1:
                for i in range(self.filas):
                    for j in range(self.columnas):
                        if self.tablero[i][j] == -1:
                            self.tablero_visible[i][j] = -1
                self.partidas_perdidas += 1
                return "perdiste"
            elif self.tablero[fila][columna] == 0:
                self.desvelar_celda_adyacente(fila, columna)
            elif self.verificar_ganador():
                self.partidas_ganadas += 1
                return "ganaste"
            return "continua"

    def desvelar_celda_adyacente(self, fila, columna): #si la celda esta vacia revela todas las celdas vacias cercanas
        for i in range(fila - 1, fila + 2):
            for j in range(columna - 1, columna + 2):
                if 0 <= i < self.filas and 0 <= j < self.columnas:
                    self.desvelar_celda(i, j)

    def verificar_ganador(self): #si el usuario gana, revela todas las celdas sin minas
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero_visible[i][j] == -2 and self.tablero[i][j] != -1:
                    return False
        return True
