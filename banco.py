from conta import Conta
from cliente import Cliente
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

class Banco:
    def __init__(self, nome_agencia: str, agencia: int) -> None:
        self.clientes : list[Cliente] | list = []        
        self.contas : list[Conta] | list = []
        self.agencia : int = agencia
        self.nome_agencia : str = nome_agencia

    def _verificacao_agencia(self, numero_agencia : int) -> bool:
        if numero_agencia == self.agencia:
            return True
        return False

    def _verificacao_conta(self, conta : int) -> bool:
        for conta_agencia in self.contas:
            if conta == conta_agencia.NUMERO_CONTA:
                return True
        return False

    def _verificacao_cliente(self, cliente : Cliente) -> bool:
        if cliente in self.clientes:
            return True
        return False

    def autenticacao(self, cliente: Cliente, conta: Conta) -> bool:
        return self._verificacao_agencia(conta.AGENCIA) \
            and self._verificacao_cliente(cliente) \
            and self._verificacao_conta(conta.NUMERO_CONTA) \
            and cliente.conta is conta
        

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.contas!r}'\
            f'{self.clientes!r}) '\
            f'Agencia: {self.nome_agencia} {self.agencia}'
        return f'{class_name}{attrs}'