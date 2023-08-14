
niveles = 0
estrellas = '⭐'
conteo = 1
base = int(input('¿La base de cuantas estrellas quieres que sea?'))
while base > niveles:
    print(' '*int((base/2)), '*'*conteo,' '*int((base/2)))
    conteo += 1
    base -=1
    niveles += 1
    if base == niveles:
        break
