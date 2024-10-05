from moduloConta import Conta, ContaAutomatica

def exemplo2():
    novaConta = Conta('201-2',100.0)
    print(novaConta)
    novaConta.creditar(500.0)
    novaConta.saldo-=300
    print(novaConta)


def exemplo3():
    novaConta = Conta('201-2',100.0)
    contaBB = Conta('16.222-4',1000.0)
    contaBB.transferir(500,novaConta)
    print(novaConta)
    print(contaBB)

def exemplo4():
    novaConta = Conta('201-2',100.0)
    print(novaConta)
    atribuicao(novaConta)
    print(novaConta)

def atribuicao(conta):
    print(conta)
    conta = Conta('0001-x',0.0) 
    print(conta)

def exemplo5():
    cAutA = ContaAutomatica()
    cAutB = ContaAutomatica(100.0)
    cAutC = ContaAutomatica(1000.0)
    print(cAutA)
    print(cAutB)
    print(cAutC)

def exemplo6():
    valor=-1000.0
    if ContaAutomatica.validaSaldo(valor):
        c_a = ContaAutomatica(valor)
    else:
        print("Erro ao criar a conta.")

def exemplo7():
    if ContaAutomatica.validaNumero():
        c_a = ContaAutomatica(100.0)
        print('Conta criada.')
    else:
        print("Erro! Número de contas excedido.")

    c_a = ContaAutomatica(100.0)
    if c_a.validaNumero():
        print('Agência ainda disponível.')
    else:
        print("Erro! Número de contas excedido.")

if __name__ == '__main__':
    exemplo2()
