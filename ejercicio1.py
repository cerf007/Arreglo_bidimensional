# La Abarrotera ABSA arreglo bidimensional


#Variables
matriz_tienda= ["ABSA 1", "ABSA 2", "ABSA 3", "ABSA 4"]
print("-"*45)

#Ventas por tienda y mes
Julio = [50000, 89000, 65000, 92000]
Agosto = [60000, 90000, 72000, 88000]
Septiembre = [65000, 98000, 85000, 90000]
Octubre = [62000, 80000, 72000, 76000]
Noviembre = [78000, 85000, 83000, 82000]
Diciembre = [95000, 90000, 98000, 93000]

for tienda in matriz_tienda:
    print(f"|| {tienda:>6}", end=" ||")
    print("||")
    print("-"*45)
        
# Crear una matriz bidimensional para almacenar los meses
matriz_meses = ["Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
print("-"*45)

for meses in matriz_meses:
    print(f"|| {meses:>6} ||")
    print("||")
    print("-"*45)
    
# Crear una matriz bidimensional para almacenar las ventas
matriz_ventas = [
    Julio,
    Agosto,
    Septiembre,
    Octubre,
    Noviembre,
    Diciembre
]
print("-"*45)
for ventas in matriz_ventas:
    print(f"|| {ventas}", end=" ||")
    print("||")
    print("-"*45)
        
#Operaciones

#Calcular ventas por mes
ventas_mes = [sum(matriz_ventas[i]) for i in range(len(matriz_ventas))]

#Calcular ventas totales de todas las tiendas
ventas_totales = sum(ventas_mes)
print("-"*45)

print(f"Las ventas totales de todas las tiendas es: {ventas_totales}")

#Calcular las ventas de cada tienda
ventas_tienda = [sum(matriz_ventas[i][j] for i in range(len(matriz_ventas))) for j in range(len(matriz_tienda))]
print(f"Las ventas de cada tienda es: {ventas_tienda}")

#Calcular el mes con mayores ventas
mayor_venta = max(ventas_mes)
print(F"El mes con mayores ventas fue: ")
for i, mes in enumerate(matriz_meses):
    if ventas_mes[i] == mayor_venta:
        print(f"{mes} con ventas de {mayor_venta}")

# Calcular el mes con menores ventas
menos_venta = min(ventas_mes)
indice_menor = ventas_mes.index(menos_venta)
print(f"El mes con menores ventas fue: {matriz_meses[indice_menor]} con ventas de {menos_venta}")






