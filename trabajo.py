

#calcular las calificaciones 
estudiantes = int(input("Ingresa la cantidad de estudiantes: "))
materias = int(input("Ingresa la cantidad de materias: "))

calificaciones = []

for i in range(estudiantes):
    fila = []
    print("Estudiante", i + 1)

    for j in range(materias):
        calificacion = float(input("Ingresa la calificacion: "))
        fila.append(calificacion)

    calificaciones.append(fila)

print("\nPromedio de cada estudiante:")

for i in range(estudiantes):
    suma = 0

    for j in range(materias):
        suma = suma + calificaciones[i][j]

    promedio = suma / materias
    print("Estudiante", i + 1, ":", promedio)


print("\nPromedio de cada materia:")

for j in range(materias):
    suma = 0

    for i in range(estudiantes):
        suma = suma + calificaciones[i][j]

    promedio = suma / estudiantes
    print("Materia", j + 1, ":", promedio)


mayor = calificaciones[0][0]
menor = calificaciones[0][0]

for i in range(estudiantes):
    for j in range(materias):

        if calificaciones[i][j] > mayor:
            mayor = calificaciones[i][j]

        if calificaciones[i][j] < menor:
            menor = calificaciones[i][j]

print("\nCalificacion mas alta:", mayor)
print("Calificacion mas baja:", menor)
