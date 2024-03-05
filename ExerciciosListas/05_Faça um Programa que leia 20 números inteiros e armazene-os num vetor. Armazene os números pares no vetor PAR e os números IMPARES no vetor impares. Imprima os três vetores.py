# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores
def vetor_int():
    vetor = []
    for i in range(20):
        number = int(input(f"Informe o {i+1} numero inteiro: "))
        vetor.append(number)
    return vetor


def vet_par_impar(vetor):
    par = []
    impar = []
    for number in vetor:
        if number % 2 == 0:
            par.append(number)
        elif number % 2 == 1:
            impar.append(number)

    print(f"A quantidade de inteiros é: {len(vetor)}")
    print(f"A quantidade de numeros pares é: {len(par)}")
    print(f"A quantidade de numeros impares é: {len(impar)}")

# Lê o vetor de 20 numeros
qtd_vetor = vetor_int()

# Separa os numeros pares e impares, e imprime a quantidade de cada
vet_par_impar(qtd_vetor)
