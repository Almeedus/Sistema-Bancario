from banco import Banco, ContaPoupanca, ContaCorrente, Cliente

if __name__ == "__main__":
    santander = Banco('Santander', 111)
    
    pessoa1 = Cliente('Eduardo', 23)
    pessoa1.conta = ContaCorrente(111,123)

    pessoa2 = Cliente('Larissa', 28)
    pessoa2.conta = ContaPoupanca(111,11001)
    
    santander.clientes.extend([pessoa1, pessoa2])
    santander.contas.extend([pessoa1.conta, pessoa2.conta])

    if santander.autenticacao(pessoa1, pessoa2.conta):
        pessoa1.conta.extrato()
        
        pessoa1.conta.sacar(100)
        
        pessoa1.conta.extrato()
    else:
        print(f'Autenticação Inválida')
