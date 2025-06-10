try:
    mi_ruta = "C:\\Users\\rfter\\Documents\\Archivos UAM\\Intro Programación\\S12\\Archivo\\"
    mi_archivo = open(mi_ruta + "notas.txt", "w")
    texto = input("Dime algo: ")
    mi_archivo.write(texto)
    mi_archivo.close()
except FileNotFoundError:
    print("Error")