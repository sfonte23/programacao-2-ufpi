import tkinter as tk
from tkinter import messagebox

def criar_janela_explicacao(titulo, texto):
    # Função para criar uma nova janela com a explicação
    nova_janela = tk.Toplevel(root)
    nova_janela.title(titulo)
    nova_janela.geometry("400x300")
    
    # Frame para centralizar o conteúdo
    frame = tk.Frame(nova_janela, bg="lightyellow")
    frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    
    # Label com a explicação
    label = tk.Label(frame, text=texto, font=("Arial", 12), bg="lightyellow", wraplength=380, justify="left")
    label.pack(pady=20)

def sobre_tkinter():
    texto = (
        "Tkinter é a biblioteca padrão do Python para a criação de interfaces gráficas (GUI). "
        "Ele permite a criação de janelas, botões, campos de texto, menus e muito mais.\n\n"
        "A janela principal é onde todos os widgets são colocados. Você pode criar novas janelas "
        "usando o widget Toplevel."
    )
    criar_janela_explicacao("Sobre Tkinter", texto)

def sobre_widgets():
    texto = (
        "Widgets são os componentes da interface gráfica, como botões, labels, campos de texto, etc.\n\n"
        "Exemplo de alguns widgets:\n"
        "- Label: exibe texto ou imagens.\n"
        "- Button: executa uma ação quando clicado.\n"
        "- Entry: campo de entrada de texto de linha única.\n"
        "- Text: caixa de texto de múltiplas linhas."
    )
    criar_janela_explicacao("Sobre Widgets", texto)

def sobre_layouts():
    texto = (
        "Tkinter oferece três métodos principais para gerenciar layouts:\n\n"
        "1. pack(): organiza os widgets em blocos antes de colocá-los na janela.\n"
        "2. grid(): organiza widgets em uma grade (linhas e colunas).\n"
        "3. place(): coloca widgets em posições específicas.\n\n"
        "Você pode usar esses métodos para posicionar os widgets na janela de maneira flexível."
    )
    criar_janela_explicacao("Sobre Layouts", texto)

def sobre_eventos():
    texto = (
        "Eventos são ações que ocorrem em resposta a interações do usuário, como cliques de botão ou "
        "movimentos do mouse.\n\n"
        "Você pode usar eventos para executar funções específicas quando uma ação é realizada.\n"
        "Exemplo: command=função para botões, bind(evento, função) para eventos específicos."
    )
    criar_janela_explicacao("Sobre Eventos", texto)

# Criando a janela principal
root = tk.Tk()
root.title("Guia Tkinter")
root.geometry("500x400")

# Criando a barra de menus
menubar = tk.Menu(root)

# Criando o menu "Ajuda"
menu_ajuda = tk.Menu(menubar, tearoff=0)
menu_ajuda.add_command(label="Sobre Tkinter", command=sobre_tkinter)
menu_ajuda.add_command(label="Widgets", command=sobre_widgets)
menu_ajuda.add_command(label="Layouts", command=sobre_layouts)
menu_ajuda.add_command(label="Eventos", command=sobre_eventos)

# Adicionando o menu "Ajuda" à barra de menus
menubar.add_cascade(label="Ajuda", menu=menu_ajuda)

# Configurando a barra de menus na janela principal
root.config(menu=menubar)

# Label de boas-vindas na janela principal
label_boas_vindas = tk.Label(root, text="Bem-vindo ao Guia Tkinter!", font=("Arial", 16, "bold"), fg="blue")
label_boas_vindas.pack(pady=20)

# Mensagem inicial
mensagem_inicial = (
    "Use o menu 'Ajuda' para aprender mais sobre Tkinter.\n\n"
    "Clique em uma das opções para abrir uma nova janela com informações detalhadas."
)
label_mensagem = tk.Label(root, text=mensagem_inicial, font=("Arial", 12), justify="left", wraplength=480)
label_mensagem.pack(pady=10)

root.mainloop()
