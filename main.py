saldo = 0.0
acoes = []
flag = 0
def saque(dinheiro):
    global saldo, flag
    if dinheiro < saldo and flag < 3 and dinheiro <= 500:
        saldo = saldo - dinheiro
        flag += 1
        acoes.append(("-", dinheiro))
    else:
        print("Não é possivel sacar esse valor")
def deposito(dinheiro):
    global saldo
    if dinheiro > 0:
        saldo = saldo + dinheiro
        acoes.append(("+", dinheiro))
    else:
        print("Não é permitido depositar valores negativos")


def extrato():
    global saldo
    for ope, val in acoes:
        print("Seu extrato: " + ope + " " + str(val))
    print("Seu saldo é: R$ " + str(saldo))

print("Digite 1 para Depositar")
print("Digite 2 para Sacar")
print("Digite 3 para Visualizar")
print("Digite -1 para Sair")

sel = 0
while sel != -1:
    sel = int(input("Digite sua operação: "))
    if sel == 1:
        dim = float(input("Digite o valor que deseja depositar: "))
        deposito(dim)
    elif sel == 2:
        dim = float(input("Digite o valor que deseja sacar: "))
        saque(dim)
    elif sel == 3:
        extrato()
    else:
        print("Operação invalida!")