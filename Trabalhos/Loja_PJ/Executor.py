from Fatura_PJ import FaturaPessoaJuridica
from Fatura_PF import FaturaPessoaFisica
from Item import Item

class Executor2:
    def __init__(self):
        pass

    def executar(self):
        while True:
            tipo = input('Qual o tipo de fatura? PF - Pessoa Física  ou PJ - Pessoa Jurídica? ').upper()
            if tipo in ('PF', 'PJ'):
                break
            else:
                print("Por favor, insira 'PF' para Pessoa Física ou 'PJ' para Pessoa Jurídica.")

        item1 = Item("Laptop ultrafino i7 16GB RAM 512GB SSD.", 3000.00)
        item2 = Item("Monitor curvo 27' 4K 144Hz HDR", 3100.00)
        item3 = Item("Armazenamento em nuvem pessoal 2TB", 645.00)

        print('') # pulando uma linha para ficar um visual melhor

        if tipo == 'PF':
            fatura_pf = FaturaPessoaFisica("Cobrança_001_PF", "Fatura dos Produtos - Pessoa Física")
            fatura_pf.adicionar_item(item1)
            fatura_pf.adicionar_item(item2)
            fatura_pf.adicionar_item(item3)
            max_len_descricao_pf = max(len(item.descricao) for item in fatura_pf.itens) + 5

            print("Fatura para Pessoa Física".center(100))
            print('-~-' * 30)
            print((f'{fatura_pf.codigo} - {fatura_pf.descricao} - Itens da fatura').center(100))
            print('-~-' * 30)
            print(f'{"Descrição":<{max_len_descricao_pf}} {"Valor":>15} {"Imposto":>15}')
            print('-~-' * 30)
            for item in fatura_pf.itens:
                imposto = item.valor * 0.05  # 5% de ISS para pessoas físicas
                print((f"{item.descricao.ljust(max_len_descricao_pf)} R$ {item.valor:>15_.2f} R$ {imposto:>15_.2f}").replace(".", ",").replace("_", "."))
            print('-~-' * 30)
            print("")
            total_pf = fatura_pf.get_total_fatura()
            imposto_pf = sum(item.valor * 0.05 for item in fatura_pf.itens)  # Calculando o imposto total corretamente
            print(f'Total: R$ {total_pf:_.2f}'.replace(".", ",").replace("_", ".") + f' | Imposto Total: R$ {imposto_pf:_.2f}'.replace(".", ",").replace("_", "."))

        elif tipo == 'PJ':
            fatura_pj = FaturaPessoaJuridica("Cobrança_001_PJ", "Fatura dos Produtos - Pessoa Jurídica")
            fatura_pj.adicionar_item(item1)
            fatura_pj.adicionar_item(item2)
            fatura_pj.adicionar_item(item3)
            max_len_descricao_pj = max(len(item.descricao) for item in fatura_pj.itens) + 5

            print("\n\nFatura para Pessoa Jurídica".center(100))
            print('-~-' * 30)
            print((f'{fatura_pj.codigo} - {fatura_pj.descricao} - Itens da fatura').center(100))
            print('-~-' * 30)
            print(f'{"Descrição":<{max_len_descricao_pj}} {"Valor":>15} {"Imposto":>15}')
            print('-~-' * 30)
            for item in fatura_pj.itens:
                imposto = item.valor * 0.025  # 2.5% de imposto para pessoas jurídicas
                print((f"{item.descricao.ljust(max_len_descricao_pj)} R$ {item.valor:>15_.2f} R$ {imposto:>15_.2f}").replace(".", ",").replace("_", "."))
            print('-~-' * 30)
            print("")
            total_pj = fatura_pj.get_total_fatura()
            imposto_pj = sum(item.valor * 0.025 for item in fatura_pj.itens)  # Calculando o imposto total corretamente
            print((f'Total: R$ {total_pj:_.2f}').replace(".", ",").replace("_", ".") + f' | Imposto Total: R$ {imposto_pj:_.2f}'.replace(".", ",").replace("_", "."))
        else:
            print('ERRO')        
