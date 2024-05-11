
pessoas = 0
valor = 0
dinheiro = 0
acc_idades = 0

while True:
    idade = int(input('QUAL SUA IDEDA? '))
    if idade ==0:
        break

    pessoas +=1
    acc_idades += idade

    if idade <3:
        ingresso = 0
       

    else:
        if idade > 12:
            ingresso = 30
      
        else:
            ingresso = 15

    dinheiro += ingresso

if pessoas >0:      
    media = acc_idades / pessoas
    
    print(f'o total de pessoas que compraram o ingressos {pessoas}.')
    print(f'o total de dinheiro a pagar ${dinheiro} .')
    print(f'MEDIA DE IDADE {media} .')