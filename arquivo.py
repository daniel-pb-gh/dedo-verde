def fasesConcluidas():
    arquivo = open("save/fasesConcluidas.txt", "a+")
    arquivo.seek(0)
    fases = arquivo.readlines()
    arquivo.close()

    return len(fases)

def escreveFase(fase):
    niveisCompletos = fasesConcluidas()
    if fase > niveisCompletos:
        arquivo = open("save/fasesConcluidas.txt", "a+")
        arquivo.write(str(fase) + '\n')
        arquivo.close()