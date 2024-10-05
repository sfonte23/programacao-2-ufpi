class Data:
    def __init__(self,strData) -> None:
        totalDeDias=[31,28,31,30,31,30,31,31,30,31,30,31]
        try:
            partes=strData.split('/')
            self.dia=int(partes[0])
            self.mes=int(partes[1])
            self.ano=int(partes[2])
            if self.isBissexto():
                 totalDeDias[1]=29 # fevereiro terá 29 dias
        except:
             self.__erro()
        if self.dia<1 or self.dia > totalDeDias[self.mes-1]: self.__erro()
        if self.mes<1 or self.mes > 12: self.__erro()
        if self.ano <1 : self.__erro()

    def __erro(self): #método usado APENAS dentro da classe, por isso o "__" 
            self.dia=1
            self.mes=1
            self.ano=1
    
    def isBissexto(self):
         return  self.ano%4==0

    def compara(self, data):
         if str(self)==str(data): return 0 #dia, mês e ano iguais
         #daqui pra frente as datas são obrigatoriamente diferentes 
         #testa-se inicialmente o ano 
         if self.ano!=data.ano:
               return 1 if self.ano>data.ano else -1 
        #daqui pra frente os anos são iguais, testa-se o mês
         if self.mes!=data.mes:
               return 1 if self.mes>data.mes else -1 
        #se chegou nesse ponto significa q ano e mês são iguas, falta o dia, que obrigatoriamente são diferentes
         return 1 if self.dia>data.dia else -1 

    def getDia(self):
         return self.dia     

    def getMes(self):
         return self.mes     

    def getAno(self):
         return self.ano     

    def getMesExtenso(self):
         meses={'1':'janeiro','2':'fevereiro',\
                '3':'março','4':'abril','5':'maio',\
                '6':'junho','7':'junho','8':'agosto',\
                '9':'setembro','10':'outubro',\
                '11':'novembro','12':'dezembro'}
         mesTxt=str(self.mes) 
         return f'{self.dia} de {meses[mesTxt]} de {self.ano}'     

    #transforma o objeto em string
    def __str__(self) -> str: 
         return f'{self.dia:02d}/{self.mes:02d}/{self.ano:04d}'

    def clone(self):
          #cria um novo objeto com os mesmos dados, porém em áreas de memórias diferentes
          #Lembre-se:
          #   clone: o que acontece com um não acontece com o outro
          #   apelido: o que acontece com um obrigatoriamente acontece com o outro
         return Data(str(self))