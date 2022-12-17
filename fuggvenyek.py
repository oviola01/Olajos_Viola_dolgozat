
#1
def beker():
    paros = int(input("Kérlek adj meg egy páros számot!"))
    while paros % 2 != 0:
        paros = int(input("Sajnos ez páratlan, kérlek adj meg egy másik számot!"))
    print(paros)

