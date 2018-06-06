#-*- coding:utf-8 -*-
from matplotlib import rcParams
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
rcParams['font.family'] = 'Liberation Sans'
rcParams['font.sans-serif'] = ['Liberation Sans']
rcParams['text.latex.unicode']=True
plt.style.use('classic')

import numpy as np

def drawGraphs():
    y = list(range(0, 30))
    x = y
    f, (ax1, ax2) = plt.subplots(2, sharex=False)
    
    ax1.plot(y, x, "b-",label = u"Bez modyfikacji")  
    ax1.set_title(u"Średnie wychylenie od środka trasy per epizod, trasa: a")
    ax1.legend(loc = "best",prop={"size":10})
    ax1.set_xlim(np.min(y), np.max(y))
    ax1.set_ylabel(u"Wychylenie")
    ax1.set_xlabel(u"Epizod")
    ax1.grid()

    ax2.plot(y, x, "b-",label = u"Bez modyfikacji 2")  
    ax2.set_title(u"Średnie wychylenie od środka trasy per epizod, trasa: abbbbb")
    ax2.legend(loc = "best",prop={"size":10})
    ax2.set_xlim(np.min(y), np.max(y))
    ax2.set_ylabel(u"Wychylenie")
    ax2.set_xlabel(u"Epizod")
    ax2.grid()
    
    f.subplots_adjust(hspace=0.3)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)
    
    #plt.savefig("%s.pdf" % (filename), bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    drawGraphs()
