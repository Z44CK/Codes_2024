# Faça um Programa que leia 4 notas, mostre as notas e a média na tela

# Solicita o usuario que informe 4 notas e armazena-os em uma lista chamada 'n'
n = [float(input(f"Informe {i+1} notas: ")) for i in range(4)]

# Calcula a média das notas, somando e dividindo todas as notas pelo numero tota de notas
media = sum(n) / len(n)

# Exibe as notas dentro da lista
print(f'As notas contidas na lista: {n}')

# Exibe a media final das notas
print(f'A media final é: {media:.2f}')
