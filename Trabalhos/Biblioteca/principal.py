# Importando as classes
from modulo import Aluno, Livro, Biblioteca

# Criando instâncias de livros
livro1 = Livro("A Culpa é das Estrelas", "John Green", 304, 1)
livro2 = Livro("O Hobbit", "J.R.R. Tolkien", 368, 1)
livro3 = Livro("Percy Jackson e o Ladrão de Raios", "Rick Riordan", 400, 1)
livro4 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 332, 1)
livro5 = Livro("A Menina que Roubava Livros", "Markus Zusak", 480, 1)
livro6 = 'teste'

# Criando instâncias de alunos
aluno1 = Aluno("Maria", "2021001", "Engenharia Civil")
aluno2 = Aluno("José", "2021002", "Ciência da Computação")
aluno3 = Aluno("Ana", "2021003", "Medicina")
aluno4 = Aluno("Pedro", "2021004", "Administração")
aluno5 = Aluno("Luciana", "2021005", "Direito")
aluno6 = 'teste2'

# Cadastrando os livros e alunos na biblioteca
biblioteca = Biblioteca()
biblioteca.cadastra_livro(livro1)
biblioteca.cadastra_livro(livro2)
biblioteca.cadastra_livro(livro3)
biblioteca.cadastra_livro(livro4)
biblioteca.cadastra_livro(livro5)
#forçando erro
biblioteca.cadastra_livro(livro6)

biblioteca.cadastra_aluno(aluno1)
biblioteca.cadastra_aluno(aluno2)
biblioteca.cadastra_aluno(aluno3)
biblioteca.cadastra_aluno(aluno4)
biblioteca.cadastra_aluno(aluno5)
#forçando erro
biblioteca.cadastra_aluno(aluno6)

# Simulação de empréstimo de livros
biblioteca.empresta_livro(livro1, aluno1)
biblioteca.empresta_livro(livro3, aluno2)

# Simulação de empréstimo de livro indisponível
biblioteca.empresta_livro(livro3, aluno3)
biblioteca.empresta_livro(livro1, aluno2)

# Simulação de devolução de livro
biblioteca.devolve_livro(aluno1, livro1)

#Ver empréstimos
biblioteca.listar_livros_aluno(aluno3)