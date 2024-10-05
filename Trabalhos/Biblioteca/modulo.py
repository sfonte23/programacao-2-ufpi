class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.emprestimos = [] 

class Livro:
    def __init__(self, titulo, autor, paginas, exemplares=1):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.exemplares = exemplares

class Biblioteca:
    universidade = 'UFPI'

    @staticmethod
    def altera_universidade(nova_universidade):
        Biblioteca.universidade = nova_universidade
        print(f"Universidade alterada para: {nova_universidade}")

    @classmethod
    def altera_nome_biblioteca(cls, novo_nome):
        cls.nome_biblioteca = novo_nome
        print(f"Nome da biblioteca alterado para: {novo_nome}")

    def __init__(self, livros=[], alunos=[]):
        self.livros = livros
        self.alunos = alunos
        self.emprestimos = []
        print("Biblioteca inicializada")

    def cadastra_livro(self, livro):
        if not isinstance(livro, Livro):
            print("\033[91mErro: Livro inválido\033[0m")
            return
        self.livros.append(livro)
        print(f"\033[92mLivro '{livro.titulo}' cadastrado na biblioteca\033[0m")

    def cadastra_aluno(self, aluno):
        if not isinstance(aluno, Aluno):
            print("\033[91mErro: Aluno(a) inválido\033[0m")
            return
        self.alunos.append(aluno)
        print(f"\033[92mAluno '{aluno.nome}' cadastrado na biblioteca\033[0m")

    def empresta_livro(self, livro, aluno):
        if not isinstance(livro, Livro) or not isinstance(aluno, Aluno):
            print("\033[91mErro: Livro ou aluno(a) inválido\033[0m")
            return
        if livro.exemplares <= 0:
            print("\033[91mErro: Livro sem exemplares disponíveis\033[0m")
            return
        self.emprestimos.append((aluno, livro))
        livro.exemplares -= 1
        print(f"\033[92mLivro '{livro.titulo}' emprestado para o(a) aluno(a) '{aluno.nome}'\033[0m")

    def devolve_livro(self, aluno, livro):
        if not isinstance(aluno, Aluno) or not isinstance(livro, Livro):
            print("\033[91mErro: Livro ou aluno(a) inválido\033[0m")
            return
        emprestimo = next((e for e in self.emprestimos if e[0] == aluno and e[1] == livro), None)
        if emprestimo is None:
            print("\033[91mErro: Livro não encontrado emprestado a este aluno\033[0m")
            return
        self.emprestimos.remove(emprestimo)
        livro.exemplares += 1
        print(f"\033[92mLivro '{livro.titulo}' devolvido pelo(a) aluno(a) '{aluno.nome}'\033[0m")

    def listar_livros_aluno(self, aluno):
        if not isinstance(aluno, Aluno):
          print("\033[91mErro: Aluno(a) inválido\033[0m")
          return

        livros_emprestados = [l for a, l in self.emprestimos if a == aluno]
        if not livros_emprestados:
          print(f"Sem livros emprestados para {aluno.nome}")
          return

        print(f"Livros emprestados para o aluno(a) '{aluno.nome}':")
        for i, livro in enumerate(livros_emprestados, start=1):
          print(f"{i}. {livro.titulo}")

    def remove_livro(self, livro):
        if not isinstance(livro, Livro):
            print("\033[91mErro: Livro inválido\033[0m")
            return
        self.livros.remove(livro)
        self.emprestimos = [e for e in self.emprestimos if e[1] != livro]
        print(f"\033[92mLivro '{livro.titulo}' removido da biblioteca\033[0m")
