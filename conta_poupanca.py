from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta):
        super().__init__(agencia, numero_conta)
        
    def sacar(self, valor):
        return super().sacar(valor)
    
    def extrato(self):
        return super().extrato()