class Aluno:
    def __init__(self, nome, matricula):
        self.nome=nome
        self.matricula=matricula
    def setNome(self, novoNome):
        self.nome = novoNome
    def setMatricula(self, novaMatricula):
        self.matricula = novaMatricula
    def getNome(self):
        return self.nome
    def getMatricula(self):
        return self.matricula


