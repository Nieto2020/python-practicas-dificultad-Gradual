#Dado `N`, calcula la suma:
#ejmp
#1 + 2 + 3 + ... + N

#Restricción:** no uses una fórmula matemática; utiliza un ciclo.

n = 7
acumulador = 0

for i in range(1, n+1):
    print(i)
    acumulador += i
print(acumulador)
