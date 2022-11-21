import numpy as np
from numpy import mean
import matplotlib.pyplot as plt
from math import sqrt

#Punto 1
fp =open ("datos.txt","r")
col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
col6=[]
col7=[]
col8=[]
col9=[]
col10=[]
for line in fp:
        sline=line.split()
        col1.append(float(sline[0]))
        col2.append(float(sline[1]))
        col3.append(float(sline[2]))
        col4.append(float(sline[3]))
        col5.append(float(sline[4]))
        col6.append(float(sline[5]))
        col7.append(float(sline[6]))
        col8.append(float(sline[7]))
        col9.append(float(sline[8]))
        col10.append(float(sline[9]))

        
promcol1 = mean(col1[0])
promcol2 = mean(col2[1])
promcol3 = mean(col3[2])
promcol4 = mean(col4[3])
promcol5 = mean(col5[4])
promcol6 = mean(col6[5])
promcol7 = mean(col7[6])
promcol8 = mean(col8[7])
promcol9 = mean(col9[8])
promcol10 = mean(col10[9])

datos=np.zeros((800,10))


#for col in range(0,10):
for fil in range(0,800):
        datos[fil][0]=col1[fil]
        datos[fil][1]=col2[fil]
        datos[fil][2]=col3[fil]
        datos[fil][3]=col4[fil]
        datos[fil][4]=col5[fil]
        datos[fil][5]=col6[fil]
        datos[fil][6]=col7[fil]
        datos[fil][7]=col8[fil]
        datos[fil][8]=col9[fil]
        datos[fil][9]=col10[fil]

print datos
        
#Punto 2
#matriz =np.matrix([col1, col2, col3, col4, col5, col6, col7, col8, col9, col10])

#for ke in range(800):
#        =col1[ke],col2[ke],col3[ke],col4[ke],col5[ke],col1[ke]

matriz=datos
mat_cov = np.cov(matriz, rowvar=False)

#Punto 5
eigval, eigvec = np.linalg.eig(mat_cov)

print "eigen", len(eigval),len(eigvec)
suma = np.sum(eigval)

pv_Zn = eigval[0]/suma
pv_Si = eigval[1]/suma
pv_K = eigval[2]/suma
pv_Mn = eigval[3]/suma
pv_Fe = eigval[4]/suma
pv_Sr = eigval[5]/suma
pv_Ti = eigval[6]/suma
pv_Pb = eigval[7]/suma
pv_Al = eigval[8]/suma
pv_Kr = eigval[9]/suma

#Punto 8
pv = [pv_Zn, pv_Si, pv_K, pv_Mn, pv_Fe, pv_Sr, pv_Ti, pv_Pb, pv_Al, pv_Kr]
print pv_Zn, pv_Si, pv_K, pv_Mn, pv_Fe, pv_Sr, pv_Ti, pv_Pb, pv_Al, pv_Kr

plt.figure()
labels = "Zn", "Si", "K", "Mn", "Fe", "Sr", "Ti", "Pb", "Al", "Kr"
plt.pie(pv, labels = labels, autopct='%1.1f%%', startangle=90)
plt.show()


#PUnto 6
dotZn = np.dot(eigvec[0].T, datos.T)
dotSi = np.dot(eigvec[1].T, datos.T)
dotK = np.dot(eigvec[2].T, datos.T)
dotMn = np.dot(eigvec[3].T, datos.T)
dotFe = np.dot(eigvec[4].T, datos.T)
dotSr = np.dot(eigvec[5].T, datos.T)
dotTi = np.dot(eigvec[6].T, datos.T)
dotPb = np.dot(eigvec[7].T, datos.T)
dotAl = np.dot(eigvec[8].T, datos.T)
dotKr = np.dot(eigvec[9].T, datos.T)



#normalizacion de vectores
norZn=np.linalg.norm(dotZn)
norSi=np.linalg.norm(dotSi)
norK=np.linalg.norm(dotK)
norMn=np.linalg.norm(dotMn)
norFe=np.linalg.norm(dotFe)
norSr=np.linalg.norm(dotSr)
norTi=np.linalg.norm(dotTi)
norPb=np.linalg.norm(dotPb)
norAl=np.linalg.norm(dotAl)
norKr=np.linalg.norm(dotKr)

#Punto 7
#std_Zn = np.std(dotZn)/norZn
#std_Si = np.std(dotSi)/norSi
#std_K = np.std(dotK)/norK

#std_Mn = np.std(dotMn)/norMn
std_Fe = np.std(dotFe)/norFe
std_Sr = np.std(dotSr)/norSr
std_Ti = np.std(dotTi)/norTi
std_Pb = np.std(dotPb)/norPb
std_Al = np.std(dotAl)/norAl
std_Kr = np.std(dotKr)/norKr


std_Zn = np.std(dotZn)/norZn
std_Si = np.std(dotSi)/norSi
std_K = np.std(dotK)/norK
std_Mn = np.std(dotMn)/norMn
std_Fe = np.std(dotFe)/norFe
std_Sr = np.std(dotSr)/norSr
std_Ti = np.std(dotTi)/norTi
std_Pb = np.std(dotPb)/norPb
std_Al = np.std(dotAl)/norAl
std_Kr = np.std(dotKr)/norKr
print "stds ",std_Zn, std_Si, std_K, std_Mn, std_Fe, std_Sr, std_Ti, std_Pb, std_Al, std_Kr
summma=std_Zn+ std_Si+ std_K+ std_Mn+ std_Fe+ std_Sr+ std_Ti+ std_Pb+ std_Al+ std_Kr
summma=max(std_Zn, std_Si, std_K, std_Mn, std_Fe, std_Sr, std_Ti, std_Pb, std_Al, std_Kr)
print "varianzas ",summma
#pv = [std_Zn , std_Si, std_K, std_Mn, std_Fe, std_Sr, std_Ti, std_Pb, std_Al, std_Kr]
pv = [norZn*800 , norSi*800, norK*800, norMn*800, norFe*800, norSr*800, norTi*800, norPb*800, norAl*800, norKr*800]
plt.figure()
labels = "varZn", "Si", "K", "Mn", "Fe", "Sr", "Ti", "Pb", "Al", "Kr"
plt.pie(pv, labels = labels, autopct='%1.1f%%', startangle=90)
plt.show()	

