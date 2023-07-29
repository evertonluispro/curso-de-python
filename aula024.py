nome = input('Digite seu nome: ')
encontrar = input('Digite quem você quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em nome')
else:
    print(f'{encontrar} não está em nome')