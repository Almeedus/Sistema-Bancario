# 🏦 Desafio: Sistema Bancário em Python (POO)

Este projeto implementa um **sistema bancário simples** utilizando os quatro pilares da Programação Orientada a Objetos:

- **Abstração**
- **Encapsulamento**
- **Herança**
- **Polimorfismo**

O objetivo é criar um mini-sistema onde **clientes** utilizam **contas bancárias** (corrente ou poupança) e interagem com um **banco** que valida e autoriza operações.

---

## 📌 Funcionalidades Implementadas

- Criar clientes e vincular suas contas.
- Criar contas corrente (com limite extra) e contas poupança.
- Realizar **depósitos**.
- Realizar **saques**, respeitando regras específicas de cada conta.
- Autenticação do banco para permitir saques:
  - Verifica se a **agência** pertence ao banco.
  - Verifica se o **cliente** pertence ao banco.
  - Verifica se a **conta** está cadastrada no banco.

---

## 🧱 Estrutura do Projeto

### **Classes Base (Abstração)**

#### `Pessoa` (Classe Abstrata)
- Atributos:
  - `nome`
  - `idade`
- Possui getters protegidos.

#### `Conta` (Classe Abstrata)
- Atributos:
  - `agencia`
  - `numero_conta`
  - `saldo`
- Métodos:
  - `depositar(valor)`
  - `sacar(valor)` → **abstrato** (polimorfismo aplicado nas subclasses)

---

### **Classes Derivadas (Herança e Polimorfismo)**

#### `Cliente` → herda de `Pessoa`
- Possui uma **conta** (agregação):
  - `ContaCorrente` ou `ContaPoupanca`

#### `ContaPoupanca` → herda de `Conta`
- Implementa o método `sacar()` com regras específicas.

#### `ContaCorrente` → herda de `Conta`
- Atributo adicional:
  - `limite_extra`
- Implementa `sacar()` usando saldo + limite.

---

## 🏛️ Classe Banco (Agregação + Autenticação)

O banco mantém:

- Lista de **clientes**
- Lista de **contas**

Responsabilidades:

- Registrar clientes e contas.
- Autenticar operações através de:
  - Verificação da **agência**
  - Verificação do **cliente**
  - Verificação da **conta**

Apenas após a autenticação o saque é permitido.

---

## 🔧 Tecnologias Utilizadas

- Python 3.x  
- `abc` (Abstract Base Classes)

---

## 📂 Estrutura de Arquivos

```
sistema_bancario/
├── banco.py
├── pessoa.py
├── cliente.py
├── conta.py
├── conta_corrente.py
├── conta_poupanca.py
├── main.py
└── README.md
```

---
