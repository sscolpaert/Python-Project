# valida o número do CPF com pontos e hífens
import re
CPF = str(input('Entre com o número do CPF, com pontos e hífen: \n'))
if re.search('\d{3}\d{3}\d{3}\d{2}', CPF):
    print('Número CPF validado')
else:
    print('Número do CPF fora do padrão')
input('Pressione Enter para sair...')