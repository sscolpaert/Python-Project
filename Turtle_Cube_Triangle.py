from turtle import *
# Movimentando a tartaruga.

def quadrado(graus, tamanho):
    for cont in range(4):
        forward(tamanho)
        right(graus)

def triangulo(graus, tamanho):
    for i in ["red","violet","orange"]:
        color(i)
        left(graus)
        forward(tamanho)

def touche():
    title("TARTARUGA TOUCHE!") # Coloca o título na janela.
    bgcolor("lightyellow") # Coloca a cor de fundo da janela em amarelo claro.
    pensize(4) # Define a espessura do traço.
    color("blue") #Define a cor da tartaruga e do traço.
    shape("turtle") #Define o formato da tartaruga
    delay(50)
    quadrado(90, 200)
    triangulo(120, 150)

touche() # Chama a função.
exitonclick() # Aguarda o clique do mouse para encerrar.