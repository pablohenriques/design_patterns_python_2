
class Subtracao:

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita
    
    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita

    def avaliar(self):
        return self.__expressao_esquerda.avaliar() - self.__expressao_direita.avaliar()

    def aceita(self, visitor):
        visitor.visitar_subtracao(self)
        

class Soma:
    
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita
    
    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita
    
    def avaliar(self):
        return self.__expressao_esquerda.avaliar() + self.__expressao_direita.avaliar()

    def aceita(self, visitor):
        visitor.visitar_soma(self)


class Numero:

    def __init__(self, numero):
        self.__numero = numero

    def avaliar(self):
        return self.__numero

    def aceita(self, visitor):
        visitor.visitar_numero(self)


if __name__ == "__main__":
    from impressao import Impressao

    impressao = Impressao()

    expressao_esquerda = Soma(Numero(10), Numero(20))
    expressao_direita = Soma(Numero(10), Numero(20))
    expressao_conta = Soma(expressao_direita, expressao_esquerda)
    #print(expressao_conta.avaliar())
    print("\n")
    expressao_conta.aceita(impressao)
    print("\n")
    #expressao_conta2 = Subtracao(Numero(100), Numero(70))
    #print(expressao_conta2.avaliar())

    expressao_esquerda = Subtracao(Numero(100), Numero(20))
    expressao_direita = Soma(Numero(5), Numero(5))
    expressao_conta = Soma(expressao_direita, expressao_esquerda)
    print("\n")
    expressao_conta.aceita(impressao)
    print("\n")
    