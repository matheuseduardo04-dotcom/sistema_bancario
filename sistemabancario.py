def depositar(saldo, valor, extrato, numero_depositos):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        numero_depositos += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_depositos


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def exibir_quantidade(numero_saques, numero_depositos):
    opcoes = input("Qual opção você quer saber a quantidade(saques ou depositos)?: ")
    if opcoes == "saques":
        print(numero_saques)
    else:
        print(numero_depositos)


def main():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [quantidade]
    [q] Sair

    => """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_depositos = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato, numero_depositos = depositar(
                saldo, valor, extrato, numero_depositos
            )

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "quantidade":
            exibir_quantidade(numero_saques, numero_depositos)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
