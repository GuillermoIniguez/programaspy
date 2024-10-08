import socket

def banner_grabbing():
    ip = input("Ingresa la IP del objetivo: ")
    puerto = int(input("Ingresa el puerto: "))
    
    s = socket.socket()
    s.connect((ip, puerto))
    banner = s.recv(1024)
    print(f"Banner: {banner.decode().strip()}")
    s.close()
