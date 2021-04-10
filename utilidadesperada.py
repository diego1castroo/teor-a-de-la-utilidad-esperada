import math
print("datos para la primera opcion\n")
x1 = float(input("ingresa cantidad a ganar:\t"))
p1 = float(input("ingresa probabilidad de ganar:\t"))
x2 = float(input("ingresa cantidad a perder:\t"))
p2 = float(input("ingresa probabilidad de perder:\t"))
print("\n\ndatos para la segunda opcion\n")
x11 = float(input("ingresa cantidad a ganar:\t"))
p11 = float(input("ingresa probabilidad de ganar:\t"))
x21 = float(input("ingresa cantidad a perder:\t"))
p21 = float(input("ingresa probabilidad de perder:\t"))
a = (p1 / 100)
b = (p2 / 100)
c = (p11 / 100)
d = (p21 / 100)

s1 = ((a*(pow(x1**2, 1/3))) - (b*(pow(x2**2, 1/3))))
s2 = ((c*(pow(x11**2, 1/3))) - (d*(pow(x21**2, 1/3))))


print("\nla opcion 1 queda de la siguiente manera:\nGanar ", x1," con ", p1, " de probabilidad o perder ", x2, " con ", p2, " de probabilidad ")
print("\t", s1, " unidades")
print("\nla opcion 2 queda de la siguiente manera:\nGanar ", x11," con ", p11, " de probabilidad o perder ", x21, " con ", p21, " de probabilidad ")
print("\t", s2, " unieades")

if(s1>s2):
	print("\n<<<<<<<<la mejor opcion es la numero 1>>>>>>>>")
else:
	print("\n<<<<<<<<la mejor opcion es la numero 2>>>>>>>>")