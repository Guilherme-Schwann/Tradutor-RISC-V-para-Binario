# imports
import sys

def complementoDeDoisDec13(num):
    numBin = bin(num)[3:]
    
    while len(numBin) < 13:
        numBin = "0" + numBin
    
    numBin = numBin.replace("0", "z").replace("1", "0").replace("z", "1")

    numDec = int(numBin, 2) + 1
    numBin = bin(numDec)[2:]
    
    return numBin

def conversaoDecBin13(num):
    if num < 0:
        return complementoDeDoisDec13(num)
    
    else:
        numBin = bin(num)[2:]

        while len(numBin) < 13:
            numBin = "0" + numBin

        return numBin

def complementoDeDoisDec12(num):
    numBin = bin(num)[3:]
    
    while len(numBin) < 12:
        numBin = "0" + numBin
    
    numBin = numBin.replace("0", "z").replace("1", "0").replace("z", "1")

    numDec = int(numBin, 2) + 1
    numBin = bin(numDec)[2:]
    
    return numBin

def conversaoDecBin12(num):
    if num < 0:
        return complementoDeDoisDec12(num)
    
    else:
        numBin = bin(num)[2:]

        while len(numBin) < 12:
            numBin = "0" + numBin

        return numBin
    
def complementoDeDoisDec5(num):
    numBin = bin(num)[3:]
    
    while len(numBin) < 5:
        numBin = "0" + numBin
    
    numBin = numBin.replace("0", "z").replace("1", "0").replace("z", "1")

    numDec = int(numBin, 2) + 1
    numBin = bin(numDec)[2:]
    
    return numBin

def conversaoDecBin5(num):
    if num < 0:
        return complementoDeDoisDec5(num)
    
    else:
        numBin = bin(num)[2:]

        while len(numBin) < 5:
            numBin = "0" + numBin

        return numBin

def getInfo(comando):
    arqInfo = open("instrucoesInfo.txt", "r")
    infoLinhas = arqInfo.readlines()
    
    #busca binaria para achar a linha certa
    inicio = 0
    fim = len(infoLinhas) - 1
    meio = (inicio + fim) // 2

    while inicio <= fim:
        if infoLinhas[meio].split()[0] == comando:
            return infoLinhas[meio]
            break
            
        elif infoLinhas[meio].split()[0] < comando:
            inicio = meio + 1
        else:
            fim = meio - 1

        meio = (inicio + fim) // 2
    print("Não achei o comando nas infos")

def montarBin(linha):
    linha = linha.replace("(", " ").replace(")", " ").replace(" x", " ")
    linha = linha.replace(",", " ").split()

    infoComando = getInfo(linha[0])
    infoComando = infoComando.split()
    tipo = infoComando[1]

    if tipo == "I":
        if linha[0] in ["lw", "lb", "lh"]:
            aux = linha[2]
            linha[2] = linha[3]
            linha[3] = aux
        instrucaoBinT = conversaoDecBin12(int(linha[3])) + conversaoDecBin5(int(linha[2])) + infoComando[3] + conversaoDecBin5(int(linha[1])) + infoComando[2]
        return instrucaoBinT

    elif tipo == "R":
        instrucaoBinT = infoComando[4] + conversaoDecBin5(int(linha[3])) + conversaoDecBin5(int(linha[2])) + infoComando[3] + conversaoDecBin5(int(linha[1])) + infoComando[2]
        return instrucaoBinT

    elif tipo == "S":
        instrucaoBinT = conversaoDecBin12(int(linha[2]))[:7] + conversaoDecBin5(int(linha[1])) + conversaoDecBin5(int(linha[3])) + infoComando[3] + conversaoDecBin12(int(linha[2]))[7:] + infoComando[2]
        return instrucaoBinT

    elif tipo == "SB":
        endInt = conversaoDecBin13(int(linha[3]))

        instrucaoBinT = endInt[0] + endInt[2:8] + conversaoDecBin5(int(linha[2])) + conversaoDecBin5(int(linha[1])) + infoComando[3] + endInt[8:-1] + endInt[1] + infoComando[2]
        return instrucaoBinT
    else:
        print("comando não implementado")

def main():

    tipoOut = "indefinido"
    if sys.argv[1][-4:] != ".asm":
        print("Sintaxe de comando errada!")
        exit()    

    if len(sys.argv) == 2:
        tipoOut = "terminal"
    elif len(sys.argv) == 4 and sys.argv[2] == "-o":
        tipoOut = "arquivo"
    #abrir arquivos 

    try:
        arquivoIn = open(sys.argv[1], "r")
    except:
        print("Não foi possível abrir o arquivo de entrada!")
        exit()

    if tipoOut == "arquivo":
        try:
            arquivoOut = open(sys.argv[3], "w")
        except:
            print("Não foi possível abrir o arquivo de saída!")
    
    listaComandos = arquivoIn.readlines()

    for linha in listaComandos:
        linhaBin = montarBin(linha)

        if tipoOut == "terminal":
            print(linhaBin)
        elif tipoOut == "arquivo":
            arquivoOut.write(linhaBin + "\n")


if __name__ == "__main__":
    main()