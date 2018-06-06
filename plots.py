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

def drawFirstPartOfErythrocytes():
    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)

    y = list(range(0, len(RBC)))
    ax1.plot(y, RBC, "bo--", label = u"RBC")
    ax1.plot((-1, 100), (RBC_limits[0], RBC_limits[0]), "g-", linewidth=2)
    ax1.plot((-1, 100), (RBC_limits[1], RBC_limits[1]), "g-", linewidth=2)
    d = RBC_limits[0] * 0.05
    y_min_lim = min(RBC_limits[0] - d, min(RBC) - d)
    y_max_lim = max(RBC_limits[1] + d, max(RBC) + d)
    ax1.set_ylim(y_min_lim, y_max_lim)
    ax1.set_xlim(np.min(y) - 0.2, np.max(y) + 0.2)
    ax1.set_title(u"Czerwone krwinki", weight="semibold", size="medium")
    ax1.set_ylabel(u"RBC", weight="semibold", size="medium")
    ax1.grid()
    for x, y in enumerate(RBC):
        ax1.annotate(y, (x, y), ha="center", va="bottom", weight="semibold", size="medium")

    y = list(range(0, len(HGB)))
    ax2.plot(y, HGB, "bo--", label = u"HGB")
    ax2.plot((-1, 100), (HGB_limits[0], HGB_limits[0]), "g-", linewidth=2)
    ax2.plot((-1, 100), (HGB_limits[1], HGB_limits[1]), "g-", linewidth=2)
    d = HGB_limits[0] * 0.05
    y_min_lim = min(HGB_limits[0] - d, min(HGB) - d)
    y_max_lim = max(HGB_limits[1] + d, max(HGB) + d)
    print(y_min_lim)
    print(y_max_lim)
    ax2.set_ylim(y_min_lim, y_max_lim)
    ax2.set_xlim(np.min(y) - 0.2, np.max(y) + 0.2)
    ax2.set_ylabel(u"HGB", weight="semibold", size="medium")
    ax2.grid()
    for x, y in enumerate(HGB):
        ax2.annotate(y, (x, y), ha="center", va="bottom", weight="semibold", size="medium")

    y = list(range(0, len(HCT)))
    ax3.plot(y, HCT, "bo--", label = u"HCT")
    ax3.plot((-1, 100), (HCT_limits[0], HCT_limits[0]), "g-", linewidth=2)
    ax3.plot((-1, 100), (HCT_limits[1], HCT_limits[1]), "g-", linewidth=2)
    d = HCT_limits[0] * 0.05
    y_min_lim = min(HCT_limits[0] - d, min(HCT) - d)
    y_max_lim = max(HCT_limits[1] + d, max(HCT) + d)
    ax3.set_ylim(y_min_lim, y_max_lim)
    ax3.set_xlim(np.min(y) - 0.2, np.max(y) + 0.2)
    ax3.set_ylabel(u"HCT", weight="semibold", size="medium")
    ax3.grid()
    for x, y in enumerate(HCT):
        ax3.annotate(y, (x, y), ha="center", va="bottom", weight="semibold", size="medium")
    
    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)
    
    #plt.savefig("%s.pdf" % (filename), bbox_inches='tight')
    plt.show()
    
def drawSecondPartOfErythrocytes():
    pass

def drawThrombocytes():
    pass

def drawLeukocytesAndPlasma():
    pass

if __name__ == "__main__":
    drawFirstPartOfErythrocytes()
    drawSecondPartOfErythrocytes()
    drawThrombocytes()
    drawLeukocytesAndPlasma()
