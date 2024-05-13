
id = 0

map = open("map.in","w")

datos = "16 " + "16 " + "16 " + "1 " + "\n"
map.write(datos)

datos = "#l1 " + "l2 " + "l3 " + "k " + "atom_id " + "\n"
map.write(datos)

for z in range(0,16):
    l3 = z
    for y in range(0,16):
        l2 = y
        for x in range(0,16):
            l1 = x
            id = id + 1
            Columna = str(l1) + " " + str(l2) + " " + str(l3) + " " + "0 " + str(id) + " "  +"\n"
            map.write(Columna)
        
map.close()
