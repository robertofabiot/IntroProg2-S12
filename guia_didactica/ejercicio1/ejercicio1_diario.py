"""Escribe un programa que funcione como un diario simple. Cada vez que se 
ejecute, debe solicitar al usuario una entrada de texto y la guardará, junto con la fecha y hora 
actual, en un archivo llamado diario.txt. Cada nueva entrada debe añadirse al final del 
archivo sin borrar las anteriores."""

from datetime import datetime

fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
entrada = input("Ingrese la entrada del día de hoy: ")

diario = open("diario.txt","a")
diario.write(f"{fecha_hora}: {entrada}\n")
diario.close()