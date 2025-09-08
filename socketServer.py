import socket
import random

#configuracion del servidor
HOST= '127.0.0.1'
PORT= 65432

def main():
    try:        
        #creacion del socket servidor
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST,PORT))# ENLACE SOCKET A LA IP Y EL PUERTO
            s.listen()  #socket en modo escucha
            print(f"servidor escuchando en {HOST}:{PORT}")

            conn, addr=s.accept() #aceptar la conexion del cliente

            with conn:
                print(f"Conectado a {addr}")

                aciertos=0
                desaciertos_seguidos=0

                while True:
                    data=conn.recv(1024)
                    if not data:
                        break
                    mensaje_recibido=data.decode('utf-8')

                    if mensaje_recibido.lower=="terminar":
                        print("El cliente solicito terminar el juego")
                        break
                    try:
                        num_cliente=int(mensaje_recibido)
                        num_server=random.randint(0,99)#numero que genera el servidor para tratar de adivinar
                        print(f"Numero del cliente: {num_cliente}")
                        print(f"Numero del servidor: {num_server}")
                        
                        if num_cliente==num_server:
                            aciertos+=1
                            conn.sendall("has adivinado el numero".encode('utf-8'))
                            desaciertos_seguidos=0
                        else:
                            conn.sendall("incorrecto".encode('utf-8'))
                            desaciertos_seguidos+=1

                        if desaciertos_seguidos>=3:
                            print("El servidor fallo 3 veces seguidas, perdiste")
                            conn.sendall("Perdiste. El servidor fallo 3 veces seguidas".encode('utf-8'))
                            break

                    except ValueError:
                        print(f"Mensaje no valido: {mensaje_recibido}")
                        continue
                
                print("--Juego terminado--")
                print(f"Aciertos: {aciertos}")
                print(f"Desaciertos seguidos: {desaciertos_seguidos}")

                        
    except Exception as e:
        print(f"Ocurrio un error en el servidor {e}")
    finally:
        print("Conexion cerrada")

if __name__=="__main__":
    main()