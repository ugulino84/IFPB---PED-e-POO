class Fila:

    #construtor
    def __init__(self):
        self.dados = []

    def getFila(self):
        return self.dados

    def inserirDado(self, novoValor):
        self.dados.append(novoValor)

    def removerDado(self):
        self.dados.pop(0)

    def tamanhoFila(self):
        return self.dados.__len__()

    def primeirodafila(self):
        return self.dados[0]