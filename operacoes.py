
class Subtracao:

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avaliar(self):
        return self.__expressao_esquerda.avaliar() - self.__expressao_direita.avaliar()


class Soma:
    
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita
    
    def avaliar(self):
        return self.__expressao_esquerda.avaliar() + self.__expressao_direita.avaliar()


class Numero:

    def __init__(self, numero):
        self.__numero = numero

    def avaliar(self):
        return self.__numero


if __name__ == "__main__":
    expressao_esquerda = Soma(Numero(10), Numero(20))
    expressao_direita = Soma(Numero(10), Numero(20))
    expressao_conta = Soma(expressao_direita, expressao_esquerda)
    print(expressao_conta.avaliar())

    expressao_conta2 = Subtracao(Numero(100), Numero(70))
    print(expressao_conta2.avaliar())
    