from AutomatoFD import AutomatoFD
from TesteAFDAceita import TesteAFDAceita


def exemploAFDFormat():
    print('=================================Calculo de AFD=================================')
    print('Forneca o endereco de um arquivo .txt com a seguinte formatacao das linhas:')
    print('(1) Conter o alfabeto')
    print('(2) Quantidade de estados')
    print('(3) Estado inicial')
    print('(4) Estados finais')
    print('(5 a N) Transicoes')
    print('====================================Exemplo====================================')
    print('ab')
    print('4')
    print('1')
    print('4')
    print('12a')
    print('21a')
    print('34a')
    print('43a')
    print('13b')
    print('31b')
    print('24b')
    print('42b')
    print('==================================FIM Exemplo==================================')
    return 0

def lerAFDtxt(arquivo):

    arquivoLeitura = open(arquivo, "r")

    i = 0
    text = ''
    afd = ''
    cadeia = ''

    #for que le o arquivo
    for linha in arquivoLeitura:
        argumento = linha.split()
        if i == 0:
            for y in argumento:
                text += y
            #foi necessario fazer o for incrementando a variavel text
            #pois qd se passa o argumento as chaves [ ] vao junto
            #virando um simbolo do alfabeto
            afd = AutomatoFD(text)
        elif i == 1:
            #a quantidade de estados a serem criadas depende do numero
            #que esta na posicao 0 da linha, incrementa +1 para o
            #funcionamento correto do for
            for x in range(1, int(argumento[0]) + 1):
                afd.criaEstado(x)
        elif i == 2:
            afd.mudaEstadoInicial(int(argumento[0]))
        elif i == 3:
            for y in argumento:
                #o mesmo caso que ocorreu na criacao do alfabeto
                afd.mudaEstadoFinal(int(y), True)
        elif i >= 4:
            afd.criaTransicao(argumento[0][0], argumento[0][1], argumento[0][2])
        i = i + 1

    print(afd)


    cadeia= input('Digite a cadeia ')
    afd.limpaAfd()
    parada = afd.move(cadeia)
    if not afd.deuErro() and afd.estadoFinal(parada):
        print('Aceita cadeia "{}"'.format(cadeia))
        return afd
    else:
        print('Rejeita cadeia "{}"'.format(cadeia))
        return 1



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
    print('Digite o estado atual, o estado novo e o simbolo (exemplo: 12a)')
    for i in range(x):
        ADFtext.writelines(input('T'+str(i)+': '))
        ADFtext.writelines('\n')
    ADFtext.close()
    return 0

def copiarAFtxt():
    print('=================================Copiar AFD=================================')
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

    #arquivoAuxiliar = "C:/Users/aleff/Desktop/lfa/teste.txt"

    while True:
        print('====================================MENU DE OPCOES====================================')
        print('1) Gerenciar AFD')
        print('2) Gerenciar AFN')
        print('3) Testar AFS ja criados')
        print('0) Fechar Programa')
        inputN = input('Digite a opcao desejada: ')
        print('=================================')
        if inputN =='1':
            print('1) Criar e Salvar o AFD em um txt')
            print('2) Ler e Testar o AFD de txt')
            print('3) Criar cópia do AFD')
            print('4) Calcular estados equivalentes do AFD')
            print('5) Testar a equivalência entre dois AFD')
            print('6) Calcular o autômato minimizado para um AFD')
            inputN = input('Digite a opcao desejada: ')
            print('=================================')
            if inputN == '1':
                if salvarAFDtxt() == 0:
                    print('Salvo com sucesso')
                else:
                    print('Falha no salvamento')
            elif inputN == '2':
                exemploAFDFormat()
                arquivo = input('Digite o caminho do arquivo: ')
                lerAFDtxt(arquivo)
            elif inputN == '3':
                if copiarAFtxt() == 0:
                    print('Copiado com sucesso')
                else:
                    print('Falha na copia')
            elif inputN == '4':
                if copiarAFtxt() == 0:
                    print('Copiado com sucesso')
                else:
                    print('Falha na copia')
            elif inputN == '5':
                if copiarAFtxt() == 0:
                    print('Copiado com sucesso')
                else:
                    print('Falha na copia')
            elif inputN == '6':
                arquivo = input('Digite o caminho do arquivo: ')
                afdm=lerAFDtxt(arquivo)
                if(afdm != 1):
                    afdm.minimiza()
                else:
                    print("Automato nao aceito")
            else:
                print('Opcao invalida')
        elif inputN == '2':
            print('1) Criar e Salvar o AFN em um txt')
            print('2) Ler e Testar o AFN de txt')
            print('3) Criar cópia do AFN')
            inputN = input('Digite a opcao desejada: ')
            print('=================================')
            if inputN == '1':
                ''' if salvarAFNtxt() == 0:
                    print('Salvo com sucesso')
                else:
                    print('Falha no salvamento')'''
            elif inputN == '2':
               '''  if lerAFNtxt() == 0:
                    print('Lido com sucesso')
                else:
                    print("Erro de Leitura")'''
            elif inputN == '3':
                if copiarAFtxt() == 0:
                    print('Copiado com sucesso')
                else:
                    print('Falha na copia')
            else:
                print('Opcao invalida')
        elif inputN == '3':
            print('1: Testar um AFD')
            print('2: Testar um AFN')
            print('3: Testar AFD com estado equivalente')
            print('4: Testar a equivalencia de 2 AFDs')
            print('5: Testar minimizacao')
            inputN = input('Digite a opcao desejada: ')
            print('=================================')
            if inputN == '1':
                TesteAFDAceita()
        elif inputN == '0':
            print('Fechando')
            break
        else:
            print('Opcao invalida')









