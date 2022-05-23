# input

c1 = int(input("Ingreos de Pedro: "))
c2 = int(input("Ingresos de Juan: "))
c3 = int(input("Igresos necesarios: "))
n = 0
# processing

while (c1+c2) < c3:
    c1 = c1 + c1 * 0.03
    c2 = c2 + c2 * 0.04
    n = n + 1

print("Los meses necesarios para completar la inversión son: " + str(n))