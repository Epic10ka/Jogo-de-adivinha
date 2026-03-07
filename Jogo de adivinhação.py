from random import randint
print('——'*20)
print('\033[1;35mJOGO DE ADIVINHAÇÃO\033[m'.center(50))
print('——'*20)
pc = randint(0, 10)
player = -1
contagem = 0
print()
while player != pc:
    player = int(input('          Adivinhe o número: '))
    print('——'*20)
    contagem += 1
    if player != pc:
        print('\033[1;31mVocê ERROU\033[m! \033[1mTente de novo\033[m.'.center(60))
        print()
    else:
        print(f'\033[1;92mParabéns!\033[m Você acertou! O número era {pc}')
print()
print('——'*20)
print(f'Você precisou de \033[1;33m{contagem}\033[m palpites para acertar.')
print('——'*20)

#nice