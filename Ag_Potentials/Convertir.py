Nuevo = []
relacion = 1.13033254

with open("data.pos","r") as data:
    for i in data:
        Nuevo.append(i)
    dataAg = open("dataAg.pos","w")
    for n in range(0,12):
        dataAg.write(Nuevo[n])
    for j in range(12,524):
        a = Nuevo[j]
        b1 = (relacion)*float(a[10:22])
        b = "{0:.8f}".format(b1)
        c1 = (relacion)*float(a[27:38])
        c = "{0:.8f}".format(c1)
        d1 = (relacion)*float(a[43:57])
        d = "{0:.8f}".format(d1)
        Nuevo[j] = a[0:9] + str(b) + a[22:27] + str(c) + a[36:43] + str(d) + "\n"
        dataAg.write(Nuevo[j])
dataAg.close()
data.close()