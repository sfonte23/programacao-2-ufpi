from moduloEscola import Aluno

if __name__ == '__main__':
    aluno1 = Aluno('Waldisney',2023001)
    print(f'Nome = {aluno1.getNome()} Matrícula = {aluno1.getMatricula()}')
    aluno1.setNome('Waldisnei')
    print(f'Nome = {aluno1.getNome()} Matrícula = {aluno1.getMatricula()}')
    print(f'Nome Antigo = {aluno1.getNomeAntigo()} nome novo = {aluno1.getNome()}')


