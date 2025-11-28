from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta):
        self.AGENCIA = agencia
        self.NUMERO_CONTA = numero_conta
        self.SALDO = 0.0
        self.VALOR_BONUS = 100.0


    def sacar(self, valor: float):
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor do saque deve ser numérico.")

        if valor <= 0:
            raise ValueError("O saque precisa ser maior que zero.")

        if valor > self.SALDO + self.VALOR_BONUS:
            raise ValueError("Não é possível sacar um valor maior que o existente.")

        valor_original = valor

        
        if valor <= self.SALDO:
            self.SALDO -= valor
            valor = 0
        else:
            valor -= self.SALDO
            self.SALDO = 0

        if valor > 0:
            self.VALOR_BONUS -= valor

        print(f"Sacado: R${valor_original:.2f}")


    def extrato(self):
        print(f'Valor bonus: R${self.VALOR_BONUS:.2f}',end=' | ')
        print(f'Saldo atual: R${self.SALDO:.2f}\n')
        print('='*20)