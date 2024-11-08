import socket
import threading

# Função para lidar com a comunicação de um cliente
def handle_client(client_socket):
    while True:
        try:
            # Recebe a mensagem do cliente
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Mensagem recebida: {message}")
            
            # Envia uma resposta para o cliente
            response = input("Digite sua resposta: ")
            client_socket.send(response.encode('utf-8'))
        except:
            break

    client_socket.close()

def start_server():
    host = '10.1.24.43'  # IP do servidor, 0.0.0.0 significa "qualquer IP disponível"
    port = 5555         # Porta do servidor

    # Criação do socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Servidor ouvindo em {host}:{port}...")

    while True:
        # Espera uma conexão de um cliente
        client_socket, addr = server.accept()
        print(f"Conexão de {addr} estabelecida.")

        # Cria uma thread para lidar com a comunicação do cliente
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "_main_":
    start_server()
