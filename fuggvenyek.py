import random

#1
#a)
def beker(parameter = " "):
    paros = int(input(f"Kérlek {parameter} páros számot! "))
    while paros % 2 != 0:
        paros = int(input("Sajnos ez páratlan, kérlek adj meg egy másik számot! "))
    return paros

#b)
def tobbszam(mennyi):
    lista = []
    i = 0
    while i < mennyi:
        ujszam = beker(f"add meg a(z) {i + 1}.")
        lista.append(ujszam)
        i += 1
    print(f"Az általad megadott számok a következők: {lista}.")
    return lista

#c)
def legkisebb(hol):
    j = 0
    kicsi = hol[0]
    hanyadik = 1
    while j < len(hol):
        if hol[j] < kicsi:
            kicsi =hol[j]
            hanyadik = j + 1
        j += 1
    print(f"{hanyadik}. lépésben adtad meg a legkisebb páros számot, melynek értéke: {kicsi}")

#2
#a)
def veletlenek():
    i = 0
    szamaim = []
    while i < 13:
        veletlen = int(random.random()*191)-40
        szamaim.append(veletlen)
        i += 1
    print(f"2. a) A lista: {szamaim}")
    return szamaim

#b)
def ketjegyuek_szama(lista):
    db = 0
    j = 0
    while j < len(lista):
        if lista[j] < 0:
            vizsg = lista[j] * -1
        else:
            vizsg = lista[j]
        if vizsg >= 10 and vizsg < 100:
            db += 1
        j += 1
    print(f"2. b) A kétjegyű számok száma: {db}")

#c)
def paros_osszege(lista):
    j = 0
    osszeg_pp = 0
    while j < len(lista):
        if lista[j] % 2 == 0:
            osszeg_pp += lista[j]
        j += 1
    return osszeg_pp

#d)
def paratlan_osszege(lista):
    j = 0
    osszeg_pln = 0
    while j < len(lista):
        if lista[j] % 2 != 0:
            osszeg_pln += lista[j]
        j += 1
    return osszeg_pln

#e)
def nagyobb(lista):
    parosok = paros_osszege(lista)
    paratlanok = paratlan_osszege(lista)
    if parosok < paratlanok:
        relacio = "<"
    else:
        relacio = ">"
    print(f"2. e) A párosok összege {parosok} {relacio} a páratlanok összege {paratlanok}")
