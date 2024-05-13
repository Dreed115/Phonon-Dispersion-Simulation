import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.loadtxt("dispPb_alloy.dat")
data2 = np.loadtxt("dispPb_fs.dat")
data3 = np.loadtxt("dispPb_meam.dat")
data4 = pd.read_csv("datosPb_exp.csv")
data6 = pd.read_csv("datosPb_exp1.csv")
data7 = pd.read_csv("datosPb_exp2.csv")

Xvalues = data4["x"]
Xvalues1 = data6["x"]
Xvalues2 = data7["x"]
Curve1 = data4["Curve1"]
Curve2 = data6["Curve1"]
Curve3 = data7["Curve1"]

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
x6 = list(Xvalues1)
x7 = list(Xvalues2)
y12 = list(Curve1)
y13 = list(Curve2)
y14 = list(Curve3)

x5 = data3[:,3]
y15 = data3[:,4]
y16 = data3[:,5]
y17 = data3[:,6]

plt.figure()

plt.scatter(x4,y12, linewidth=0.7, s=100, zorder=20, marker=".", color="white", edgecolor="black", label="Experimental")
plt.scatter(x6,y13, linewidth=0.7, s=100, zorder=20, marker=".", color="white", edgecolor="black")
plt.scatter(x7,y14, linewidth=0.7, s=100, zorder=20, marker=".", color="white", edgecolor="black")

plt.axvline(x=0.707107, linewidth=0.7, zorder=0, color='dimgray')
plt.axvline(x=1.06066, linewidth=0.7, zorder=0, color='dimgray')
plt.axvline(x=1.41421, linewidth=0.7, zorder=0, color='dimgray')
plt.axvline(x=2.63896, linewidth=0.7, zorder=0, color='dimgray')


plt.plot(x,y,"--", linewidth=0.7, color="limegreen", label="Alloy")
plt.plot(x,y1,"--", linewidth=0.7, color="limegreen")
plt.plot(x,y2,"--", linewidth=0.7, color="limegreen")

plt.plot(x2,y6,"--", linewidth=0.7, color="royalblue", label="FS")
plt.plot(x2,y7,"--", linewidth=0.7, color="royalblue")
plt.plot(x2,y8,"--", linewidth=0.7, color="royalblue")


plt.plot(x3,y9,"--", linewidth=0.7, color="salmon", label="MEAM")
plt.plot(x3,y10,"--", linewidth=0.7, color="salmon")
plt.plot(x3,y11,"--", linewidth=0.7, color="salmon")

plt.legend()

plt.xlabel("q")
plt.ylabel("THz")
plt.xlim([0,3.5])
plt.ylim([0,2.5])
plt.xticks([])
plt.savefig('dispPb.png', dpi=1000)
plt.close()