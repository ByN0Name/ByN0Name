class jugador:
    def __init__(self, nombre ,movimiento):
        self.nombre = nombre
        self.movimiento = movimiento

    #Método por el cual le preguntas a la persona a que dirección quiere moverse
    def moverse(self, nombre, dirección):
        print("Introduce la dirección en la que te quieres mover: ")
        dirección = input()
 #a partir de aqui serian los objetos      
class Objeto:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion

    def posicion_inicial(self):
        #Método vacío
        pass

    def moverse(self):
        #Método vacío
        pass
    
class lápiz(Objeto):
    def posicion_inicial(self):
        pass

class cuaderno(Objeto):
    def posicion_inicial(self):
        pass

class computador(Objeto):
    def posicion_inicial(self):
        pass

class pase_escolar(Objeto):
    def posicion_inicial(self):
        pass    

class persona(Objeto):
    def posicion_inicial(self):
        pass

    def moverse(self):
        pass
        

class tablero():
    def __init__(self,num_filas,num_columnas,estado_celda):
        self.__num_filas= num_filas
        self.__num_columnas= num_columnas
        self.estado_celda= estado_celda

    def init_tablero(self):
        Tablero = [[0 for x in range(self.__num_filas)] for y in range(self.__num_columnas)]
        coord_y = 0
        coord_x = 0

    def estado_celda(self):
        for y in Tablero[]:
            for x in Tablero[y][]:
                if Tablero[y][x] == 0:
                    self.estado_celda = "Vacia"
                elif Tablero[y][x] == 1:
                    self.estado_celda = "Jugador"

    
    def imprimir_tablero(self):
        print()
t1=tablero(3,4)
t1.init_tablero()

Archivo: __main__.py

            Este archivo se dedica a iniciar el juego, importando las funciones de los otros archivos.


    #esta es la explicacion de cada apartado
    Archivo: estado_casilla.py

            Este archivo se dedica a mostrar el estado de una casilla, ya estubiese vacia, ocupada por un objeto o ocupada por el jugador.
            Se le darían atributos para mostrar su estado en otros archivos y un filtro de if para comprobar su estado.

Archivo: juego.py

            Este archivo inicializariía todas las funciones que sean necesarias para que el usuario pueda utilizar el programa en una sola.
             
Archivo: Jugador.py

            Este archivo se utilizaria para definir al usuario y todos los movimientos disponibles para el mismo.
            
Archivo: Tablero.py

            Este archivo sería el lugar donde se realiza el juego y donde el usuario se puede mover e interactuar con los demas objetos.
