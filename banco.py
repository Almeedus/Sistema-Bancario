from conta import Conta
from pessoa import Pessoa

class Banco:
    def __init__(self, cliente: Pessoa, conta: Conta) -> None:
        self._clientes : list[Pessoa] = []        
        self._contas : list[Conta] = []

        if cliente:
            self._clientes.append(cliente)


        if conta:
            self._contas.append(conta)