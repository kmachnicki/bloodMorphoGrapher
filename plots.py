# -*- coding:utf-8 -*-

import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt

rcParams['font.family'] = 'Liberation Sans'
rcParams['font.sans-serif'] = ['Liberation Sans']
rcParams['text.latex.unicode'] = True
plt.style.use('classic')

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

def draw(ax, data, data_limits, labels, ylabel, unit, title=None):
    y = list(range(0, len(data)))
    ax.plot(y, data, "bo--")
    ax.plot((-1, 100), (data_limits[0], data_limits[0]), "g-", linewidth=2,
            label="%s-%s %s" % (data_limits[0], data_limits[1], unit))
    ax.plot((-1, 100), (data_limits[1], data_limits[1]), "g-", linewidth=2)
    d = data_limits[0] * 0.05
    y_min_lim = min(data_limits[0] - d, min(data) - d)
    y_max_lim = max(data_limits[1] + d, max(data) + d)
    ax.set_ylim(y_min_lim, y_max_lim)
    ax.set_xlim(np.min(y) - 0.2, np.max(y) + 0.2)
    if title is not None:
        ax.set_title(title, weight="semibold", size="medium")
    ax.set_ylabel(ylabel, weight="semibold", size="medium")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels)
    legend_location = "upper left" if abs(data_limits[0] - data[0]) < abs(data_limits[1] - data[0]) else "lower left"
    ax.legend(loc=legend_location, prop={"size":10})
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

    draw(ax1, RBC, RBC_limits, dates, "RBC", "[mln/µl]", u"Czerwone krwinki")
    draw(ax2, HGB, HGB_limits, dates, "HGB ", "[g/dl]")
    draw(ax3, HCT, HCT_limits, dates, "HCT", "[%]")

    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)

    output(plt, show_only, u"czerwone krwinki 1")

def drawSecondPartOfErythrocytes(show_only):
    f, (ax1, ax2) = plt.subplots(2, sharex=True)

    draw(ax1, MCV, MCV_limits, dates, "MCV", "[fl]", u"Czerwone krwinki")
    draw(ax2, MCH, MCH_limits, dates, "MCH", "[pg]")

    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)

    output(plt, show_only, u"czerwone krwinki 2")

def drawThirdPartOfErythrocytes(show_only):
    f, (ax1, ax2) = plt.subplots(2, sharex=True)

    draw(ax1, MCHC, MCHC_limits, dates, "MCHC", "[g/dl]", u"Czerwone krwinki")
    draw(ax2, RDW, RDW_limits, dates, "RDW", "[%]")

    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)

    output(plt, show_only, u"czerwone krwinki 3")

def drawThrombocytes(show_only):
    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)

    draw(ax1, PLT, PLT_limits, dates, "PLT", "[tys/µl]", u"Płytki krwi")
    draw(ax2, PDW, PDW_limits, dates, "PDW", "[%]")
    draw(ax3, MPV, MPV_limits, dates, "MPV", "[fl]")

    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)

    output(plt, show_only, u"płytki krwi")

def drawLeukocytesAndPlasma(show_only):
    f, (ax1, ax2) = plt.subplots(2, sharex=True)

    draw(ax1, WBC, WBC_limits, dates, "WBC", "[tys/µl]", u"Leukocyty i osocze")
    draw(ax2, PCT, PCT_limits, dates, "PCT", "[%]")

    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)

    output(plt, show_only, u"leukocyty i osocze")

if __name__ == "__main__":
    show_only = False
    drawFirstPartOfErythrocytes(show_only)
    drawSecondPartOfErythrocytes(show_only)
    drawThirdPartOfErythrocytes(show_only)
    drawThrombocytes(show_only)
    drawLeukocytesAndPlasma(show_only)
