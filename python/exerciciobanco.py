saldo = 1000.0
extrato = []

while True:

    print("\n=============================")
    print("        BANCO PYTHON")
    print("=============================")
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Extrato")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print(f"\nSaldo atual: R$ {saldo:.2f}")

    elif opcao == "2":

        valor = float(input("Valor para depositar: R$ "))

        if valor > 0:

            saldo += valor

            extrato.append(f"Depósito: R$ {valor:.2f}")

            print(f"Depósito realizado com sucesso!")
            print(f"Novo saldo: R$ {saldo:.2f}")

        else:
            print("Valor inválido!")

    elif opcao == "3":

        valor = float(input("Valor para sacar: R$ "))

        if valor <= 0:

            print("Valor inválido!")

        elif valor > saldo:

            print(f"Saldo insuficiente. Saldo disponível: R$ {saldo:.2f}")

        else:

            saldo -= valor

            extrato.append(f"Saque: R$ {valor:.2f}")

            print(f"Saque realizado com sucesso!")
            print(f"Novo saldo: R$ {saldo:.2f}")

    elif opcao == "4":

        print("\n--- Extrato ---")

        if len(extrato) == 0:

            print("Nenhuma operação realizada.")

        else:

            for operacao in extrato:

                print(operacao)

    elif opcao == "5":

        print(f"\nSaldo final: R$ {saldo:.2f}")
        print("Obrigado!")

        break

    else:

        print("Opção inválida!")
        