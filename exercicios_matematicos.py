# --> Atividade da Semana 02 <-- #

# Primeiro Exercício: #
# Um freelancer está com dificuldade para calcular qual valor cobrar por um projeto que está estimado em 80 horas. Após pensar e revisitar o preço de alguns projetos que cobrou no passado, ele montou a seguinte fórmula: valor inicial + quantidade de horas estimadas * valor da hora + 15% do valor calculado. Crie um programa que faça essa conta para o freelancer. Considere que o valor inicial sempre será R$ 1000,00 e o valor da hora cobrada é de R$ 20,45. A aplicação deve imprimir o valor calculado pelo projeto considerando duas casas decimais na formatação do valor. #

# Resolução: #
valor_inicial = 1000
quantidade_horas = int(input("Quantas horas estimadas para o projeto? "))
valor_hora = 20.45

resultado_inicial = valor_inicial + (quantidade_horas * valor_hora)
valor_total = resultado_inicial + resultado_inicial * 0.15
print(f"O valor a ser cobrado pelo projeto é de: R${valor_total:.2f}")

# Quebrando linha #
print()

# Segundo Exercício: #
# Uma nave espacial recebe as pessoas com uma mensagem de boas vindas de acordo com o nome que elas forneceram ao fazer o cadastro na recepção. Crie uma aplicação que imprima a mensagem de boas vindas de acordo com os nomes na lista: nomes = [“Elysson“, “Giulia“, “Willian“, “Gileno“], com a seguinte mensagem: “Olá, NOME_PESSOA! Seja bem vindo à nave Imperial dos Siths.”. Crie um programa que faça a interpolação da string de boas vindas, substituindo o NOME_PESSOA pelo nome lido na lista e imprimindo a frase de boas vindas com o nome substituído. # 

# Resolução: #
nomes = ["Elysson", "Giulia", "Willian", "Gileno"]
for nome in nomes:
  print(f"Olá, {nome}! Seja bem vindo à nave Imperial dos Siths.")