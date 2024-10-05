class Conta:
    def __init__(self, numero, saldo=0):
        self.numero=numero
        self.saldo=saldo
    def setNumero(self, novoNumero):
        self.numero = novoNumero
    def creditar(self,valor):
        self.saldo+=valor
    def debitar(self,valor):
        self.saldo-=valor
    def getNumero(self):
        return self.numero
    def getSaldo(self):
        return self.saldo
    def transferir(self, valor, contaDst):
        self.debitar(valor)
        contaDst.creditar(valor)
    def __str__(self):
        txt=f'Número = {self.numero}\nSaldo = {self.saldo}\n'
        return txt

class ContaAutomatica:
    proximaConta=1
    def __init__(self, saldo=0):
       self.numero=ContaAutomatica.proximaConta
       ContaAutomatica.proximaConta+=1
       self.saldo=saldo
    def setNumero(self, novoNumero):
        self.numero = novoNumero
    def creditar(self,valor):
        self.saldo+=valor
    def debitar(self,valor):
        self.saldo-=valor
    def getNumero(self):
        return self.numero
    def getSaldo(self):
        return self.saldo
    def transferir(self, valor, contaDst):
        self.debitar(valor)
        contaDst.creditar(valor)
    def __str__(self):
        return f'Número = {self.numero}\nSaldo = {self.saldo}\n'
    @staticmethod
    def validaSaldo(valor):
        return valor >= 0
    @classmethod
    def validaNumero(cls):
        return  cls.proximaConta<100
