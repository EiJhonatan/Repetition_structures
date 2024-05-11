print("1 - coxinha -$5.00")
print("2 - Pastel -$7.00")
print("3 - cafe -$4.00")
print("4 - Suco -$6.00")
print("5 - SAIR")

total = 0

while True:
    op = int(input("QUAL ITEM GOSTARIA DE COMPRA? "))
   

    if(op ==1):
         qtd = int(input("QUANTAS UNIDADES QUER COMPRAR? "))
         total = total + qtd * 5.00
         
    elif(op ==2):
        qtd = int(input("QUANTAS UNIDADES QUER COMPRAR? "))
        total = total + qtd * 7.00
       
    elif(op ==3):
         qtd = int(input("QUANTAS UNIDADES QUER COMPRAR? "))
         total = total + qtd * 4.00
         
    elif(op ==4):
        qtd = int(input("QUANTAS UNIDADES QUER COMPRAR? "))
        total = total + qtd * 6.00 
        
    elif(op ==5):
       break
    else:
        print("PRODUTO INVALIDO. SELECIONE OUTRO.")

print(f"o TOTAl da ser pago de de {total} REAIS.")

