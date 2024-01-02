def check_fermat(a, b, c, n):
    try:
        a, b, c, n = int(a), int(b), int(c), int(n)
        if n > 2 and (a**n + b**n == c**n):
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work.")
    except ValueError:
        print('Por favor, insira valores inteiros válidos')


def etrada_do_usuario():

    a = input('Digite o valor de a: ')
    b = input('Digite o valor de b: ')
    c = input('Digite o valor de c: ')
    n = input('Digite o valor de n (deve ser maior que 2): ')
    return a, b, c, n


def main():
    valores = etrada_do_usuario()

    if valores:
        a, b, c, n = valores
        check_fermat(a, b, c, n)


if __name__ == "__main__":
    main()
