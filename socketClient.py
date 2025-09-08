import socket
import random
import time
import threading

HOST='127.0.0.1' #ip del server
PORT=65432

detener_hilo=threading.Event()#controla la terminacion del hilo

def generar_num_aleatorio(s):
    while not detener_hilo.is_set():
        num_aleatorio=random.randint(0,99)
        print(f"Numero generado: {num_aleatorio}")
        try:
            s.sendall(str(num_aleatorio).encode('utf-8'))

            resp_server=s.recv(1024).decode('uft-8')#recibe la respuesta del servidor
            print(f"Respuesta del servidor: {resp_server}")

            if resp_server.lower()=="perdiste":
                print("El juego acabo")
                detener_hilo.set()
                break

        except Exception as e:
            print(f"Error en el hilo de envio: {e}")
            detener_hilo.set()

        time.sleep(2)#esperara 2 segundos para la siguiente ronda

