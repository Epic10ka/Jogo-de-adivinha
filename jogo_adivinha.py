from random import randint
while True:
    print('——'*20)
    print('\033[1;35mJOGO DE ADIVINHAÇÃO\033[m'.center(50))
    print('——'*20)
    print('Você tem \033[1;34m10 TENTATIVAS!\033[m'.center(50))
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
            print(f'Você precisou de \033[1;33m{contagem}\033[m palpites para acertar.')
        if contagem > 10:
            print('\033[1;33mAcabaram suas tentativas\033[m'.center(50))
            break
    print('——'*20)
    print('——'*20)
    print()#Aparência da interface
    print()#Aparência da interface
    continuar = str(input('     \033[1mQuer Jogar de novo?\033[m (\033[1;92mSIM\033[m/\033[1;31mNÃO\033[m): ')).upper().strip()
    if continuar.startswith('N'):
        break
from time import sleep
sleep(0.4)
print('Ok')
sleep(0.6)
print('Finalizando...')
sleep(1)
for c in range (3, 0, -1):
    print(c)
    sleep(0.8)

#nice dms
