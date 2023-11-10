# --> Atividade da Semana 03 <-- #

# Crie uma função que, ao receber um número inteiro, retorna se um número é par ou ímpar. #
def par_ou_impar():
  numero = int(input("Digite um número: "))
  if numero % 2 == 0:
    return print("Par")
  else:
    return print("Ímpar")
par_ou_impar()

# Quebrando linha #
print()

# Crie uma função que recebe um número inteiro por parâmetro e então imprime na tela do número recebido até o zero. #
def sequencia_descrescente():
  numero = int(input("Digite um número: "))
  if numero < 0:
    for i in range(numero, -1, 1):
      print(i, end=" ")
  else:
        for i in range(numero, -1, -1):
            print(i, end=" ")
sequencia_descrescente()

# Quebrando linha #
print()

# Crie um programa com uma função que necessite de três parâmetros e então que retorne a sua soma. #
def soma_tripla():
   numero_1 = int(input("Digite o primeiro número: "))
   numero_2 = int(input("Digite o segundo número: "))
   numero_3 = int(input("Digite o terceiro número: "))
   resultado = numero_1 + numero_2 + numero_3
   return print(f"A soma desses três números é: {resultado}")
soma_tripla()

# Quebrando linha #
print()

# Crie um programa que seja capaz de obter e somar TODOS os números passados pelo usuário como entrada, permitindo somar qualquer quantidade de dados de entrada. #
def soma_numeros():
   numeros = []
   while True:
      entrada = input("Digite um número ou 'exit' para finalizar: ")
      if entrada.lower() == 'exit':
         break
      try:
         numero = int(entrada)
         numeros.append(numero)
      except ValueError:
         print("Entrada inválida. Por favor, insira um número válido.")
   if numeros:
    soma = sum(numeros)
    print(f"A soma dos números é: {soma}")
   else:
      print("Nenhum número foi inserido.")
soma_numeros()

# Quebrando linha #
print()

# Faça um programa com uma função que necessite de um parâmetro. A função deve retornar “Positivo”, se seu o número for maior que zero, “Negativo” se o número for menor que zero, e “Zero” se o número for igual a zero. #
def positividade(numero):
   if numero > 0:
      return "Positivo"
   elif numero < 0:
      return "Negativo"
   else:
      return "Zero"
numero = int(input("Digite um número: "))
resultado = positividade(numero)
print(f"O número é {resultado}!")

# Quebrando linha #
print()

# Escreva uma função que, dado o valor da conta de um restaurante e um percentual de taxa de serviço, calcule e exiba a gorjeta do garçom, considerando o percentual do valor da conta. #
def calcular_gorjeta(valor_conta, percentual_taxa):
    gorjeta = valor_conta * (percentual_taxa / 100)
    return gorjeta
valor_conta = float(input("Digite o valor da conta: R$ "))
percentual_taxa = float(input("Digite o percentual de taxa de serviço: "))
gorjeta = calcular_gorjeta(valor_conta, percentual_taxa)
print(f"A gorjeta do garçom é: R$ {gorjeta:.2f}")

# Quebrando linha #
print()

# Crie uma função que permita contar o número de vezes que aparece uma determinada letra em uma frase. A letra desejada e a frase a ser verificada serão passadas por parâmetro para a função, que retornará a quantidade da letra na frase. #
def contar_letra(frase, letra):
    return frase.count(letra)
frase = input("Digite a frase: ")
letra_desejada = input("Digite a letra que deseja contar: ")
resultado = contar_letra(frase, letra_desejada)
print(f"A letra '{letra_desejada}' aparece {resultado} vezes na frase.")

# Quebrando linha #
print()

# Crie uma função que receba duas palavras e retorne “True” caso a primeira palavra seja um prefixo da segunda, e “False” caso contrário. #
def verificar_prefixo(palavra1, palavra2):
    if palavra2.startswith(palavra1):
        return True
    else:
        return False
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
resultado = verificar_prefixo(palavra1, palavra2)
print(resultado)
