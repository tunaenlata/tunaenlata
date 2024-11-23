import os
os.system ('cls')

from tabulate import tabulate

patentes_en_stock = ['ABC123', 'DEF422', 'GFE403']

# ingreso = [8, 20, 15]

# patentes_ingreso = list(zip(patentes_en_stock, ingreso))
# Es necesario "zipearlos" porque el módulo tabulate espera que los datos que queremos tabular estén organizados en filas.

def validar_patente():
    patente = ""
    while not (patente.isalnum and len(patente) >= 6):
        patente = input("\nIngrese la patente del vehiculo (o 'S' para terminar): ").upper()
    return patente
    # Cosas a agregar: Un mensaje de error si falla ("Patente errónea, intentá nuevamente")
    # Que reemplace si se agrega un espacio. Ejemplo: ABC 123

# tabla = tabulate(patentes_ingreso, headers=["Patentes", "Ingreso"], tablefmt="grid")

def patente_entrante(patente):
    patentes_en_stock.append(patente)
    print("\nDejá las llaves y nosotros lo estacionamos")

# (1) validar_patente (2) si la patente ingresada está en la lista de patentes en stock, remove. (3) si no está, append. 
    
def patente_saliente(patente):
    patentes_en_stock.remove(patente)
    print("\n¡Vuelva pronto!")

# print(tabla)

print("\nPatentes actuales: ", patentes_en_stock)

# Validar la patente ingresada
patente = validar_patente()

while patente != 'S'.upper():
    if patente in patentes_en_stock:
        patente_saliente(patente)
    else: 
        patente_entrante(patente)

print("\nPatentes actuales: ", patentes_en_stock)