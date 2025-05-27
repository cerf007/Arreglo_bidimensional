#2. Se desea realizar un programa en donde se capture el nombre y tres calificaciones para
#5 estudiantes de la facultad de Ingeniería, y después se pueda procesar dándonos el
#promedio final de cada uno de los alumnos, el resultado se mostrará en pantalla.

cant_estudiante = 5
cant_materia = 3
#Definimos el numero de estudiantes y materias para nuestro bucle

estudiante = []
#Se crea una lista vacía para ingresar el nombre de los estudiantes y luego sus notas

for alumno in range(cant_estudiante):
    nombre = (input(f"Ingrese el nombre del estudiante {alumno + 1}: "))
    nota = []
    #Se crea un bucle para obtener el nombre del estudiante y se  crea una lista vacía para almacenar las notas
    
    for asignatura in range(cant_materia):
        while True:
            calificacion = float(input(f"Ingrese la nota de la materia {asignatura + 1} del estudiante {nombre}: "))
            #Cree un while true para una validación de error
            
            if 0 <= calificacion <= 100:
            #Si no se cumple la condición, le saltara el error 
                break  
            print("ERROR, INGRESE UNA NOTA VÁLIDA [0 - 100]: ") 
            
        nota.append(calificacion) 
        #Al arreglo nota se le introduce los valores de las calificaciones

    promedio = sum(nota) / cant_materia
    estudiante.append([nombre] + nota + [promedio])

print("\n Resumen ")
print(f"{'Nombre':<15} {'Asignatura':<15} {'Asignatura 2':<15} {'Asignatura 3':<15} {'Promedio':<10}")
print("=" * 70)
for alumno in estudiante:
    print(f"{alumno[0]:<15} {alumno[1]:<15.2f} {alumno[2]:<15.2f} {alumno[3]:<15.2f} {alumno[4]:<10.2f}")
    #Imprime al estudiante, las notas y el promedio accediendo uno a uno
