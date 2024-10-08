from encontrar_ip_socket import encontrar_ip_socket
from encontrar_ip_cli import encontrar_ip_cli
from banner_grabbing import banner_grabbing
from escaneo_puertos import escaneo_de_puertos


def menu():
    print("1. Encontrar IP con Sockets")
    print("2. Encontrar IP con Comando CLI")
    print("3. Banner Grabbing")
    print("4. Escaneo de Puertos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        encontrar_ip_socket()
    elif opcion == "2":
        encontrar_ip_cli()
    elif opcion == "3":
        banner_grabbing()
    elif opcion == "4":
        escaneo_de_puertos()
    elif opcion == "5":
        print("Saliendo...")
    else:
        print("Opción no válida")
        menu()

if __name__ == "__main__":
    menu()
