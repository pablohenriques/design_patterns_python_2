from datetime import date


class Contrato:

    def __init__(self, data, cliente, tipo):
        self.__data = data
        self.__cliente = cliente
        self.__tipo = tipo

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
    
    def avancar(self):
        if self.__tipo == "NOVO":
            self.__tipo = "EM ANDAMENTO"
        elif self.__tipo == "EM ANDAMENTO":
            self.__tipo = "ACERTADO"
        elif self.__tipo == "ACERTADO":
            self.__tipo = "CONCLUIDO"

    def salvar_estado(self):
        return Estado(
            Contrato(
                data=self.__data, 
                cliente=self.__cliente, 
                tipo=self.__tipo
            )
        )

    def restaurar_estado(self, estado):
        self.__cliente = estado.contrato.cliente
        self.__data = estado.contrato.data
        self.__tipo = estado.contrato.tipo
        return None

class Estado:

    def __init__(self, contrato):
        self.__contrato = contrato
    
    @property
    def contrato(self):
        return self.__contrato

class Historico:

    def __init__(self):
        self.__estados_salvos = []
    
    def obter_estado(self, indice):
        return self.__estados_salvos[indice]
    
    def adicionar_estado(self, estado):
        self.__estados_salvos.append(estado)


if __name__ == "__main__":
    h = Historico()
    c = Contrato(data=date.today(), cliente="Sousa", tipo="NOVO")
    
    c.avancar()
    h.adicionar_estado(c.salvar_estado())

    c.avancar()
    c.cliente = "Henrique"
    h.adicionar_estado(c.salvar_estado())

    c.avancar()
    h.adicionar_estado(c.salvar_estado())

    print(c.tipo)
    print(c.cliente)

    c.restaurar_estado(h.obter_estado(0))
    
    print(c.tipo)
    print(c.cliente)
