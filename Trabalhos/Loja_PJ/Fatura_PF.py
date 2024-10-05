from Fatura import Fatura

class FaturaPessoaFisica(Fatura):
    def __init__(self, codigo, descricao):
        super().__init__(codigo, descricao)

    def get_total_fatura(self):
        imposto = 1.05
        total = super().get_total_fatura()
        return total*imposto
