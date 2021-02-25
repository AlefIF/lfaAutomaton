class AutomatoFD:
    def __init__(self, Alfabeto):
        Alfabeto = str(Alfabeto)
        self.estados = set()
        self.alfabeto = Alfabeto
        self.transicoes = dict()
        self.inicial = None
        self.finais = set()

    def limpaAfd(self):
        self.__deuErro = False
        self.__estadoAtual = self.inicial

    def criaEstado(self, id, inicial=False, final=False):
        id = int(id)
        if id in self.estados:
            return False
        self.estados = self.estados.union({id})
        if inicial:
            self.inicial = id
        if final:
            self.finais = self.finais.union({id})
        return True

    def criaTransicao(self, origem, destino, simbolo):
        origem = int(origem)
        destino = int(destino)
        simbolo = str(simbolo)
        if not origem in self.estados:
            return False
        if not destino in self.estados:
            return False
        if len(simbolo) != 1 or not simbolo in self.alfabeto:
            return False
        self.transicoes[(origem, simbolo)] = destino
        return True

    def mudaEstadoInicial(self, id):
        if not id in self.estados:
            return
        self.inicial = id

    def mudaEstadoFinal(self, id, final):
        if not id in self.estados:
            return
        if final:
            self.finais = self.finais.union({id})
        else:
            self.finais = self.finais.difference({id})

    def move(self, cadeia):
        for simbolo in cadeia:
            if not simbolo in self.alfabeto:
                self.__deuErro = True
                break
            if (self.__estadoAtual, simbolo) in self.transicoes.keys():
                novoEstado = self.transicoes[(self.__estadoAtual, simbolo)]
                self.__estadoAtual = novoEstado
            else:
                self.__deuErro = True
                break
        return self.__estadoAtual

    def deuErro(self):
        return self.__deuErro

    def estadoAtual(self):
        return self.__estadoAtual

    def estadoFinal(self, id):
        return id in self.finais

    def __str__(self):
        s = 'AFD(E, A, T, i, F): \n'
        s += '   E = { '
        for e in self.estados:
            s += '{}, '.format(str(e))
        s += '} \n'
        s += '   A = { '
        for a in self.alfabeto:
            s += "'{}', ".format(a)
        s += '} \n'
        s += '   T = { '
        for (e, a) in self.transicoes.keys():
            d = self.transicoes[(e, a)]
            s += "({}, '{}')-->{}, ".format(e, a, d)
        s += '} \n'
        s += '   i = {} \n'.format(self.inicial)
        s += '   F = { '
        for e in self.finais:
            s += '{}, '.format(str(e))
        s += '}'
        return s

def lerAFDtxt():
    print('=================================Calculo de AFD=================================')
    print('Forneca o endereco de um arquivo .txt com a seguinte formatacao das linhas:')
    print('(1) Conter o alfabeto')
    print('(2) Quantidade de estados')
    print('(3) Estado inicial')
    print('(4) Estados finais separados por espaco')
    print('(5 a N) Transicoes')
    print('(N+1) ter o simbolo - para indicar o fim das transicoes ')
    print('(N+2) A cadeia em sequencia e sem espaco ')
    print('====================================Exemplo====================================')
    print('ab')
    print('4')
    print('1')
    print('4')
    print('1 2 a')
    print('2 1 a')
    print('3 4 a')
    print('4 3 a')
    print('1 3 b')
    print('3 1 b')
    print('2 4 b')
    print('4 2 b')
    print('-')
    print('abbabaabbbbbba')
    print('==================================FIM Exemplo==================================')

    #arquivo = "C:/Users/aleff/Desktop/lfa/teste.txt"
    arquivo = input('Digite o caminho do arquivo: ')
    arquivoLeitura = open(arquivo, "r")

    i = 0
    text = ''
    afd = ''
    cadeia = ''

    for linha in arquivoLeitura:
        argumento = linha.split()
        if i == 0:
            for y in argumento:
                text += y
            afd = AutomatoFD(text)
        elif i == 1:
            for x in range(1, int(argumento[0]) + 1):
                afd.criaEstado(x)
        elif i == 2:
            afd.mudaEstadoInicial(int(argumento[0]))
        elif i == 3:
            for y in argumento:
                afd.mudaEstadoFinal(int(y), True)
        elif i >= 4:
            if argumento[0] == '-':
                i = -2
            else:
                afd.criaTransicao(argumento[0], argumento[1], argumento[2])
        elif i == -1:
            text = ''
            for g in argumento:
                text += g
            cadeia = text
        i = i + 1

    arquivoLeitura.close()
    print(afd)
    afd.limpaAfd()
    parada = afd.move(cadeia)
    if not afd.deuErro() and afd.estadoFinal(parada):
        print('Aceita cadeia "{}"'.format(cadeia))
    else:
        print('Rejeita cadeia "{}"'.format(cadeia))

    return 0

def salvarAFDtxt():
    print('=================================Salvar AFD=================================')
    print('Para uma futura leitura do AFD, siga as instrucoes em ()')
    try:
        ADFtext = open(input('Digite o diretorio do arquivo a ser gerado: '), 'w')
    except:
        return -1
    ADFtext.writelines(input('Digite o alfabeto (sem espaco): '))
    ADFtext.writelines('\n')
    ADFtext.writelines(input('Digite a quantidade de estados: '))
    ADFtext.writelines('\n')
    ADFtext.writelines(input('Digite o Estado inicial: '))
    ADFtext.writelines('\n')
    ADFtext.writelines(input('Digite o(s) Estado(s) final(is) (separados por espaco): '))
    ADFtext.writelines('\n')
    x = int(input('Digite a quantidade de transicoes: '))
    print('Digite o estado atual, o estado novo e o simbolo (exemplo: 1 2 a)')
    for i in range(x):
        ADFtext.writelines(input('T'+str(i)+': '))
        ADFtext.writelines('\n')
    ADFtext.writelines('-')
    ADFtext.writelines('\n')
    ADFtext.writelines(input('Digite a cadeia (em sequencia e sem espaco): '))
    ADFtext.writelines('\n')
    ADFtext.close()
    return 0

def copiarAFDtxt():
    print('=================================Salvar AFD=================================')
    try:
        origAFD = open(input('Digite o diretorio do arquivo a ser copiado: '), 'r')
    except:
        print("Erro de leitura")
        return -1
    try:
        copiaAFD = open(input('Digite o diretorio da copia: '), 'w')
    except:
        print("Erro de escrita")
        return -1

    for linha in origAFD:
        copiaAFD.writelines(linha.split())
        copiaAFD.writelines('\n')

    origAFD.close()
    copiaAFD.close()

    return 0

if __name__ == '__main__':

    inputN = -2

    while inputN != '0':
        print('====================================MENU DE OPCOES====================================')
        print('1) Gerenciar AFD')
        print('2) Gerenciar AFN')
        print('0) Fechar Programa')
        inputN = input('Digite a opcao desejada: ')
        print('=================================')
        if inputN =='1':
            print('1) Salvar o AFD em um arquivo texto')
            print('2) Carregar o AFD de um arquivo texto')
            print('3) Criar cópia do AFD')
            inputN = input('Digite a opcao desejada: ')
            print('=================================')
            if inputN == '1':
                salvarAFDtxt()
            elif inputN == '2':
                if lerAFDtxt() == 0:
                    print('criado com sucesso')
                else:
                    print("Erro de criacao")
            elif inputN == '3':
                if copiarAFDtxt() == 0:
                    print('Copiado com sucesso')
                else:
                    print('Falha na copia')
            else:
                print('Opcao invalida')
        elif inputN == '2':
            print('AFN')
        elif inputN == '0':
            print('Fechando')
        else:
            print('Opcao invalida')









