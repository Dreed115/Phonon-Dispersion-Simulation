import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.loadtxt("dispAL_alloy.dat")
data2 = np.loadtxt("dispAL_fs.dat")
data3 = np.loadtxt("dispAL_meam.dat")
data4 = pd.read_csv("datosAl_exp.csv")
data5 = pd.read_csv("datosAl_exp1.csv")
data6 = pd.read_csv("datosAl_exp2.csv")

Xvalues = data4["x"]
Xvalues1 = data5["x"]
Xvalues2 = data6["x"]
Curve1 = data4["Curve1"]
Curve2 = data5["Curve2"]
Curve3 = data6["Curve3"]

x = data[:,3]
y = data[:,4]
y1 = data[:,5]
y2 = data[:,6]

x2 = data2[:,3]
y6 = data2[:,4]
y7 = data2[:,5]
y8 = data2[:,6]

x3 = data3[:,3]
y9 = data3[:,4]
y10 = data3[:,5]
y11 = data3[:,6]

x4 = list(Xvalues)
x5 = list(Xvalues1)
x6 = list(Xvalues2)
y12 = list(Curve1)
y13 = list(Curve2)
y14 = list(Curve3)

plt.figure()

plt.scatter(x4,y12, s=100, linewidth=0.7, zorder=20, marker=".", color="white", edgecolor="black", label="Experimental")
plt.scatter(x5,y13, s=100, linewidth=0.7, zorder=20, marker=".", color="white", edgecolor="black")
plt.scatter(x6,y14, s=100, linewidth=0.7, zorder=20, marker=".", color="white", edgecolor="black")

plt.axvline(x=0.707107, linewidth=0.7, zorder=0, color='dimgray')
plt.axvline(x=1.06066, linewidth=0.7, zorder=0, color='dimgray')
plt.axvline(x=1.41421, linewidth=0.7, zorder=0, color='dimgray')
plt.axvline(x=2.63896, linewidth=0.7, zorder=0, color='dimgray')

plt.plot(x,y,"--", linewidth=0.7, zorder=10, color="limegreen", label="Alloy")
plt.plot(x,y1,"--", linewidth=0.7, zorder=10, color="limegreen")
plt.plot(x,y2,"--", linewidth=0.7, zorder=10, color="limegreen")

plt.plot(x2,y6,"--", linewidth=0.7, zorder=15, color="royalblue", label="FS")
plt.plot(x2,y7,"--", linewidth=0.7, zorder=15, color="royalblue")
plt.plot(x2,y8,"--", linewidth=0.7, zorder=15, color="royalblue")

plt.plot(x3,y9,"--", linewidth=0.7, zorder=10, color="salmon", label="MEAM")
plt.plot(x3,y10,"--", linewidth=0.7, zorder=10, color="salmon")
plt.plot(x3,y11,"--", linewidth=0.7, zorder=10, color="salmon")


plt.legend()

plt.xlabel("q")
plt.ylabel("THz")
plt.xlim([0,3.5])
plt.ylim([0,16])
plt.xticks([])
plt.savefig('dispAl.png', dpi=1000)
plt.close()