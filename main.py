from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente

if __name__ == "__main__":
    conta1 = ContaPoupanca(1,1)
    conta1.depositar(100.00)
    
    conta1.extrato()
    
    conta1.sacar(10.00)
    conta1.extrato()
    
    conta1.sacar(50.00)
    conta1.extrato()
    
