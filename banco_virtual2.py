def menu():
    menu = """
    |==========MENU=============|
    |       [d] Depositar       |
    |       [s] Sacar           |
    |       [e] Extrato         |
    |   	[n] Nova conta      |
    |       [l] Listar conta    |
    |       [u] Novo Usuário    |
    |       [q] Sair            |
    |======BancoVirtual=========|
    Digite a operação desejada
    => """
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:{valor:.2f}"
        print("|== Deposito realizado com sucesso! ==|")
    else:
        print(" ## Falha na Operação, valor informado não é valido ## ")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    acima_saldo = valor > saldo
    acima_limite = valor > limite
    acima_saques = numero_saques >= limite_saques

    if acima_saldo:
        print("## Falha na Operação: Saldo insuficiente!! ##")

    elif acima_limite:
        print("## Falha na Operação: Saque excede o seu limite diário ##")

    elif acima_saques:
        print("## Falha na Operação: Limite de saques diario excedido! ##")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saques: {valor:.2f}"
        numero_saques += 1
        print(" |== Saque realizado com sucesso! ==|")

    else:
        print("## Falha na Operação: Valor inválido!! ##")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def cadastro_usuario(usuarios):
    cpf = input("insira o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(" ## Falha na Operação: CPF já cadastrado ! ## ")
        return

    nome = input("digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aa)")
    endereco = input("Digite seu endereço(rua - nro - bairro - cidade/sigla - estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("|== Novo Usuario Inserido no Sistema ==")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("## Falha na Operação: Usuario não encontrado, ciração de conta encerrada!! ##")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        ================= contas =================                                    
            Agência:{conta['agencia']}            
            C/C:{conta['numero_conta']}          
            Titular:{conta['usuario']['nome']}   
        ==========================================
        """
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            cadastro_usuario(usuarios)

        elif opcao == "n":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
