class Aluno:
    #atributos estáticos, acessados via Classe
    PROVA1=0
    PROVA2=1
    TRABALHO=2
    def __init__(self,matricula,nome,n1=0.0,n2=0.0,n3=0.0):
        self.matricula=matricula
        self.nome=nome
        self.notas=[n1,n2,n3]
    
    def setNota(self,avalicao,nota):
        self.notas[avalicao]=nota

    def media(self):
        soma=self.notas[0] * 2.5 + self.notas[1] * 2.5 + self.notas[2] * 2.0
        return soma / 7.0
    
    def final(self):
        media_aluno = self.media()
        if media_aluno < 7.0:
            nota_p_final = 12.0-media_aluno
            return nota_p_final
        else:
            return 0
    
    #transforma o objeto em string
    def __str__(self) -> str:
        texto=f'''Nome:{self.nome}
        nota 1={self.notas[0]:.2f}
        nota 2={self.notas[1]:.2f}
        trabalho={self.notas[2]:.2f}
        média={self.media():.2f}
        Nota mínima na final = {self.final():.2f}        
        '''
        return texto
    
