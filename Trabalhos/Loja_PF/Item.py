class Item:  # 1
    def __init__(self, descricao, valor):
        self.__descricao = descricao 
        if valor > 0:
            self.__valor = valor # 5
        else:
            raise ValueError("O valor do item deve ser maior que zero.")

    @property  # 3
    def descricao(self):
        return self.__descricao

    @descricao.setter  # 3
    def descricao(self, descricao):
        self.__descricao = descricao

    @property  # 3
    def valor(self):
        return self.__valor