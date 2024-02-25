# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa


# Utilizando list comprehension para ler os numeros reais
vetor = [float(input(f"Digite o {i+1}º numero: ")) for i in range(10)]

# Mostra os numeros na ordem inversa utilizando "reversed"
print("Números na ordem inversa")
for numero in reversed(vetor):
    print(numero)
