"""Se proporciona un archivo productos.csv donde cada línea contiene el nombre 
de un producto, su precio y la cantidad en stock, separados por comas (ej: Laptop,1200,15). 
Escribe un programa que lea este archivo y muestre la información en un formato legible 
para el usuario, indicando el nombre, precio y stock de cada producto."""

archivo_csv = open("productos.csv")
lista_lineas = archivo_csv.readlines()

for linea in lista_lineas:
    linea = linea.strip()
    linea = linea.split(",")
    print(f"Producto: {linea[0]} | Precio: ${linea[1]} | Stock: {linea[2]} unidades")

archivo_csv.close()
        