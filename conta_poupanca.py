from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, agencia: int, numero_conta: int):
        super().__init__(agencia, numero_conta)
        
    def sacar(self, valor) -> str:
        return super().sacar(valor)
    
    def extrato(self) -> None:
        return super().extrato()