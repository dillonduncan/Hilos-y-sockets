import socket

#configuracion del servidor
HOST= '127.0.0.1'
PORT= 65432

#creacion del socket servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))# ENLACE SOCKET A LA IP Y EL PUERTO
    s.listen()  #socket en modo escucha
    conn, addr=s.accept() #aceptar la conexion del cliente