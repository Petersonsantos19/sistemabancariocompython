menu = """

====MENU====

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

============
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação não concluida! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Erro! Voçe não tem saldo suficiente.")
        
        elif valor > limite:
            print("Erro! Voçe excedeu o valor de limite de saque de R$500.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Erro! Limite de 3 saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Erro! O valor informado é inválido.")

    elif opcao == "e":
        print("EXTRATO".center(20, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("FIM".center(20, "="))

    elif opcao == "q":
        print("Obrigado pela preferencia!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")    

