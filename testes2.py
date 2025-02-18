"""
def calcular_media(*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media

print("Media: ", calcular_media(10, 20, 30, 40))

somar = lambda x: x + 3

print("Somar 3 a um número: ", somar(5))
"""

"""
try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")
"""

arquivo = open("teste.txt", "w")
arquivo.write("Testando escrita!")
arquivo.close()

arquivo = open("teste.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

with open("teste.txt", "w") as arquivo:
    arquivo.write("Teste escrita novamente!")

with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)