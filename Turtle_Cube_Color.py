from turtle import *
# Movimentando a tartaruga.
title("TARTARUGA TOUCHE!") # Coloca o título na janela.
bgcolor("lightyellow") # Coloca a cor de fundo da janela em amarelo claro.
pensize(4) # Define a espessura do traço.
color("blue") # Define a cor da tartaruga e do traço.
shape("turtle") # Coloca o formato da tartaruga.
delay(50)
for cont in range(4):
    forward(200) # Anda para frente 200 pixels.
    right(90) # Gira 90 graus para a direita.