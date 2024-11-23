import os
os.system ('cls')

from tabulate import tabulate

patentes_en_stock = ['ABC123', 'DEF422', 'GFE403']

ingreso = [8, 20, 15]

patentes_ingreso = list(zip(patentes_en_stock, ingreso))

def validar_patente():
    patente = ""
    while not (patente.isalnum and len(patente) >= 6):
        patente = input("\nIngrese la patente del vehiculo: ")
    # Cosas a agregar: Un mensaje de error si falla ("Patente errónea, intentá nuevamente")
    # Que reemplace si se agrega un espacio. Ejemplo: ABC 123

tabla = tabulate(patentes_ingreso, headers=["Patentes", "Ingreso"], tablefmt="grid")

# def patente_entrante():
#     append
    
# def patente_saliente():
#     pop(0 ó 1, dependerá)  

print(tabla)
validar_patente()
