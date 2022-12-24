import socket

host = '127.0.0.1' # O mesmo que localhost
porta = 8800 # Porta da conexão

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Estou usando TCP/IP
recebe = (host, porta)
soquete.bind(recebe)
soquete.listen(2)

print('\nServidor Iniciado...IP: ', host, 'PORTA: ', porta)

while True:
    conexao, enderecoIP = soquete.accept()
    print('\Servidor Acessado pelo Cliente:', enderecoIP, 'EM: ', datetime.now().strftime('%d/%m/%y - %H:%M:%S'))

    while True:
        mensagem = conexao.recv(2048)
        