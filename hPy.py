def eje1():
    print("ingrese un numero1")
num1=int(input())
print("ingrese un numero2")
num2=int(input())
r=num1+num2
print("el resultado es:",r)
eje1()

def eje2():
    print("ingrese un numero1")
num1=int(input())
print("ingrese un numero2")
num2=int(input())
print("ingrese un numero3")
num3=int(input())
print("ingrese un numero4")
num4=int(input())
r=num1+num2+num3+num4
print("el resultado es:",r)
eje2()

def eje3():
    print("ingrese lado1 del rectangulo")
num1=int(input())
print("ingrese lado2 del rectangulo")
num2=int(input())
r=num1*num2
print("la superficie del rectangulo es",r)
eje3()

def eje4():
    print("ingrese el lado del cuadrado")
num1=float(input())
r=num1*num1
print("la superficie del cuadrado es:",r)
eje4()

def eje5():
    print("ingrese una hora")
num1=int(input())
print("ingrese minutos")
num2=int(input())
print("ingrese segundos")
num3=int(input())

ra=num1*3600
rb=num2*60
resu=ra+rb+num3
print("segundos: ", resu)
eje5()

def eje6():
    print("ingrese la base del triangulo")
num1=float(input())
print("ingrese la altura del triangulo")
num2=float(input())
r=num1*num2*0.5
print("superficie del triangulo:",r)
eje6()

def eje7():
    print("ingrese 6 numeros")
    sumaxd=0
    for i in range(6):
        n=float(input())
        sumaxd+=n
p=sumaxd/6
print("el promedio es:",p)
eje7()

def eje8():
    print("ingrese parcial")
parcial=int(input())
print("ingrese total")
total=int(input())

r=(parcial*100)/total
print("el porcentaje es:",r,"%")
eje8()

def eje9():
print("Ingrese una fecha en formato DDMMAAAA:")
fecha = int(input())
anio=fecha-int(fecha/10000)*10000
resto=int(fecha/10000)
mes=resto-int(resto/100)*100
dia=int(resto/100)

print("Día:",dia)
print("Mes:",mes)
print("Año:",anio)
eje9()

def eje10():
    print("ingrese nota del examen parcial")
parcial=float(input())
print("ingrese nota del examen integrador")
integrador=float(input())
print("ingrese nota del tp")
tp=float(input())
nota=(parcial*0.3)+(tp*0.2)+(integrador*0.5)
print("la nota final es",nota)
eje10()

def eje11():
   print("Ingrese la cantidad de autos vendidos:")
autosvendi=int(input())

preciAu=[]
print("Ingrese el precio del auto:")
precio=float(input())

for i in range(autosvendi):
    preciAu.append(precio)

salariofijo=5500
comisionfija=autosvendi*200

adicionalxautos=0
for precio in preciAu:
    adicionalxautos+=precio*0.05
    
salarioTo=salariofija+comisionfija + adicionalxautos
print("El salario total del vendedor es: $", salarioTo)
eje11()
