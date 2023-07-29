"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
0123456
everton

    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se contém espaços (ou não)
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpa, você deixou campos vazios."
"""

nome = input('Escreva seu nome: ')
idade = input('Escreva sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpa, você deixou campos vazios.")