"""Determina si dos palabras son anagramas.

- Ejemplos:
  - `"roma"` y `"amor"` → `True`
  - `"python"` y `"java"` → `False`"""

p1 = "roma"
p2 = "amor"


if p1 == p2[::-1]:
  print(True)
else:
  print(False)
