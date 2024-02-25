# Sem uso de list comprehension
# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

# Armazena os valores em uma lista
notas = [4.5, 6.5, 1.2, 3.2]

# Faz a soma das notas e a divide pela quantidade de notas 
media = sum(notas) / len(notas)

# Mostra as notas armazenadas na lista
print(f"As notas na lista: {notas}")

# Mostra a média total da soma de todas as notas
print(f"A media final é: {media:.2f}")
