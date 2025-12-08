import abc

class Conta(abc.ABC):   
    def __init__(self, agencia: int, numero_conta: int):
        self.AGENCIA = agencia
        self.NUMERO_CONTA = numero_conta
        self.SALDO = 0.0

    @abc.abstractmethod    
    def sacar(self, valor: float):
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor do saque deve ser numérico.")

        if valor <= 0:
            raise ValueError("O saque precisa ser maior que zero.")
        
        if valor > self.SALDO:
            raise ValueError("Não é possível sacar um valor maior que o existente.")

        self.SALDO -= valor
        return f'Sacado: R${valor:.2f}'

    def depositar(self, valor: float):
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor do depósito deve ser numérico.")

        if valor <= 0:
            raise ValueError("O depósito precisa ser maior que zero.")

        self.SALDO += valor
        return f'Depositado: R${valor:.2f}'

    @abc.abstractmethod
    def extrato(self):
        print(f'Saldo atual: R${self.SALDO:.2f}\n')
