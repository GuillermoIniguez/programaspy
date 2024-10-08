import socket

def encontrar_ip_socket():
    hostname = socket.gethostname()
    ip_local = socket.gethostbyname(hostname)
    print(f"La IP local es: {ip_local}")
