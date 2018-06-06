#-*- coding:utf-8 -*-
from matplotlib import rcParams
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
rcParams['font.family'] = 'Liberation Sans'
rcParams['font.sans-serif'] = ['Liberation Sans']
rcParams['text.latex.unicode']=True
plt.style.use('classic')

import numpy as np

RBC_limits = [4.5, 5.9]
HGB_limits = [13.5, 18.5]
HCT_limits = [40, 54]

MCV_limits = [76, 102.9]
MCH_limits = [25.7, 35.7]
MCHC_limits = [29.5, 38.8]
RDW_limits = [10.3, 15.9]

PLT_limits = [135, 495]
PDW_limits = [11, 18]
MPV_limits = [6, 11]

WBC_limits = [3.8, 10.5]
PCT_limits = [0.2, 0.5]

RBC = [5.04, 5.58, 5.08, 4.96]
HGB = [13, 15.4, 15.4, 15.5]
HCT = [39.7, 47, 46.1, 45.5]

MCV = [79, 84, 91, 92]
MCH = [25.9, 27.6, 30.2, 31.3]
MCHC = [32.8, 32.8, 33.3, 34.1]
RDW = [17.4, 18.4, 14.5, 13.6]

PLT = [220, 230, 206, 180]
PDW = [18, 18.8, 18, 17.8]
MPV = [9.5, 9.5, 9.3, 9.2]

WBC = [3.8, 4.6, 5.1, 4.3]
PCT = [0.2, 0.2, 0.2, 0.2]

dates = ["18.12.17", "05.02.18", "04.04.18", "06.06.18"]

def draw(ax, data, data_limits, label, title=None):
    y = list(range(0, len(data)))
    ax.plot(y, data, "bo--")
    ax.plot((-1, 100), (data_limits[0], data_limits[0]), "g-", linewidth=2)
    ax.plot((-1, 100), (data_limits[1], data_limits[1]), "g-", linewidth=2)
    d = data_limits[0] * 0.05
    y_min_lim = min(data_limits[0] - d, min(data) - d)
    y_max_lim = max(data_limits[1] + d, max(data) + d)
    ax.set_ylim(y_min_lim, y_max_lim)
    ax.set_xlim(np.min(y) - 0.2, np.max(y) + 0.2)
    if title is not None:
        ax.set_title(title, weight="semibold", size="medium")
    ax.set_ylabel(label, weight="semibold", size="medium")
    ax.grid()
    for x, y in enumerate(data):
        ax.annotate(y, (x, y), ha="center", va="bottom", weight="semibold", size="medium")

def output(plt, show_only, filename):
    if show_only is True:
        plt.show()
    else:
        plt.savefig(u"%s.pdf" % (filename), bbox_inches='tight')

def drawFirstPartOfErythrocytes(show_only):
    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)

    draw(ax1, RBC, RBC_limits, "RBC", u"Czerwone krwinki")
    draw(ax2, HGB, HGB_limits, "HGB")
    draw(ax3, HCT, HCT_limits, "HCT")

    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)

    output(plt, show_only, "czerwone krwinki 1")
    
def drawSecondPartOfErythrocytes(show_only):
    pass

def drawThrombocytes(show_only):
    pass

def drawLeukocytesAndPlasma(show_only):
    pass

if __name__ == "__main__":
    show_only = True
    drawFirstPartOfErythrocytes(show_only)
    drawSecondPartOfErythrocytes(show_only)
    drawThrombocytes(show_only)
    drawLeukocytesAndPlasma(show_only)
