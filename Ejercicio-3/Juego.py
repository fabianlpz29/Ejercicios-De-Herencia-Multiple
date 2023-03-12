from Jugador1 import Jugador1
from Jugador2 import Jugador2
from Jugador1 import goku
from Jugador2 import gohan

class Juego(Jugador1,Jugador2):
    pass

    def Batalla():
        #ataque del jugador 1
        print(f"{goku.nombre} ataca, resta {goku.ataque} de la salud de {gohan.nombre}")
        gohan.salud = gohan.salud - goku.ataque
        print(f"La salud de {gohan.nombre} es {gohan.salud}")

        #ataque del jugador 2
        print(f"{gohan.nombre} ataca, resta {gohan.ataque} de la salud de {goku.nombre}")
        goku.salud = goku.salud - gohan.ataque
        print(f"La salud de {goku.nombre} es {goku.salud}")

        #ataque del jugador 1
        print(f"{goku.nombre} ataca, resta {goku.ataque} de la salud de {gohan.nombre}")
        gohan.salud = gohan.salud - goku.ataque
        print(f"La salud de {gohan.nombre} es {gohan.salud}")

        #ataque del jugador 2
        print(f"{gohan.nombre} ataca, resta {gohan.ataque} de la salud de {goku.nombre}")
        goku.salud = goku.salud - gohan.ataque
        print(f"La salud de {goku.nombre} es {goku.salud}")

        #ataque del jugador 1
        print(f"{goku.nombre} ataca, resta {goku.ataque} de la salud de {gohan.nombre}")
        gohan.salud = gohan.salud - goku.ataque
        print(f"La salud de {gohan.nombre} es {gohan.salud}")
        #ataque del jugador 2

        print(f"{gohan.nombre} ataca, resta {gohan.ataque} de la salud de {goku.nombre}")
        goku.salud = goku.salud - gohan.ataque
        print(f"La salud de {goku.nombre} es {goku.salud}")

        #ataque del jugador 1
        print(f"{goku.nombre} ataca, resta {goku.ataque} de la salud de {gohan.nombre}")
        gohan.salud = gohan.salud - goku.ataque
        print(f"La salud de {gohan.nombre} es {gohan.salud}")
        print(f"!!! {goku.nombre} gana la batalla !!!")
       
pelea = Juego
print(pelea.Batalla())





