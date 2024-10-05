class Voo:
    proxLivre=1 #atributo estatico, pertence à Classe inteira, todos os
    #objetos da Classe podem acessar (para esse exemplo é inútil)
    def __init__(self,numero,data):
        self.ocupados=[]
        self.numero=numero
        self.data=data
    
    @classmethod #método da classe acessa a variável da classe
    def proximoLivre(cls): # para esse exemplo é inútil
        return cls.proxLivre
    
    def verifica(self,nCadeira):
        return nCadeira in self.ocupados
    
    def ocupa(self,nCadeira):
        if self.vagas()>0: #se ainda tem vaga disponível
            estaOcupado = self.verifica(nCadeira)
            if not estaOcupado:
                self.ocupados.append(nCadeira)
                return True
            else:
                return False
        else:
            return False

    def vagas(self):
        return 100-len(self.ocupados)
    
    def getVoo(self):
        return self.numero

    def getData(self):
        return self.data

    def clone(self):
        data=self.getData().clone()
        num=self.numero
        novo=Voo(num,data)
        novo.ocupados=self.ocupados[:]
        return novo
    
    def __str__(self) -> str:
        texto=f'\nVoo n° = {self.numero}\n'+\
        f'Data = {self.data}\n'+\
        f'Cadeiras ocupadas = {self.ocupados}\n'
        return texto
