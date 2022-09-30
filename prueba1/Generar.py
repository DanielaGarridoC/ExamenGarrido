import random
import csv

 
nregistros=int(input("Ingreso el numero de registros a generar: "))
valmax=int(input("valor numerico maximo a generar en las columnas: "))

    #for row in csv.reader(open('C:/Users/ALIENWARE/bd.csv')):
    #tessiu.objects.create(**dict(zip(fields, row)))


with open('bdmatutino.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(0,nregistros):
        texto= [random.randint(0, valmax), chr(random.randint(ord('A'), ord('Z'))) ,random.randint(0, valmax), random.randint(0, valmax)]
        writer.writerow(texto)