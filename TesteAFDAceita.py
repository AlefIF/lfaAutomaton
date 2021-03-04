from AutomatoFD import AutomatoFD

def TesteAFDAceita():

    afd = AutomatoFD('ab')

    for i in range(1,5):
        afd.criaEstado(i)
    afd.mudaEstadoInicial(1)
    afd.mudaEstadoFinal(4, True)

    afd.criaTransicao(1, 2, 'a')
    afd.criaTransicao(2, 1, 'a')
    afd.criaTransicao(3, 4, 'a')
    afd.criaTransicao(4, 3, 'a')
    afd.criaTransicao(1, 3, 'b')
    afd.criaTransicao(3, 1, 'b')
    afd.criaTransicao(2, 4, 'b')
    afd.criaTransicao(4, 2, 'b')

    print(afd)
    cadeia = 'abbabaabbbbbba'
    afd.limpaAfd()
    parada = afd.move(cadeia)
    if not afd.deuErro() and afd.estadoFinal(parada):
        print('Aceita cadeia "{}"'.format(cadeia))
    else:
        print('Rejeita cadeia "{}"'.format(cadeia))


