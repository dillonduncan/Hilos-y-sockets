import socket

HOST='127.0.0.1' #ip del server
PORT=65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    print(f"Conectado al server: {HOST}:{PORT}")

    mensaje=input("Ingrese el mensaje que desea enviar: ")#mensaje que se envia al server
    s.sendall(mensaje.encode('utf-8'))
    print(f"Mensaje enviado: {mensaje}")

    data=s.recv(1024)#recibir respuesta del servidor

print(f"Respuesta recibida del servidor: {data.decode('utf-8')}")

