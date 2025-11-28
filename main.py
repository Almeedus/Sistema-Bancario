from conta import Conta
from conta_corrente import ContaCorrente

if __name__ == "__main__":
    conta1 = ContaCorrente(1,1)
    conta1.depositar(10.00)
    
    conta1.extrato()
    
    conta1.sacar(10.00)
    conta1.extrato()
    
    conta1.sacar(100.00)
    conta1.extrato()
    
