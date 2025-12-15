from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente
from cliente import Cliente

if __name__ == "__main__":
    cliente = Cliente('Eduardo', 23)
    cliente.conta = ContaCorrente(111, 123)
    cliente.conta.depositar(120)
    cliente.conta.extrato()
    print(cliente.conta)
    print(cliente)

    cliente2 = Cliente('Larissa', 28)
    cliente2.conta = ContaPoupanca(111, 124)
    cliente2.conta.depositar(120)
    cliente2.conta.extrato()
    print(cliente2.conta)
    print(cliente2)

