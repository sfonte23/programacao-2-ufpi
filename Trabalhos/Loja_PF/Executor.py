from Item import Item
from Fatura import Fatura

class Executor:  # 6
    def __init__(self):
        pass

    # Inclusão de itens na fatura
    def executar(self):
        item1 = Item("Laptop ultrafino i7 16GB RAM 512GB SSD.", 1)
        item2 = Item("Monitor curvo 27' 4K 144Hz HDR", 3100.00)
        item3 = Item("Armazenamento em nuvem pessoal 2TB", 645.00)

        fatura = Fatura("Cobrança_001", "Fatura dos Produtos")
        fatura.adicionar_item(item1)
        fatura.adicionar_item(item2)
        fatura.adicionar_item(item3)
        max_len_descricao = max(len(item.descricao) for item in fatura.itens)+5 #Função só para deixar com o mesmo espaçamento os itens

        #impressão em tela de fatura
        print(fatura.codigo, '-',fatura.descricao)
        print("")
        print("Itens da fatura".center(75))
        print('-~-'*25)
        print(f'{"Descrição":<{max_len_descricao}} {"Valor":>15}')
        print('-~-'*25)
        for item in fatura.itens:
            print((f"{item.descricao.ljust(max_len_descricao)} R$ {item.valor:>15.2f}").replace(".",",").replace("_","."))
        print('-~-'*25)
        print("")
        print((f'Total: R$ {fatura.gettotalfatura():.2f}').replace(".",",").replace("_","."))  # 7