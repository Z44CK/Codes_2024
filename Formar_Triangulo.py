def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def entrada_usuario():
    comprimentos = []
    for i in range(3):
        while True:
            try:
                comprimento = int(input(f'Digite o comprimento do graveto: '))
                comprimentos.append(comprimento)
                break
            except ValueError:
                print('Por favor, informe um numero inteiro valido!')
    return comprimentos


def verifica_triangulo(comprimentos):
    if is_triangle(*comprimentos):
        print("Os gravetos com os comprimentos dados podem formar um triangulo.")
    else:
        print("Os gravetos com os comprimentos dados não podem formar um triangulo.")


graveto = entrada_usuario()
verifica_triangulo(graveto)
