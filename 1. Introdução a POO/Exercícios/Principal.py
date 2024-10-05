from ModuloAluno import Aluno
from ModuloData import Data
from ModuloVoo import Voo

class Aula02:

    @staticmethod  #m.estático não precisa criar um objeto, usa direto da Classe
    def questao1():
        a1=Aluno(2023001,'Exclebeuton Silveira')
        a1.setNota(Aluno.PROVA1,10.0)
        a1.setNota(Aluno.PROVA2,9.0)
        a1.setNota(Aluno.TRABALHO,8.0)
        a2=Aluno(2023002,'Franciscória Augustina',5.0,5.0,6.0)
        print(a1)
        print(a2)

    @staticmethod
    def questao2():
        d1 = Data('28/02/2024') #erro fevereiro
        d2 = Data('28/02/2024') #erro fevereiro
        print(d1)
        print(d1.compara(d2))
        print(d1.getMesExtenso())
        d3=d1.clone()
        print(d1)
        print(d3)
        print(id(d1))
        print(id(d3))
    
    def questao3():
        v1 = Voo(1,Data('17/03/2024'))
        nCadeira = Voo.proximoLivre()
        
        if v1.ocupa(nCadeira):
            print(f'Cadeira {nCadeira} ocupada com sucesso!')
        else:
            print(f'Cadeira {nCadeira} está ocupada!')
        print(f'{v1.vagas()} cadeiras vagas.\n')

        if v1.ocupa(nCadeira):
            print(f'Cadeira {nCadeira} ocupada com sucesso!')
        else:
            print(f'Cadeira {nCadeira} está ocupada!')
        print(f'{v1.vagas()} cadeiras vagas.\n')
        
        nCadeira=20
        if v1.ocupa(nCadeira):
            print(f'Cadeira {nCadeira} ocupada com sucesso!')
        else:
            print(f'Cadeira {nCadeira} está ocupada!')
        print(f'{v1.vagas()} cadeiras vagas.\n')

        print(v1)



if __name__=='__main__':
    #Aula02.questao1()  #m.estático não precisa criar um objeto, usa direto da Classe
    #Aula02.questao2()
    Aula02.questao3()