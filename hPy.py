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

r1=num1*3600
print("horas a segundos",r1)
r2=num2*60
print("horas a minutos",r2)
print("segundos a segundos",num3)
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
    print("ingrese un numero1")
num1=int(input())
print("ingrese un numero2")
num2=int(input())
print("ingrese un numero3")
num3=int(input())
print("ingrese un numero4")
num4=int(input())
print("ingrese un numero5")
num5=int(input())
print("ingrese un numero6")
num6=int(input())

r=num1+num2+num3+num4+num4+num5+num6
p=r/6
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
    print("elegi una fecha")
array=[]
array=input()

print("el dia es:",array[0],array[1])
print("el mes es:",array[2],array[3])
print("el año es:",array[4],array[5],array[6],array[7])
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
    print("ingrese numero de autos")
n1=int(input())
print("ingrese valor de la unidad")
n2=float(input())

salario=5500+(n1*200)+(n2*0.05)
print("el salario es:",salario)
eje11()
