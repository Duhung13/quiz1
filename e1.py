#En un proceso de mecanización química se monitorizan varios lotes de producción, cada uno con un valor de temperatura y de concentración. Se requiere un programa que:
#Solicite un número entero n, indicando cuántos lotes se van a registrar.
#Use un ciclo para leer la información de cada lote:
#temperatura (entero)
#concentración (entero)
#Almacene los pares (temperatura, concentración) en una lista llamada lotes.Cuidado de no confundir la palabra magnetismo con la temperatura o la concentración.
#Una vez registrada la información:
#Calcule cuántos lotes tienen temperatura superior a 100.
#Calcule el promedio de concentración de todos los lotes.
#Verifique si la temperatura promedio es mayor a la concentración promedio, imprimiendo un mensaje que indique si el proceso podría ser “inestable”.


n=int(input("ingrese el numero de lotes a registrar:  "))
n_lotes=[]
for i in range(n):
    print(f"registro del lote {i + 1}:")
    temperatura = int(input("ingrese la temperatura: "))
    concentracion = int(input("ingrese la concentracion: "))
    n_lotes.append((temperatura,concentracion))
    lotes_de_temperatura_superior = sum(1 for temperatura, _ in n_lotes if temperatura > 100)

    
concentracion_promedio = sum(concentracion for _, concentracion in n_lotes) / n

    
temperatura_promedio = sum(temperatura for temperatura, _ in n_lotes) / n

    
if temperatura_promedio > concentracion_promedio:
    mensaje_de_estabilidad = "el proceso podria ser inestable"
          
else:
    mensaje_de_estabilidad = "el proceso parece estable"

    
print("resultados:")
print(f"lotes con temperatura superior a 100: {lotes_de_temperatura_superior}")
print(f"promedio de concentracion: {concentracion_promedio}")
print(f"promedio de temperatura: {temperatura_promedio}")
print(mensaje_de_estabilidad)



