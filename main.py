import random
import fuggvenyek

"""
#1/a)
print(fuggvenyek.beker("adj meg egy"))

#1/b)
keres = int(input("Kérlek add meg, hány darab számmal szeretnél dolgozni! "))
vizsgalom = fuggvenyek.tobbszam(keres)

#1/c)
fuggvenyek.legkisebb(vizsgalom)

#2/a)
lista = fuggvenyek.veletlenek()

#2/b)
fuggvenyek.ketjegyuek_szama(lista)

#2/c)-d)-e)
fuggvenyek.nagyobb(lista)
"""

#3
szoveg = open("stadionok.txt", "r", encoding = "utf-8")
fejlec = szoveg.readline().strip().split(";")
print(fejlec)
nev = []
hely = []
csapat = []
elso = []
utolso = []
i = 1
while i < 41:
    #ez sajnos nem működik :(
    nev.append(szoveg.readlines().strip().split(";"))
    i += 1
print(nev)

#számlálás NewYork
j = 0
NYC_stad = []
NYC_csap = []
while j < len(hely):
    if hely[j] = "New York":
        NYC_stad.append(nev[j])
        NYC_csap.append(csapat[j])
    j += 1
k = 0
print("NewYorki csapatok:")
while k < len(NYC_stad):
    print(f"A(z) {NYC_stad[k]} stadionban a(z) {NYC_csap[k]}. számú csapat")
    k += 1
