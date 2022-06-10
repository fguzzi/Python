print('ADVINHE O NÚMERO...')
print('=' * 30)
from random import randint
while True:
    print('Sorteei um número de 1 a 10. Tente advinhar !!')
    print('Você terá 3 chances !!')
    sorteio = randint(1, 10)
    cont = 0
    while True:
        if cont > 3:
            print('MAIS DE 3 TENTATIVAS. VOCÊ PERDEU !')
            break
        palpite = int(input('Digite seu palpite: '))
        if palpite == sorteio:
            print('VOCÊ  VENCEU !')
            break
        else:
            if palpite > sorteio:
                print('É menor !')
                cont += 1
            if palpite < sorteio:
                print('É maior !')
                cont += 1
    op = str(input('Jogar novamente? [ S/N ]: ')).strip().upper()
    if op == 'N':
        print('ENCERRADO.')
        break
