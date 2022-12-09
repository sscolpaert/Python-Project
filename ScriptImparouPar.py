# Entra com um número e verifica se este número é par ou impar
vResultado = ""
vNum = int(input('Entre com um número: '))
if vNum % 2 == 0:
    vResultado = "Par"
else:
    vResultado = "Impar"
print("O númeero é: ",vResultado) #Apresenta o resultado