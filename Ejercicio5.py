""" 5. Escriba el programa que tenga un arreglo bidimensional que almacena la cantidad de
computadores vendidos por tres vendedores en cuatro zonas diferentes. Se pide mostrar:
a. La zona en la que más computadores se vendió.
b. El vendedor que menos computadores vendió.
c. La cantidad de computadores vendidos por todos los vendedores en todas las zonas.
"""

Computadores_vendidos = [[20, 30, 40, 50], #Venderdor 1
                        [23, 104, 69, 88], #Vendedor 2
                        [14, 20, 94, 60]] #Vendedor 3



#Inciso [a]
suma_zon = []
for zona in range(4):
    suma_venta = 0
    for vendedor in range(3):
        suma_venta += Computadores_vendidos[vendedor][zona]
    suma_zon.append(suma_venta)

zona_mayor = 0
for zona in range(4):
    venta = suma_zon[zona]
    if venta > zona_mayor:
        zona_mayor = venta
        zona_mayor_index = zona

print("Cantidad de computadores vendidos por todos los vendedores en todas las zonas:", suma_zon)
print (zona_mayor)


#Inciso [b]
suma_vendedor = []
for vendedor in range(3):
    venta = sum(Computadores_vendidos[vendedor])
    suma_vendedor.append(venta)

vendedor_menor = suma_vendedor[0]
vendedor_menor_index = 0
for vendedor in range(3):
    venta = suma_vendedor[vendedor]
    if venta < vendedor_menor:
        vendedor_menor = venta
        vendedor_menor_index = vendedor

print("Cvendedores:", suma_vendedor)
print (vendedor_menor_index + 1)