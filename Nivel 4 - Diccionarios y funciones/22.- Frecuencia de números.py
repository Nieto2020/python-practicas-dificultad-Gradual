"""
Entrada: [1, 2, 2, 3, 3, 3, 4]
Salida:

python
{
    1: 1,
    2: 2,
    3: 3,
    4: 1
}
"""
X = [1, 2, 2, 3, 3, 3, 4]

out = {}

for i in X:
    if i not in out:
        out[i] = 1
    else:
        out[i] += 1

print(out)