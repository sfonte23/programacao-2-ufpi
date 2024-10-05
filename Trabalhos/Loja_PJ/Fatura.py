class Fatura:
    def __init__(self, codigo, descricao):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__itens = []

    def adicionar_item(self, item):
        self.__itens.append(item)

    def remover_item(self, item):
        self.__itens.remove(item)

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def itens(self):
        return self.__itens

    def get_total_fatura(self):
        total = 0
        for item in self.__itens:
            total += item.valor
        return total 