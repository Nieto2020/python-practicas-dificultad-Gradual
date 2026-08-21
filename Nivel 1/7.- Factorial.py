#Calcula:
#5! = 5 × 4 × 3 × 2 × 1 = 120
#Restricción: no uses `math.factorial()`
#formula n! = n x (n-1) x (n-2)... x 1

n = 5
acumulador = 1

for i in range(n,1,-1):
    acumulador *= i

print(acumulador)