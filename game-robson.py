import turtle
import random
import time

# Configurar a janela do jogo
window = turtle.Screen()
window.title("Space Invaders - Robson")
window.bgpic("loop.gif")

# Desenhar a borda
border_pen = turtle.Turtle()
border_pen.speed(10)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0

# Desenhar a pontuação
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("red")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "SCORE: %s" % score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Registrar as formas
turtle.register_shape("invader.gif")
turtle.register_shape("player (1).gif")

# Criar a tartaruga do jogador
player = turtle.Turtle()
player.shape("player (1).gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

number_of_enemies = 10
enemies = []

# Adicionar inimigos à lista
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

# Configuração dos inimigos
for enemy in enemies:
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 5

# Configuração do projétil disparado pelo jogador
fogo = turtle.Turtle()
fogo.color("yellow")
fogo.shape("triangle")
fogo.penup()
fogo.speed(0.1)
fogo.setheading(90)
fogo.shapesize(0.5,0.5)
fogo.setposition(0, -235)

fogospeed = 30

# Função para mover o jogador para a esquerda
def mover_esquerda():
    x = player.xcor()
    if x >= -250:
        x -= playerspeed
    player.setx(x)
    fogo.setx(x)
    
# Função para mover o jogador para a direita
def mover_direita():
    x = player.xcor()
    if x <= 250:
        x += playerspeed
    player.setx(x)
    fogo.setx(x)

# Função para mover o projétil disparado pelo jogador
def mover_fogo():
    y = fogo.ycor()
    while y< 300:
        y += fogospeed
        fogo.sety(y)
        time.sleep(0.01)
    fogo.sety(-235)

# Configurar os ouvintes de eventos do teclado
turtle.listen()
turtle.onkey(mover_esquerda, "Left")
turtle.onkey(mover_direita, "Right")
turtle.onkey(mover_fogo, "space")

while i < 10:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Verifique se o inimigo atingiu a borda
        if x > 280:
            y = enemy.ycor()
            y -= 20
            enemy.sety(y)
            enemyspeed *= -1
        if x < -280:
            y = enemy.ycor()
            y -= 20
            enemy.sety(y)
            enemyspeed *= -1

turtle.done()