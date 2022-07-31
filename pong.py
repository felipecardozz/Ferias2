# SE LER os comentários vai parecer mais fácil, confia
# o jogo é uma bola e duas peças ou retângulos, o da esquerda está como elemento "esquerda" e o da direita "direita", a bola vai estar como "bola"
# usamos a biblioteca turtle, q já vem com o python então nao precisa baixar, criamos um janela e definimos esses objetos em classes
# com essa estrutura vamos criar funções para que o jogo fique na animação ideal

import turtle
import os

# janela do jogo
janela = turtle.Screen()
janela.title("Pong")  # titulo q aparece na parte superior da janela
# janela preta na forma do pong original, bg = background
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)  # impede q a janela reinicie sozinha tipo f5

# Score
direita = 0
esquerda = 0

esquerda = turtle.Turtle()  # nessa linha existe
# essa é a velocidade da animação e não do retângulo, 0 a maior de todas o q melhora jogabilidade
esquerda.speed(0)
esquerda.shape("square")
esquerda.color("white")
# penup e pendown servem para deslocar o objeto sem criar uma linha feita pelo turtle
esquerda.penup()
esquerda.shapesize(stretch_wid=5, stretch_len=1)
esquerda.goto(-350, 0)  # onde esse retângulo aparecera, 0 eh o centro

# é o mesmo código do "esquerda" menos as
direita = turtle.Turtle()
direita.speed(0)  #
direita.shape("square")
direita.color("white")
direita.penup()
direita.shapesize(stretch_wid=5, stretch_len=1)
direita.goto(350, 0)

# Bola está em 0, 0 pq é o centro da janela
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 2  # como a bola vai mover em horizontal em 2px
bola.dy = 2  # como a bola vai mover em horizontal em 2px

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Brasil:0 Argentina:0", align="center",  # Placar e nome do time dos elementos "esquerda" e "direita"
          font=("Courier", 24, "normal"))

# Funções


def esquerda_up():  # definir a função para fazer os retangulos se moverem
    y = esquerda.ycor()
    y += 20  # y nesse caso é a coordenada, e anda 20px pra cima
    esquerda.sety(y)


def esquerda_down():
    y = esquerda.ycor
    y -= 20
    esquerda.sety(y)


def direita_up():
    y = direita.ycor()
    y += 20
    direita.sety(y)


def direita_down():
    y = direita.ycor
    y -= 20
    direita.sety(y)


# Essa parte se chama keyboard binding, serve para ligar a função com o teclado e ai mover os retangulos
janela.listen()
janela.onkeypress(esquerda_up, "w")
janela.onkeypress(esquerda_down, "s")
janela.onkeypress(direita_up, "Up")  # "UP" é a setinha de subir
janela.onkeypress(direita_down, "Down")  # "Down" é a setinha de descer

# Parte q chamam de game loop onde o input eh processado
while True:
    janela.update()  # toda vez q o programa rodar ele vai dar um f5 automatico

    # Movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.setx(bola.xcor() + bola.dy)

    if bola.ycor() > 290:  # para fazer ela tabelar nas paredes
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.ycor() > 390:
        bola.sety(0, 0)
        bola.dy *= -1

    if bola.ycor() < -390:
        bola.sety(0, 0)
        bola.dy *= -1

    # Quando a bola chegar a alguma extremidade ou retangulo, ganhará 50 px de movimento nas coordenadas
    if bola.xcor() < -340 and bola.ycor() < esquerda.ycor() + 50 and bola.ycor() > esquerda.ycor() - 50:
        bola.dx *= -1
        os.system("afplay bounce.wav&")

    elif bola.xcor() > 340 and bola.ycor() < direita.ycor() + 50 and bola.ycor() > direita.ycor() - 50:
        bola.dx *= -1
        os.system("afplay bounce.wav&")
