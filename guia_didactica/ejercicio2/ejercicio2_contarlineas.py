"""Problema: Desarrolla un programa que pida al usuario el nombre de un archivo de texto. El 
programa deberá leer el archivo y mostrar en pantalla el número total de líneas que contiene. 
Debe manejar el error en caso de que el archivo no exista. """

while True:
    try:
        nombre_archivo = input("Elige el archivo para contar sus líneas. Está cancion.txt y poema.txt: ")
        archivo = open(nombre_archivo, "r")
        lineas = len(archivo.readlines())
        print(f"El archivo tiene {lineas} lineas.")
        break
    except FileNotFoundError:
        print("😱 ¡Oh no! Parece que el archivo que estás buscando ha decidido jugar al escondite... 🎭 Pero no te preocupes, juntos lo encontraremos. 🚀 ¿Quizás verificando el nombre del archivo o su ubicación? ¡Tú puedes! 💪")
        print("¡Inténtalo de nuevo!")