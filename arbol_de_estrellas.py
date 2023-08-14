niveles = 0
base = int(input('¿La base de cuantas estrellas quieres que sea?'))
while base > niveles:
    print(' '*int((base)), '⭐'*niveles,' '*int((base)))
    base -=1
    niveles += 1
