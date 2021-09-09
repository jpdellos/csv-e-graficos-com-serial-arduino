from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from main import fileName




plt.style.use('fivethirtyeight')
eixo_x = []
index = count()
cont = 0
def animate(i):
    data = pd.read_csv(fileName)    # nome do arquivo do codigo 'main'
    x = eixo_x                #indice para o eixo x,caso tenha um dado no csv que queira usar como eixo x necessario trocar
    y1 = data["y1"]           #nome das colunas, caso exista mais, adicione mais variaveis
    y2 = data["y2"]

    global cont                #cria o indice
    while len(x) < len(y2):
        eixo_x.append(cont)
        cont += 1





    plt.cla()

    plt.plot(x, y1, label='y1')       # em 'label=' vai a legenda, escreva o nome da coluna
    plt.plot(x, y2, label='y2')
    plt.title("Title of the plot")
    plt.legend(loc='upper left')
    plt.tight_layout()



ani = FuncAnimation(plt.gcf(),animate, interval=1000)

plt.tight_layout()
plt.show()
