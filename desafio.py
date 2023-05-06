menu = """

[1] Depósito
[2] Saque
[3] Extrato
[0]Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor_deposito = int(input("Qual o valor do depósito? "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito de R${valor_deposito:.2f}\n"
        else:
            print("Operção falhou. Valor inválido.")

    elif opcao == 2:

        if numero_saques == 3:
            print("Operação falhou. Limite de saques diário atingido.")
        elif numero_saques <= 3:
            valor_saque = float(input("Qual o valor do saque? "))

            if valor_saque > 500:
                print("Operação falhou, valor ultrapassa o limite.")
            elif valor_saque > saldo:
                print("Operação falhou. Saldo insuficiente.")    
            elif valor_saque > 0:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque de R${valor_saque:.2f}\n"
            else:
                print("Operação falhou. O valor informado é inválido.")
            
    elif opcao == 3:
        print("========= Banco Barbosa ========\n")
        print("Não foram realizadas movimentações.\n" if not extrato else extrato)
        print(f"Saldo R${saldo:.2f}")
        print("".center(32,"="))

    elif opcao == 0:
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")

print("Obrigado por usar o banco Barbosa. Tenha um ótimo dia.")
