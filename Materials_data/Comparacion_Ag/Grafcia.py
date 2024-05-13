import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.loadtxt("dispAg_alloy.dat")
data1 = np.loadtxt("dispAg16.dat")

data4 = pd.read_csv("datosAg_exp.csv")
data6 = pd.read_csv("datosAg_exp1.csv")
data7 = pd.read_csv("datosAg_exp2.csv")
data8 = pd.read_csv("datosAg_exp3.csv")

Xvalues = data4["x"]
Xvalues1 = data6["x"]
Xvalues2 = data7["x"]
Xvalues3 = data8["x"]
Curve1 = data4["Curve1"]
Curve2 = data6["Curve1"]
Curve3 = data7["Curve1"]
Curve4 = data8["Curve1"]

x = data[:,3]
y = data[:,4]
y1 = data[:,5]
y2 = data[:,6]

x1 = data1[:,3]
y3 = data1[:,4]
y4 = data1[:,5]
y5 = data1[:,6]

x4 = list(Xvalues)
x6 = list(Xvalues1)
x7 = list(Xvalues2)
x8 = list(Xvalues3)
y12 = list(Curve1)
y13 = list(Curve2)
y14 = list(Curve3)
y18 = list(Curve4)

plt.figure()

plt.scatter(x4,y12, s=100, linewidth=0.7, zorder=20, marker=".", color="white", edgecolor="black", label="Experimental")
plt.scatter(x6,y13, s=100, linewidth=0.7, zorder=20, marker=".", color="white", edgecolor="black")
plt.scatter(x7,y14, s=100, linewidth=0.7, zorder=20, marker=".", color="white", edgecolor="black")
plt.scatter(x8,y18, s=100, linewidth=0.7, zorder=20, marker=".", color="white", edgecolor="black")

plt.axvline(x=0.707107, linewidth=0.7, zorder=0, color='dimgray')
plt.axvline(x=1.06066, linewidth=0.7, zorder=0, color='dimgray')
plt.axvline(x=1.41421, linewidth=0.7, zorder=0, color='dimgray')
plt.axvline(x=2.63896, linewidth=0.7, zorder=0, color='dimgray')


plt.plot(x,y,"--", linewidth=0.7, color="limegreen", label="Alloy")
plt.plot(x,y1,"--", linewidth=0.7, color="limegreen")
plt.plot(x,y2,"--", linewidth=0.7, color="limegreen")

plt.plot(x1,y3,"--", linewidth=0.7, color="tomato", label="Alloy 16")
plt.plot(x1,y4,"--", linewidth=0.7, color="tomato")
plt.plot(x1,y5,"--", linewidth=0.7, color="tomato")


plt.legend()

plt.xlabel("q")
plt.ylabel("THz")
plt.xlim([0,3.5])
plt.ylim([0,5.5])
plt.xticks([])
plt.savefig('dispAg16.png', dpi=1000)
plt.close()