
Nuevo = []

a = 4.09
id = 0
with open("data.pos","r") as data:
    for i in data:
        Nuevo.append(i)
    dataFCC = open("dataFCC.pos","w")
    for n in range(0,12):
        dataFCC.write(Nuevo[n])
    atom = 1
    for z in range(0,16):
        l3 = z*(a/(3**(1/2)))
        L3 = "{0:.8f}".format(l3)
        for y in range(0,16):
            l2 = z*(a)*((3/8)**(1/2))*(1/3) + y*a*((3/8)**(1/2))
            L2 = "{0:.8f}".format(l2)
            for x in range(0,16):
                l1 = z*(a/(2**(1/2)))*(1/2) + y*(a/(2**(1/2)))*(1/2) + x*(a/(2**(1/2)))
                L1 = "{0:.8f}".format(l1)
                id = id + 1
                Columna = format(str(id),">4") + "\t" + str (atom) + "\t"  + format(str(L1), ">15") + format(str(L2), ">15") + format(str(L3), ">15") +  "\n"
                dataFCC.write(Columna)
        
dataFCC.close()
data.close()