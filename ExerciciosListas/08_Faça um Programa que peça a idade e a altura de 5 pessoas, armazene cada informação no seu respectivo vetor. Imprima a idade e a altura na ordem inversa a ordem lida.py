# Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
idades = []
alturas = []
# Coletando as informações de idade e altura
for i in range(5):
    idade = int(input(f"Informe a idade da {i+1}ª pessoa: "))
    altura = float(input(f"Informe a altura da {i+1}ª pessoa (em metros): "))
    idades.append(idade)
    alturas.append(altura)

# Imprime a idade e a altura das 5 pessoas na ordem inversa
print("Idades na ordem inversa: ")
for idade in reversed(idades):
    print(idade)

print("\nAlturas na ordem inversa: ")
for altura in reversed(alturas):
    print(altura)
