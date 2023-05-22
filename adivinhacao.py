print(31 * "*")
print("Bem vindo ao jogo de advinhação")
print(31 * "*")

numero_secreto = 42

tentativas = 3
rodada = 1

while (rodada <= tentativas):

    # Lembre-se que a função input, sempre devolve uma string.
    print(f'Tentativa: {rodada} de {tentativas}')
    chute = int(input('Digite um número: '))

    print(f'Você chutou: {chute}')

    if (chute == numero_secreto):
        print('Parabéns! Você acertou.')
    else:
        print('Não foi dessa vez, continue tentando.')

    rodada += 1