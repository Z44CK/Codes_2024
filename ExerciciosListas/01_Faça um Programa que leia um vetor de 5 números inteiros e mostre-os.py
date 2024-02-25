# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os?

def ler_vetor():  # Função que lê um vetor de 5 inteiros
    print("Informe 5 numeros inteiros: ")
    # Utilizndo list comprehension para ler os 5 numeros fornecidos pelo usuario
    vetor = [int(input()) for _ in range(5)]
    return vetor


def mostrar_vetor(vetor):  # Mostra os valores contidos no vetor
    print("Os numeros no vetor são: ")
    # Cria uma lista para mostrar os valores no vetor
    numero = [x for x in vetor]
    print(numero)


vetor_lido = ler_vetor()  # Chama a função para ler os numeros fornecidos
mostrar_vetor(vetor_lido)  # Chama a função para imprimir os numeros lidos na tela
