# --> Atividade da Semana 04 <-- #

# Sistema de cadastro de novos clientes utilizando classe. #
# Apenas um protótipo para o cadastro de 5 clientes, mostrando após o cadastro os cinco clientes cadastrados. #

class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente (XXX.XXX.XXX-XX): ")
    idade = int(input("Digite a idade do cliente: "))
    return Cliente(nome, cpf, idade)

def main():
    lista_clientes = []

    for _ in range(5):
        novo_cliente = cadastrar_cliente()
        lista_clientes.append(novo_cliente)

    for cliente in lista_clientes:
        print("Cliente:", cliente.nome, "CPF:", cliente.cpf, "Idade:", cliente.idade)

if __name__ == "__main__":
    main()
