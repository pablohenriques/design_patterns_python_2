from datetime import date
from abc import ABCMeta, abstractmethod


class Comando:

    __metaclass__ = ABCMeta

    @abstractmethod
    def executar(self):
        pass


class Pedido:

    def __init__(self, cliente, valor):
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def pagar(self):
        self.__status = 'PAGO'

    def finalizar(self):
        self.__data_finalizacao = date.today()
        self.__status = 'ENTREGUE'

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def data_finalizacao(self):
        return self.__data_finalizacao


class ConcluiPedido:

    def __init__(self, pedido):
        self.__pedido = pedido

    def executar(self):
        self.__pedido.finalizar()


class PagaPedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executar(self):
        self.__pedido.pagar()


class FilaDeTrabalho:

    def __init__(self):
        self.__comandos = []

    def adicionar(self, comando):
        self.__comandos.append(comando)

    def processar(self):
        for comando in self.__comandos:
            comando.executar()


if __name__ == "__main__":
    p1 = Pedido('Flavio', 200)
    p2 = Pedido('Almeida', 400)

    ft = FilaDeTrabalho()
    cmd1 = PagaPedido(p1)
    cmd2 = ConcluiPedido(p1)
    cmd3 = ConcluiPedido(p2)
    
    ft.adicionar(cmd1)
    ft.adicionar(cmd2)
    ft.adicionar(cmd3)
    ft.processar()

    print(p1.status)