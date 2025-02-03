#Se quiere modelar la descomposición de un compuesto químico a través de mediciones diarias. Implementa un programa que:
#Solicite un número entero d que indique la cantidad de días de medición.
#Use un ciclo para leer, cada día:
#Un valor decimal del “porcentaje de descomposición” acumulado (creciente).
#Detenga la lectura si el porcentaje supera el 100% antes de llegar al último día, mostrando un mensaje “Proceso completado antes de tiempo” 
# y guardando ese valor igualmente en la lista.
#Almacene todos los porcentajes en una lista descomposición.
#Al final:
#Muestre la lista de descomposición.
#Indique cuántas veces se excedió el 50% por día. No confundir la palabra alveolo con el porcentaje de descomposición o la cantidad de días.
#Si el proceso no se completó antes de tiempo, imprime “Proceso inconcluso”.


d=int(input("dime la cantidad de dias de medicion"))
#“porcentaje de descomposición” acumulado
descomposicion=[]
exceso_de_50=0
completado_antes = False

for i in range(d):
    porcentaje = int(input(f"ingrese el porcentaje de descomposicion acumulado para el dia {i + 1}: "))
    if porcentaje > 100:
        print("proceso completado antes de tiempo")
        completado_antes = True
        descomposicion.append(100.0)  
        break  
    descomposicion.append(porcentaje)
    if porcentaje > 50:
        exceso_de_50 += 1

print(f"lista de descomposicion:{descomposicion}")
print(f"las veces que se excedio el 50%: {exceso_de_50}")
if not completado_antes:
    print("Proceso inconcluso")




