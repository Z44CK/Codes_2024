# 01.Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

def ler_vetor():
    print("Informe 10 caracteres: ")
    vetor = []
    for _ in range(10):
        caractere = input().lower()
        vetor.append(caractere)
    return vetor


def mostrar_consoantes(vetor):
    consoantes = []
    for caractere in vetor:
        if caractere.isalpha() and caractere not in 'aeiou':
            consoantes.append(caractere)
    num_consoantes = len(consoantes)
    print(f"Foram lidas {num_consoantes} consoantes!")
    print(consoantes)


vetor_caractere = ler_vetor()
mostrar_consoantes(vetor_caractere)
