
class Impressao:

    def visitar_soma(self, soma):
        print("(", end='')
        soma.expressao_esquerda.aceita(self)
        print('+', end='')
        soma.expressao_direita.aceita(self)
        print(')', end='')
    
    def visitar_subtracao(self, subtracao):
        print("(", end='')
        subtracao.expressao_esquerda.aceita(self)
        print('-', end='')
        subtracao.expressao_direita.aceita(self)
        print(')', end='')

    def visitar_numero(self, numero):
        print(numero.avaliar(), end='')
