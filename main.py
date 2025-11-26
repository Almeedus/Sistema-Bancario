from conta import Conta

if __name__ == "__main__":
    conta1 = Conta(1,1)
    conta1.depositar(12)
    
    conta1.extrato()
    
    conta1.sacar(10)
    conta1.extrato()