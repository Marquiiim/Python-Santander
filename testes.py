"""
contador = 1

while contador <= 5:
    print(contador * 2)
    contador += 1
"""

"""
contador = 0

while True:
    print(contador)
    contador += 1

    if contador == 5:
        break
"""

"""
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
"""

"""
números = [1, 2, 3, 4, 5]

quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados)
"""

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}


intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}


diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}


diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}