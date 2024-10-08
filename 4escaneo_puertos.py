import socket

def escaneo_de_puertos():
    ip = input("Ingresa la IP a escanear: ")
    
    for puerto in range(1, 1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        resultado = s.connect_ex((ip, puerto))
        
        if resultado == 0:
            print(f"Puerto {puerto} está abierto")
        s.close()
