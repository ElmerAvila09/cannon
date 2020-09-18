"""
Intituto Tecnologico de Estudios Superiores de Monterrey
Equipo "Default":
Daniel de Zamacona Madero - A01570576
Elmer Osiel Avila Vargas - A00826359
El programa despliega un juego con objetivos a destruir a partir de proyectiles que aparecen al hacer click en la pantalla.
Fecha de Modificacion: 17/9/2020
"""
from random import randrange
from turtle import *
from freegames import vector

# Declaracion de variables iniciales
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

'''
Responde al click en la pantalla de juego
Entrada: Posicion vectorial de donde se hace click
Salida: Ninguna
'''
def tap(x, y):

    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

'''
Revisar si una poscicion esta dentro de la pantalla
Entrada: Vector a revisar
Salida: Booleano, true si la posicion se encuntra dentro de los limites.
'''
def inside(xy):
    # Return con la comparacion de los limites de la pantalla
    return -200 < xy.x < 200 and -200 < xy.y < 200

'''
Dibuja las balas y los objetivos
Entrada: Ninguna
Salida: Ninguna
'''
def draw():
    clear()

    # Dibuja el punto que simulara el objetivo, color azul
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    # Dibuja el punto que simulara el proyectil, color rojo
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

'''
Genera todo el movimiento dentro del juego
Entrada: Ninguna
Salida: Ninguna
'''
def move():
    # En cada actualizacion de pantalla se hace un random, si este es 0 entonces crea objetivo
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    # Se da velocidad negativa en y para que el proyectil se caiga, es decir, simule una ruta parabolica
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Modificacion, en caso de que el objetivo salga del borde, se elimina y se reposiciona, asi no terminara el juego
    for target in targets:
        if not inside(target):
            targets.remove(target)
            y = randrange(-150, 150)
            target = vector(200, y)
            targets.append(target)

    # Actualizaciones cada 50 milesimas de segundo
    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()