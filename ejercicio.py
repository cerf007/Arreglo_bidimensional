# La Abarrotera ABSA - Ventas por tienda y mes en formato tabla

# Tiendas
matriz_tienda = ["ABSA 1", "ABSA 2", "ABSA 3", "ABSA 4"]

# Meses
matriz_meses = ["Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Ventas por mes (cada fila representa un mes, cada columna una tienda)
matriz_ventas = [
    [50000, 89000, 65000, 92000],   # Julio
    [60000, 90000, 72000, 88000],   # Agosto
    [65000, 98000, 85000, 90000],   # Septiembre
    [62000, 80000, 72000, 76000],   # Octubre
    [78000, 85000, 83000, 82000],   # Noviembre
    [95000, 90000, 98000, 93000]    # Diciembre
]

# Encabezado
print("-"*78)
print(f"|| {'Mes':<12}", end="|")
for tienda in matriz_tienda:
    print(f"|| {tienda:^12}", end="|")
print("|")
print("-"*78)

# Filas de ventas por mes
for i, mes in enumerate(matriz_meses):
    print(f"|| {mes:<12}", end="|")
    for venta in matriz_ventas[i]:
        print(f"|| ${venta:>10,} ", end="|")
    print("|")
print("-"*78)

# Cálculos
# Ventas por mes
ventas_mes = [sum(mes) for mes in matriz_ventas]

# Ventas totales de todas las tiendas
ventas_totales = sum(ventas_mes)
print(f"\nVentas totales de todas las tiendas: ${ventas_totales:,}")

# Ventas por tienda
ventas_tienda = [sum(matriz_ventas[i][j] for i in range(len(matriz_ventas))) for j in range(len(matriz_tienda))]
for i, tienda in enumerate(matriz_tienda):
    print(f"Ventas totales de {tienda}: ${ventas_tienda[i]:,}")

# Mes con mayores ventas
mayor_venta = max(ventas_mes)
mes_mayor = matriz_meses[ventas_mes.index(mayor_venta)]
print(f"\nMes con mayores ventas: {mes_mayor} con ${mayor_venta:,}")

# Mes con menores ventas
menor_venta = min(ventas_mes)
mes_menor = matriz_meses[ventas_mes.index(menor_venta)]
print(f"Mes con menores ventas: {mes_menor} con ${menor_venta:,}")
