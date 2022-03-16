"""
Recebendo dados do usuário

input() -> Todos os dados recebidos do input é do tipo string

Em Python. string é tudo que estiver entre aspas:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas.

Exemplo:
- Aspas  simples -> 'Angelina Jolie'
- Aspas duplas -> "Anelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""
# - Apas duplas triplas -> """Agenlina Jolie """

#  Entrada de dados
# print("Qual seu nome? ")
# nome = input()  # Input -> Entrada

# print('Qual a sua idade? ')
# idade = input()

nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")
#  Processamento
nome = nome.replace("W", "U")

#  Saída de dados

# Exemplo de print da versão 2.X
# print('Seja bem-vindo(a) %s' % nome)
# print('A %s tem %s anos' % (nome, idade))

# Exemplo de print moderno da versão 3.X
# print('Seja bem-vindo(a) {0} '.format(nome))
# print(('A {0} tem {1} anos'.format(nome, idade)))

# Exemplo de print mais atual
print(f'Seja bem-vinda(a) {nome}')
print(f'A {nome} tem {idade}')


"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro
"""
print(f'A {nome} nasceu em {2018 - int(idade)}')
