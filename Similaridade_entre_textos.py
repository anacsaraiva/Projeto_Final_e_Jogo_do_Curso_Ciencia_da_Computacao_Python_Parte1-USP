import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    
    grau = 0
    i = 0
    soma = 0
    
    while i < 6:
        soma += abs(as_a[i]-as_b[i])
        i +=1

    grau = soma/6

    return grau

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    palavras = []
    frases = []
    tamanho_media_palavras = 0
    tamanho_palavras = 0
    soma_sent = 0
    soma_fr = 0
    
    sentenca = separa_sentencas(texto)

    for sent in sentenca:
        soma_sent += len(sent)
        novas_frases = separa_frases(sent)
        frases.extend(novas_frases)
        for fr in novas_frases:
            soma_fr += len(fr)
            novas_palavras = separa_palavras(fr)
            palavras.extend(novas_palavras)

    for i in palavras:
        tamanho_palavras += len(i)

    quantidade_palavras = len(palavras)

    tamanho_medio_palavras = tamanho_palavras/quantidade_palavras

    media_diferentes = n_palavras_diferentes(palavras)/quantidade_palavras

    media_unicas = (n_palavras_unicas(palavras))/quantidade_palavras

    tam_med_sent = soma_sent/len(sentenca)

    comp_sent = (len(frases))/len(sentenca)

    tam_med_fr = soma_fr/len(frases)


    return tamanho_medio_palavras,media_diferentes,media_unicas,tam_med_sent,comp_sent,tam_med_fr

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    assinaturas = 0
    n_menor = 1
    lista_comp = []
    
    for text in range(len(textos)):
        assinaturas = (calcula_assinatura(textos[text]))
        comp = compara_assinatura(assinaturas,ass_cp)
        lista_comp.append(comp)

    menor = lista_comp[0]

    for i in range(len(lista_comp)):
        if lista_comp[i] <= menor:
            menor = lista_comp[i]
            n_menor = i+1
            

    return n_menor
        
    
