try:
    mi_ruta = "C:\\Users\\rfter\\Documents\\Archivos UAM\\Intro Programación\\S12\\Archivo\\"
    mi_archivo = open(mi_ruta + "datos.txt", "r")
    contenido = mi_archivo.read()
    print(contenido)
    mi_archivo.close()
except FileNotFoundError:
    print("El archivo no está bro.")