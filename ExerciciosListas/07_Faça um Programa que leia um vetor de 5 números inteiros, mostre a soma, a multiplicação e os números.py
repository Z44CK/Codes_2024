numeros_inteiros = []

for i in range(5):
    numeros = int(input(f"Informe o {i+1}ª numero inteiro: "))
    numeros_inteiros.append(numeros)

    soma = sum(numeros_inteiros)
    qtd_inteiros = numeros_inteiros

    multiplicacao = 1
    for numero in numeros_inteiros:
        multiplicacao *= numero

    print(f"Soma dos numeros:", soma)
    print(f"Multiplicação dos numeros: {multiplicacao:.2f}")
    print(f"Os valores que estão na lista:", qtd_inteiros)
