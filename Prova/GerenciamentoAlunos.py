import tkinter as tk
from tkinter import messagebox, simpledialog

class StudentManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Alunos UFPI")
        self.students = {}

        self.create_welcome_page()

    def create_welcome_page(self):
        self.clear_frame()

        # Mensagem de boas-vindas centralizada
        mensagem_boas_vindas = "Bem-Vindo ao Gerenciador de Matrícula para prova de Programação 2"
        self.lbl_boas_vindas = tk.Label(self.root, text=mensagem_boas_vindas, font=("Helvetica", 14), wraplength=400, justify="center")
        self.lbl_boas_vindas.grid(row=0, column=0, pady=50)

        # Botões Inserir, Consultar, Alterar, Excluir
        btn_texts = ["Inserir Aluno", "Consultar Aluno", "Alterar Aluno", "Excluir Aluno"]
        btn_commands = [self.create_insert_page, self.create_consult_page, self.create_alter_page, self.create_delete_page]

        for idx, (text, command) in enumerate(zip(btn_texts, btn_commands), start=1):
            btn = tk.Button(self.root, text=text, command=command, bg="gray", fg="white")
            btn.grid(row=idx, column=0, pady=10, sticky="ew")

    def create_insert_page(self):
        self.clear_frame()

        # Título Centralizado
        self.lbl_titulo = tk.Label(self.root, text="Inserir Novo Aluno", font=("Helvetica", 16))
        self.lbl_titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Matrícula
        self.lbl_matricula = tk.Label(self.root, text="Matrícula do Aluno:")
        self.lbl_matricula.grid(row=1, column=0, sticky="w")
        self.entry_matricula = tk.Entry(self.root)
        self.entry_matricula.grid(row=1, column=1, sticky="ew")

        # Nome
        self.lbl_nome = tk.Label(self.root, text="Nome do Aluno:")
        self.lbl_nome.grid(row=2, column=0, sticky="w")
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.grid(row=2, column=1, sticky="ew")

        # Celular
        self.lbl_celular = tk.Label(self.root, text="Celular do Aluno:")
        self.lbl_celular.grid(row=3, column=0, sticky="w")
        self.entry_celular = tk.Entry(self.root)
        self.entry_celular.grid(row=3, column=1, sticky="ew")

        # WhatsApp
        self.lbl_whatsapp = tk.Label(self.root, text="Possui WhatsApp?")
        self.lbl_whatsapp.grid(row=4, column=0, sticky="w")
        self.var_whatsapp = tk.StringVar()
        self.var_whatsapp.set("não")
        self.check_whatsapp = tk.Checkbutton(self.root, text="Sim", variable=self.var_whatsapp, onvalue="sim", offvalue="não")
        self.check_whatsapp.grid(row=4, column=1, sticky="w")

        # E-mail
        self.lbl_email = tk.Label(self.root, text="E-mail Institucional:")
        self.lbl_email.grid(row=5, column=0, sticky="w")
        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=5, column=1, sticky="ew")

        # Botão Inserir
        self.btn_inserir_aluno = tk.Button(self.root, text="Inserir", command=self.inserir_aluno)
        self.btn_inserir_aluno.grid(row=6, column=0, columnspan=2, pady=10)

        # Botão Voltar para a Página Inicial com cor cinza escuro
        self.btn_voltar = tk.Button(self.root, text="Voltar para a Página Inicial", command=self.create_welcome_page, bg="gray", fg="white")
        self.btn_voltar.grid(row=7, column=0, columnspan=2, pady=10, sticky="ew")

        # Configuração das colunas e linhas para expandir
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def create_consult_page(self):
        self.clear_frame()

        # Título Centralizado
        self.lbl_titulo = tk.Label(self.root, text="Consultar Aluno", font=("Helvetica", 16))
        self.lbl_titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Matrícula para Consulta
        self.lbl_consultar = tk.Label(self.root, text="Matrícula do Aluno:")
        self.lbl_consultar.grid(row=1, column=0, sticky="w")
        self.entry_consultar = tk.Entry(self.root)
        self.entry_consultar.grid(row=1, column=1, sticky="ew")

        # Botão Consultar
        self.btn_consultar_aluno = tk.Button(self.root, text="Consultar", command=self.consultar_aluno)
        self.btn_consultar_aluno.grid(row=2, column=0, columnspan=2, pady=10)

        # Resultado da Consulta
        self.lbl_resultado = tk.Label(self.root, text="", justify="left")
        self.lbl_resultado.grid(row=3, column=0, columnspan=2, pady=10)

        # Botão Voltar para a Página Inicial com cor cinza escuro
        self.btn_voltar = tk.Button(self.root, text="Voltar para a Página Inicial", command=self.create_welcome_page, bg="gray", fg="white")
        self.btn_voltar.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

        # Configuração das colunas e linhas para expandir
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def create_alter_page(self):
        self.clear_frame()

        # Título Centralizado
        self.lbl_titulo = tk.Label(self.root, text="Alterar Aluno", font=("Helvetica", 16))
        self.lbl_titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Matrícula para Alteração
        self.lbl_alterar = tk.Label(self.root, text="Matrícula do Aluno:")
        self.lbl_alterar.grid(row=1, column=0, sticky="w")
        self.entry_alterar = tk.Entry(self.root)
        self.entry_alterar.grid(row=1, column=1, sticky="ew")

        # Botão Alterar
        self.btn_alterar_aluno = tk.Button(self.root, text="Alterar", command=self.alterar_aluno_page)
        self.btn_alterar_aluno.grid(row=2, column=0, columnspan=2, pady=10)

        # Botão Voltar para a Página Inicial com cor cinza escuro
        self.btn_voltar = tk.Button(self.root, text="Voltar para a Página Inicial", command=self.create_welcome_page, bg="gray", fg="white")
        self.btn_voltar.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        # Configuração das colunas e linhas para expandir
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def create_delete_page(self):
        self.clear_frame()

        # Título Centralizado
        self.lbl_titulo = tk.Label(self.root, text="Excluir Aluno", font=("Helvetica", 16))
        self.lbl_titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Matrícula para Exclusão
        self.lbl_excluir = tk.Label(self.root, text="Matrícula do Aluno:")
        self.lbl_excluir.grid(row=1, column=0, sticky="w")
        self.entry_excluir = tk.Entry(self.root)
        self.entry_excluir.grid(row=1, column=1, sticky="ew")

        # Botão Excluir
        self.btn_excluir_aluno = tk.Button(self.root, text="Excluir", command=self.excluir_aluno)
        self.btn_excluir_aluno.grid(row=2, column=0, columnspan=2, pady=10)

        # Botão Voltar para a Página Inicial com cor cinza escuro
        self.btn_voltar = tk.Button(self.root, text="Voltar para a Página Inicial", command=self.create_welcome_page, bg="gray", fg="white")
        self.btn_voltar.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        # Configuração das colunas e linhas para expandir
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def inserir_aluno(self):
        matricula = self.entry_matricula.get().strip()
        nome = self.entry_nome.get().strip()
        celular = self.entry_celular.get().strip()
        whatsapp = self.var_whatsapp.get()
        email = self.entry_email.get().strip()

        if matricula == "" or nome == "" or email == "":
            messagebox.showerror("Erro", "Matrícula, Nome e E-mail são campos obrigatórios.")
            return

        if matricula in self.students:
            messagebox.showerror("Erro", f"Já existe um aluno cadastrado com a matrícula {matricula}.")
        else:
            self.students[matricula] = {
                "nome": nome,
                "celular": celular,
                "whatsapp": whatsapp,
                "email": email
            }
            messagebox.showinfo("Sucesso", "Aluno inserido com sucesso.")
            self.create_welcome_page()

    def consultar_aluno(self):
        matricula_consultar = self.entry_consultar.get().strip()

        if matricula_consultar in self.students:
            aluno = self.students[matricula_consultar]
            resultado = f"Matrícula: {matricula_consultar}\n"
            resultado += f"Nome: {aluno['nome']}\n"
            resultado += f"Celular: {aluno['celular']}\n"
            resultado += f"WhatsApp: {aluno['whatsapp']}\n"
            resultado += f"E-mail: {aluno['email']}"

            self.lbl_resultado.config(text=resultado)
        else:
            messagebox.showerror("Erro", f"Aluno com matrícula {matricula_consultar} não encontrado.")

    def alterar_aluno_page(self):
        matricula = self.entry_alterar.get().strip()

        if matricula in self.students:
            aluno = self.students[matricula]
            resultado = f"Matrícula: {matricula}\n"
            resultado += f"Nome: {aluno['nome']}\n"
            resultado += f"Celular: {aluno['celular']}\n"
            resultado += f"WhatsApp: {aluno['whatsapp']}\n"
            resultado += f"E-mail: {aluno['email']}"

            self.clear_frame()

            self.lbl_titulo = tk.Label(self.root, text="Alterar Aluno", font=("Helvetica", 16))
            self.lbl_titulo.grid(row=0, column=0, columnspan=2, pady=10)

            self.lbl_dados_aluno = tk.Label(self.root, text=resultado, justify="left")
            self.lbl_dados_aluno.grid(row=1, column=0, columnspan=2, pady=10)

            self.lbl_alterar = tk.Label(self.root, text="O que deseja alterar?")
            self.lbl_alterar.grid(row=2, column=0, sticky="w")

            opcoes_alterar = ["Nome", "Celular", "WhatsApp", "E-mail"]
            self.var_opcao_alterar = tk.StringVar()
            self.var_opcao_alterar.set(opcoes_alterar[0])
            self.optionmenu_alterar = tk.OptionMenu(self.root, self.var_opcao_alterar, *opcoes_alterar)
            self.optionmenu_alterar.grid(row=2, column=1, sticky="ew")

            self.btn_confirmar_alteracao = tk.Button(self.root, text="Confirmar Alteração", command=lambda: self.confirmar_alteracao(matricula))
            self.btn_confirmar_alteracao.grid(row=3, column=0, columnspan=2, pady=10)

            self.btn_voltar = tk.Button(self.root, text="Voltar para a Página Inicial", command=self.create_welcome_page, bg="gray", fg="white")
            self.btn_voltar.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

            self.root.grid_rowconfigure(0, weight=1)
            self.root.grid_columnconfigure(0, weight=1)
        else:
            messagebox.showerror("Erro", f"Aluno com matrícula {matricula} não encontrado.")

    def confirmar_alteracao(self, matricula):
        opcao_alterar = self.var_opcao_alterar.get()
        novo_valor = None

        if opcao_alterar == "Nome":
            novo_valor = tk.simpledialog.askstring("Alterar Nome", "Novo Nome:")
        elif opcao_alterar == "Celular":
            novo_valor = tk.simpledialog.askstring("Alterar Celular", "Novo Celular:")
        elif opcao_alterar == "WhatsApp":
            novo_valor = tk.simpledialog.askstring("Alterar WhatsApp", "Possui WhatsApp? (Sim ou Não):")
        elif opcao_alterar == "E-mail":
            novo_valor = tk.simpledialog.askstring("Alterar E-mail", "Novo E-mail:")

        if novo_valor is not None:
            self.students[matricula][opcao_alterar.lower()] = novo_valor
            messagebox.showinfo("Sucesso", "Alteração realizada com sucesso.")
            self.create_welcome_page()

    def excluir_aluno(self):
        matricula = self.entry_excluir.get().strip()

        if matricula in self.students:
            confirmacao = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir o aluno com matrícula {matricula}?")
            if confirmacao:
                del self.students[matricula]
                messagebox.showinfo("Sucesso", "Aluno excluído com sucesso.")
                self.create_welcome_page()
        else:
            messagebox.showerror("Erro", f"Aluno com matrícula {matricula} não encontrado.")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()

# Inicialização da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManager(root)
    app.run()
