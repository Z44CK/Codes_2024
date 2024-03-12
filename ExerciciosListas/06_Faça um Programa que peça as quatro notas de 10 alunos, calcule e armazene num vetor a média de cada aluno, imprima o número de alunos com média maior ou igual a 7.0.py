def nota_alunos():
  # Lista para armazenar a média dos alunos
    media_alunos = []

  # Loop para cada aluno
    for i in range(10):
        print(f"Informações do aluno: {i+1}")
        notas = []

      # Loop para cada nota do aluno
        for j in range(4):
            nota = float(input(f"Informe a {j+1}ª nota do aluno(a): "))
            notas.append(nota)

      # Calcula a média das notas do aluno
        media = sum(notas) / len(notas)

      # Adiciona a média na lista dos alunos
        media_alunos.append(media)

    # Conta quantos alunos possui a nota maior ou igual a 7.0
    alunos_aprovados = sum(1 for media in media_alunos if media >= 7.0)

  # Imprime a quantidade de alunos aprovados
    print(f"O número de alunos com a média maior ou igual a 7.0: {alunos_aprovados}")


# Chama a função para executar o codigo
nota_alunos()
