# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

rcParams["font.family"] = "Liberation Sans"
rcParams["font.sans-serif"] = ["Liberation Sans"]
rcParams["text.latex.unicode"] = True
plt.style.use("classic")

class Drawer(object):
    def __init__(self, morphology, show_only):
        self.morphology = morphology
        self.show_only = show_only

    def draw(self, ax, data, data_limits, ylabel, unit, labels, title=None):
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

    def output(self, plt, filename):
        if self.show_only is True:
            plt.show()
        else:
            plt.savefig(u"%s.pdf" % (filename), bbox_inches="tight")

    def draw_plots(self):
        self.draw_first_part_of_erythrocytes()
        self.draw_second_part_of_erythrocytes()
        self.draw_third_part_of_erythrocytes()
        self.draw_thrombocytes()
        self.draw_leukocytes_and_plasma()

    def draw_first_part_of_erythrocytes(self):
        f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)

        title = u"Czerwone krwinki 1"

        RBC = self.morphology.get_probe("RBC")
        HGB = self.morphology.get_probe("HGB")
        HCT = self.morphology.get_probe("HCT")

        for_women = self.morphology.show_data_limits_for_women()

        self.draw(ax1, RBC.get_samples(), RBC.get_limits(for_women), RBC.get_name(), RBC.get_unit(), self.morphology.dates)
        self.draw(ax2, HGB.get_samples(), HGB.get_limits(for_women), HGB.get_name(), HGB.get_unit(), self.morphology.dates)
        self.draw(ax3, HCT.get_samples(), HCT.get_limits(for_women), HCT.get_name(), HCT.get_unit(), self.morphology.dates)

        f.suptitle(u"%s\n%s\n%s" % (RBC, HGB, HCT), fontsize=12, fontweight="bold")
        f.subplots_adjust(hspace=0.1)
        fig = plt.gcf()
        fig.set_size_inches(8, 8)

        self.output(plt, title)

    def draw_second_part_of_erythrocytes(self):
        f, (ax1, ax2) = plt.subplots(2, sharex=True)

        title = u"Czerwone krwinki 2"

        MCV = self.morphology.get_probe("MCV")
        MCH = self.morphology.get_probe("MCH")

        for_women = self.morphology.show_data_limits_for_women()

        self.draw(ax1, MCV.get_samples(), MCV.get_limits(for_women), MCV.get_name(), MCV.get_unit(), self.morphology.dates)
        self.draw(ax2, MCH.get_samples(), MCH.get_limits(for_women), MCH.get_name(), MCH.get_unit(), self.morphology.dates)

        f.suptitle(u"%s\n%s" % (MCV, MCH), fontsize=12, fontweight="bold")
        f.subplots_adjust(hspace=0.1)
        fig = plt.gcf()
        fig.set_size_inches(8, 8)

        self.output(plt, title)

    def draw_third_part_of_erythrocytes(self):
        f, (ax1, ax2) = plt.subplots(2, sharex=True)

        title = u"Czerwone krwinki 3"

        MCHC = self.morphology.get_probe("MCHC")
        RDW = self.morphology.get_probe("RDW")

        for_women = self.morphology.show_data_limits_for_women()

        self.draw(ax1, MCHC.get_samples(), MCHC.get_limits(for_women), MCHC.get_name(), MCHC.get_unit(), self.morphology.dates)
        self.draw(ax2, RDW.get_samples(), RDW.get_limits(for_women), RDW.get_name(), RDW.get_unit(), self.morphology.dates)

        f.suptitle(u"%s\n%s" % (MCHC, RDW), fontsize=12, fontweight="bold")
        f.subplots_adjust(hspace=0.1)
        fig = plt.gcf()
        fig.set_size_inches(8, 8)

        self.output(plt, title)

    def draw_thrombocytes(self):
        f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)

        title = u"Płytki krwi"

        PLT = self.morphology.get_probe("PLT")
        PDW = self.morphology.get_probe("PDW")
        MPV = self.morphology.get_probe("MPV")

        for_women = self.morphology.show_data_limits_for_women()

        self.draw(ax1, PLT.get_samples(), PLT.get_limits(for_women), PLT.get_name(), PLT.get_unit(), self.morphology.dates)
        self.draw(ax2, PDW.get_samples(), PDW.get_limits(for_women), PDW.get_name(), PDW.get_unit(), self.morphology.dates)
        self.draw(ax3, MPV.get_samples(), MPV.get_limits(for_women), MPV.get_name(), MPV.get_unit(), self.morphology.dates)

        f.suptitle(u"%s\n%s\n%s" % (PLT, PDW, MPV), fontsize=12, fontweight="bold")
        f.subplots_adjust(hspace=0.1)
        fig = plt.gcf()
        fig.set_size_inches(8, 8)

        self.output(plt, title)

    def draw_leukocytes_and_plasma(self):
        f, (ax1, ax2) = plt.subplots(2, sharex=True)

        title = u"Leukocyty i osocze"

        WBC = self.morphology.get_probe("WBC")
        PCT = self.morphology.get_probe("PCT")

        for_women = self.morphology.show_data_limits_for_women()

        self.draw(ax1, WBC.get_samples(), WBC.get_limits(for_women), WBC.get_name(), WBC.get_unit(), self.morphology.dates)
        self.draw(ax2, PCT.get_samples(), PCT.get_limits(for_women), PCT.get_name(), PCT.get_unit(), self.morphology.dates)

        f.suptitle(u"%s\n%s" % (WBC, PCT), fontsize=12, fontweight="bold")
        f.subplots_adjust(hspace=0.1)
        fig = plt.gcf()
        fig.set_size_inches(8, 8)

        self.output(plt, title)
