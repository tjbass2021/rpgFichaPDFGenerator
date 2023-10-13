def modificador(atributo):
    mod = 0
    if atributo == 1:
        mod = -5
    elif atributo == 2 or atributo == 3:
        mod = -4
    elif atributo == 4 or atributo == 5:
        mod = -3
    elif atributo == 6 or atributo == 7:
        mod = -2
    elif atributo == 8 or atributo == 9:
        mod = -1
    elif atributo == 10 or atributo == 11:
        mod = 0
    elif atributo == 12 or atributo == 13:
        mod = 1
    elif atributo == 14 or atributo == 15:
        mod = 2
    elif atributo == 16 or atributo == 17:
        mod = 3
    elif atributo == 18 or atributo == 19:
        mod = 4
    elif atributo == 20 or atributo == 21:
        mod = 5
    elif atributo == 22 or atributo == 23:
        mod = 6
    elif atributo == 24 or atributo == 25:
        mod = 7
    elif atributo == 26 or atributo == 27:
        mod = 8
    elif atributo == 28 or atributo == 29:
        mod = 9
    elif atributo >= 30:
        mod = 10
    return mod


def calcvida(classe, modconstituicao):
    vida = 0
    classe = classe.lower()
    if classe == 'barbaro' or classe == 'bárbaro':
        vida = 12 + modconstituicao
    elif classe == 'bardo':
        vida = 8 + modconstituicao
    elif classe == 'bruxo':
        vida = 8 + modconstituicao
    elif classe == 'clérigo' or classe == 'clerigo':
        vida = 8 + modconstituicao
    elif classe == 'druida':
        vida = 8 + modconstituicao
    elif classe == 'guerreiro':
        vida = 10 + modconstituicao
    elif classe == 'ladino':
        vida = 8 + modconstituicao
    elif classe == 'mago':
        vida = 6 + modconstituicao
    elif classe == 'monge':
        vida = 8 + modconstituicao
    elif classe == 'paladino':
        vida = 10 + modconstituicao
    elif classe == 'patrulheiro':
        vida = 10 + modconstituicao

    return vida


def aumentoatributoforca(raca, forca):
    forca = int(forca)
    raca = raca.lower()
    if raca == 'anão da montanha' or raca == 'humano' or raca == 'draconato' or raca == 'meio-orc':
        forca = forca + 2
    return forca


def aumentoatributodestreza(raca, destreza):
    destreza = int(destreza)
    raca = raca.lower()
    if raca == 'elfo' or raca == 'halfiling':
        destreza = destreza + 2
    elif raca == 'humano' or raca == 'gnomo da floresta':
        destreza = destreza + 1
    return destreza


def aumentoatributoconstituicao(raca, constituicao):
    constituicao = int(constituicao)
    raca = raca.lower()
    if raca == 'anão':
        constituicao = constituicao + 2
    elif raca == 'halfling robusto' or raca == 'gnomo das rochas' or raca == 'humano' or raca == 'meio-orc':
        constituicao = constituicao + 1
    return constituicao


def aumentoatributointeligencia(raca, inteligencia):
    inteligencia = int(inteligencia)
    raca = raca.lower()
    if raca == 'humano' or raca == 'alto elfo' or raca == 'tiefling':
        inteligencia = inteligencia + 1
    elif raca == 'gnomo':
        inteligencia = inteligencia + 2
    return inteligencia


def aumentoatributosabedoria(raca, sabedoria):
    sabedoria = int(sabedoria)
    raca = raca.lower()
    if raca == 'humano' or raca == 'anão da colina' or raca == 'elfo da floresta':
        sabedoria = sabedoria + 1
    return sabedoria


def aumentoatributocarisma(raca, carisma):
    carisma = int(carisma)
    raca = raca.lower()
    if raca == 'humano' or raca == 'draconato' or raca == 'drow' or raca == 'halfling pés-leves':
        carisma = carisma + 1
    elif raca == 'tiefling' or raca == 'meio-elfo':
        carisma = carisma + 2
    return carisma
