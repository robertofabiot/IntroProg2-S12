""" Crea un programa que permita al usuario crear una lista de compras. El programa 
solicitará al usuario que ingrese productos uno por uno y los guardará en un archivo llamado 
compras.txt. El usuario indicará que ha terminado de añadir productos introduciendo la 
palabra "fin"."""

print("Bienvenido al supercreador de lista de compras.")
entrada = input("Ingrese el producto: ")

while entrada.lower() != "fin":
    with open('lista.txt', 'a') as archivo:
        archivo.write(f'{entrada}\n')
    entrada = input("Ingrese el producto: ")

print("Lista guardada bro")