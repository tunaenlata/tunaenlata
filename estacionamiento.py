import os
os.system ('cls')

from tabulate import tabulate

patentes_en_stock = ['ABC123', 'DEF422', 'GFE403']

def validar_patente():
    patente = ""
    while not (patente.isalnum and len(patente) >= 6):
        patente = input("\nIngrese la patente del vehiculo (o 'S' para terminar): ").upper()
        if patente == 'S':
            exit()
    return patente

def patente_entrante(patente):
    patentes_en_stock.append(patente)
    print("\nDejá las llaves y nosotros lo estacionamos")
    
def patente_saliente(patente):
    patentes_en_stock.remove(patente)
    print("\n¡Vuelva pronto!")

# Mostrar las patentes actuales al inicio
print("\nPatentes actuales: ", patentes_en_stock)

patente = ""

while True:

    patente = validar_patente()

    # Procesar la patente ingresada
    if patente in patentes_en_stock:
        patente_saliente(patente)
    else:
        patente_entrante(patente)

    # Mostrar el estado actualizado de las patentes
    print("\nPatentes actuales: ", patentes_en_stock)