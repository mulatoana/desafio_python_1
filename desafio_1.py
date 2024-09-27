#DESAFIO
#deposito - valores positivos armazenados em uma lista e exibido na operação extrato
#saque - três saques diarios, com limite de 500. Se nao tiver saldo, informar que nao sera possivel, armazenar em uma lista para mostrar no extrato
#extrato - exibir depositos, saques e saldo atual da conta

menu = '''
Bem vindo ao Banco Dio

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Insira a opção: 
'''

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
            extrato += f"Depósito: R$ {valor: .2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite")
        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saque += 1
        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "e":
        print("\n=========================== EXTRATO ============================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("==================================================================")
        
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione uma opção válida")