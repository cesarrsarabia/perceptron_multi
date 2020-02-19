#Ramirez Sarabia César Eduardo 
#Perceptron. Práctica 3
import numpy as np
import matplotlib
from pylab import xlim
from pylab import ylim
import matplotlib.pyplot as plt
import time
import numpy as np


def grafica_lineas(this_w,last_plot):
    clases = ['--k','--b','--r','--y','--g']
    for c,item in enumerate(this_w):
        ax.plot([-2,3],[(-item[0]/item[1]) *
        (-2)-(b[c]/item[1]), (-item[0]/item[1])*(3)-(b[c]/item[1])],clases[c])
        plt.pause(0.01)
    for c in range(1,num_col_salidas):
        ax.lines.pop(last_plot + c)

def funcion_escalon(x):
    if x<0:
        return 0
    else:
        return 1


def obtiene_Salida(r,c):
    posicion = salidas_deseadas[r]
    if c == 0:
        return posicion[0]
    else:
        return posicion[c+1]


#training set contiene entradas y salidas
training_set = []


with open('entradas.txt') as f_1:
    datos_entradas = f_1.read().splitlines() 

with open('salidas_deseadas.txt') as f_2:
    salidas_deseadas = f_2.read().splitlines() 

#Convierte entrada a lista de enteros
for i, element in enumerate(datos_entradas):
    x =  [int(k) for k in element.split()]
    datos_entradas[i] = x

#Convierte salidas deseadas a lista de enteros
for i, element in enumerate(salidas_deseadas):
    x =  [int(k) for k in element.split()]
    salidas_deseadas[i] = x
num_col_salidas = len(salidas_deseadas[0]) - salidas_deseadas[0].count(' ')

# Inicializacion de parametros ( pesos, eta , b)
################## c,r
w = np.random.rand(num_col_salidas,2)
errors = [] 
eta = .5
epoch = 40
b = np.zeros(num_col_salidas)

#crea el training set
for i in range(num_col_salidas):
    row = 0
    training_set_aux = []
    for j in datos_entradas:
        aux = salidas_deseadas[row]
        a = ((int(j[0]),
                int(j[1])),
                aux[i])
        training_set_aux.append(a)
        row += 1
    training_set.append(training_set_aux)

fig, ax = plt.subplots()
xlim([-2,3])
ylim([-2,3])

x1 = np.array([[0,1,0,1],[0,0,1,1]])
ax.plot(x1[0,0],x1[1,0], '*b')
ax.plot(x1[0,1],x1[1,1], '*g')
ax.plot(x1[0,2],x1[1,2], 'pm')
ax.plot(x1[0,3],x1[1,3], 'or')


#grafica primera linea
#ax.plot([-2,3],[(-w[0][0]/w[0][1])*(-2)-(b/w[0][1]), (-w[0][0]/w[0][1])*(3)-(b/w[0][1])],'--g')
#grafica segunda linea
#ax.plot([-2,3],[(-w[1][0]/w[1][1])*(-2)-(b/w[1][1]), (-w[1][0]/w[1][1])*(3)-(b/w[1][1])],'--m')

lst_i_plot = 3
#print(w[0][0])
#print(w[0][1])
for i in range(epoch):
    for count,fila_training_item in enumerate(training_set):
        for x,y in fila_training_item:
            u = sum(x*w[count]) + b[count] 
            error = y - funcion_escalon(u)
            for index, value in enumerate(x):          
                w[count][index] += eta * error * value
                b[count] += eta*error
                grafica_lineas(w,lst_i_plot)
                




#plt.show()
#print('Done')