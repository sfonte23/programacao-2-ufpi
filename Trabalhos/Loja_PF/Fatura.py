class Fatura:  # 2
    def __init__(self, codigo, descricao):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__itens = []

    def adicionar_item(self, item):
        self.__itens.append(item)

    def remover_item(self, item):
        self.__itens.remove(item)

     # Totalização da fatura
    def gettotalfatura(self):  # 4
        total = 0
        for item in self.__itens:
            total += item.valor
        return total
    
    @property  # 3
    def codigo(self):
        return self.__codigo

    @codigo.setter  # 3
    def codigo(self, codigo):
        self.__codigo = codigo

    @property  # 3
    def descricao(self):
        return self.__descricao

    @descricao.setter  # 3
    def descricao(self, descricao):
        self.__descricao = descricao

    @property  # 3
    def itens(self):
        return self.__itens