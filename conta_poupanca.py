from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, agencia: int, numero_conta: int):
        super().__init__(agencia, numero_conta)
        
    def sacar(self, valor) -> str:
        return super().sacar(valor)
    
    def extrato(self) -> None:
        return super().extrato()

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.AGENCIA!r}, {self.NUMERO_CONTA!r}, {self.SALDO!r})'
        return f'{class_name}{attrs}'