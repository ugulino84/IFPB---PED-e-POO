from fila import Fila

def main():
    #variáveis
    duracaoteste = int(input('Duração do teste (em minutos): '))
    duracaoteste = duracaoteste*60
    tempoadicionar = 0
    tempodecorrido = 0
    totalclientesatendidos = 0
    temponafila = 0
    minuto = 0
    caixas = [0, 0, 0, 0, 0]

    #Filas
    fila1 = Fila()
    fila2 = Fila()
    fila3 = Fila()
    fila4 = Fila()
    fila5 = Fila()



    print('\n-----Tempo Médio de Atendimento (30 a 60s) ----- ')
    tempodeatendimento = []
    for i in range(5):
        tempodeatendimento.append(int(input(f'Caixa {i+1} (em seg): ')))

    print('\n----- Fluxo de Clientes -----')
    fluxocliente = int(input('Quantos clientes serão adicionados as filas por minuto (4-16): '))
    fluxocliente = 60/fluxocliente

    for i in range(duracaoteste):
        tempodecorrido += 1
        tamanhofilas = [fila1.tamanhoFila(), fila2.tamanhoFila(), fila3.tamanhoFila(), fila4.tamanhoFila(),
                        fila5.tamanhoFila()]
        # Retirar cliente atendido e liberar caixa

        for j in range(5):
            if tempodecorrido%tempodeatendimento[j] == 0:
                caixas[j] = 0

        #adicionar clientes na fila
        tempoadicionar += 1
        if tempoadicionar >= fluxocliente:
            posicaoadicionar = tamanhofilas.index(min(tamanhofilas))
            if posicaoadicionar == 0:
                fila1.inserirDado(tempodecorrido)
            elif posicaoadicionar == 1:
                fila2.inserirDado(tempodecorrido)
            elif posicaoadicionar == 2:
                fila3.inserirDado(tempodecorrido)
            elif posicaoadicionar == 3:
                fila4.inserirDado(tempodecorrido)
            else:
                fila5.inserirDado(tempodecorrido)
            tempoadicionar = 0

        #enviando clientes para os caixas vagos

        if caixas[0] == 0 and fila1.tamanhoFila() != 0:
            caixas[0] = fila1.primeirodafila()
            temponafila += (tempodecorrido - caixas[0])
            totalclientesatendidos+=1
            fila1.removerDado()
        if caixas[1] == 0 and fila2.tamanhoFila() != 0:
            caixas[1] = fila2.primeirodafila()
            temponafila += (tempodecorrido - caixas[1])
            totalclientesatendidos += 1
            fila2.removerDado()
        if caixas[2] == 0 and fila3.tamanhoFila() != 0:
            caixas[2] = fila3.primeirodafila()
            temponafila += (tempodecorrido - caixas[2])
            totalclientesatendidos += 1
            fila3.removerDado()
        if caixas[3] == 0 and fila4.tamanhoFila() != 0:
            caixas[3] = fila4.primeirodafila()
            temponafila += (tempodecorrido - caixas[3])
            totalclientesatendidos += 1
            fila4.removerDado()
        if caixas[4] == 0 and fila5.tamanhoFila() != 0:
            caixas[4] = fila5.primeirodafila()
            temponafila += (tempodecorrido - caixas[4])
            totalclientesatendidos += 1
            fila5.removerDado()

        #informação por minuto ao cliente
        if tempodecorrido%60 == 0:
            minuto+=1
            print(f'\n--------Minuto {minuto}--------\n')
            for k in range(5):
                if caixas[k] != 0:
                    print(f'Caixa {k+1}: \n\n01 Cliente em atendiemnto\n{tamanhofilas[k]} esperando na fila\n')
                else:
                    print(f'Caixa {k+1}: \n\n00 Cliente em atendiemnto\n{tamanhofilas[k]} esperando na fila\n')

    #calculando tempo médio de espera na fila

    totalclientes = duracaoteste / fluxocliente

    lista1 = fila1.getFila()
    lista2 = fila2.getFila()
    lista3 = fila3.getFila()
    lista4 = fila4.getFila()
    lista5 = fila5.getFila()

    #adicionando o tempo de espera dos clientes que ainda aguardam na fila
    for i in range(len(lista1)):
        temponafila+=(tempodecorrido-lista1[i])
    for i in range(len(lista2)):
        temponafila+=(tempodecorrido-lista1[i])
    for i in range(len(lista3)):
        temponafila+=(tempodecorrido-lista1[i])
    for i in range(len(lista4)):
        temponafila+=(tempodecorrido-lista1[i])
    for i in range(len(lista5)):
        temponafila+=(tempodecorrido-lista1[i])

    print(f'Tempo médio de espera (aproximado) = {round((temponafila / totalclientes) / 60, 2)} minutos')

main()





