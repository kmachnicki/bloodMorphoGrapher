# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

from csv import DictReader
from matplotlib import rcParams

rcParams["font.family"] = "Liberation Sans"
rcParams["font.sans-serif"] = ["Liberation Sans"]
rcParams["text.latex.unicode"] = True
plt.style.use("classic")

class Probe(object):
    def __init__(self, data_name, data_unit, data_limits, data_description):
        self.data_name = data_name
        self.data_unit = data_unit
        self.data_limits = data_limits
        self.data_description = data_description
        self.data_samples = []

    def add_data_sample(self, data_sample):
        self.data_samples.append(data_sample)

    def __str__(self):
        return u"%s - %s" % (self.data_name, self.data_description)

    def __repr__(self):
        return u"%s: %s-%s %s - %s" % (self.data_name, str(self.data_limits[0]), str(self.data_limits[1]),
            self.data_unit, self.data_description)

    def __eq__(self, other):
        return self.data_name == other.data_name

class Morphology(object):
    def __init__(self):
        self.dates = []
        self.probes = {
            "RBC": Probe("RBC", "[mln/µl]", [4.5, 5.9], u"Ilość czerwonych krwinek (erytrocytów)"),
            "HGB": Probe("HGB", "[g/dl]", [13.5, 18.5], u"Ilość hemoglobiny w ogólnej masie erytrocytów"),
            "HCT": Probe("HCT", "[%]", [40, 54], u"Hematokryt - procentowa objętość erytrocytów we krwi"),
            "MCV": Probe("MCV", "[fl]", [76, 102.9], u"Średnia objętość erytrocytu"),
            "MCH": Probe("MCH", "[pg]", [25.7, 35.7], u"Stężenie hemoglobiny w erytrocycie"),
            "MCHC": Probe("MCHC", "[g/dl]", [29.5, 38.8], u"Stężenie hemoglobiny w ogólnej masie erytrocytów"),
            "RDW": Probe("RDW", "[%]", [10.3, 15.9], u"Anizocytoza erytrocytów - rozpiętość rozkładu objętości erytrocytów"),
            "PLT": Probe("PLT", "[tys/µl]", [135, 495], u"Ilość płytek krwi (trombocytów)"),
            "PDW": Probe("PDW", "[%]", [11, 18], u"Anizocytoza trombocytów - rozpiętość rozkładu objętości trombocytów"),
            "MPV": Probe("MPV", "[fl]", [6, 11], u"Średnia objętość trombocytu"),
            "WBC": Probe("WBC", "[tys/µl]", [3.8, 10.5], u"Ilość białych krwinek (leukocytów)"),
            "PCT": Probe("PCT", "[%]", [0.2, 0.5], u"Poziom prokalcytoniny (białka tarczycy) w osoczu krwi"),
            }

    def get_probe(self, probe_name):
        return self.probes[probe_name]

    def read_data(self, filename):
        with open(filename, "r", newline="", encoding="utf8") as csv_file:
            reader = DictReader(csv_file, delimiter=';')
            for row in reader:
                for (key, val) in row.items():
                    if key == "dates":
                        self.dates.append(val)
                    elif key in self.probes:
                        self.probes.get(key).add_data_sample(float(val))

def draw(ax, data, data_limits, ylabel, unit, labels, title=None):
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

def draw_first_part_of_erythrocytes(morphology, show_only):
    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)

    title = u"Czerwone krwinki 1"

    RBC = morphology.get_probe("RBC")
    HGB = morphology.get_probe("HGB")
    HCT = morphology.get_probe("HCT")

    draw(ax1, RBC.data_samples, RBC.data_limits, RBC.data_name, RBC.data_unit, morphology.dates)
    draw(ax2, HGB.data_samples, HGB.data_limits, HGB.data_name, HGB.data_unit, morphology.dates)
    draw(ax3, HCT.data_samples, HCT.data_limits, HCT.data_name, HCT.data_unit, morphology.dates)

    f.suptitle(u"%s\n%s\n%s" % (RBC, HGB, HCT), fontsize=12, fontweight='bold')
    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)

    output(plt, show_only, title)

def draw_second_part_of_erythrocytes(morphology, show_only):
    f, (ax1, ax2) = plt.subplots(2, sharex=True)

    title = u"Czerwone krwinki 2"

    MCV = morphology.get_probe("MCV")
    MCH = morphology.get_probe("MCH")

    draw(ax1, MCV.data_samples, MCV.data_limits, MCV.data_name, MCV.data_unit, morphology.dates)
    draw(ax2, MCH.data_samples, MCH.data_limits, MCH.data_name, MCH.data_unit, morphology.dates)

    f.suptitle(u"%s\n%s" % (MCV, MCH), fontsize=12, fontweight='bold')
    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)

    output(plt, show_only, title)

def draw_third_part_of_erythrocytes(morphology, show_only):
    f, (ax1, ax2) = plt.subplots(2, sharex=True)

    title = u"Czerwone krwinki 3"

    MCHC = morphology.get_probe("MCHC")
    RDW = morphology.get_probe("RDW")

    draw(ax1, MCHC.data_samples, MCHC.data_limits, MCHC.data_name, MCHC.data_unit, morphology.dates)
    draw(ax2, RDW.data_samples, RDW.data_limits, RDW.data_name, RDW.data_unit, morphology.dates)

    f.suptitle(u"%s\n%s" % (MCHC, RDW), fontsize=12, fontweight='bold')
    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)

    output(plt, show_only, title)

def draw_thrombocytes(morphology, show_only):
    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)

    title = u"Płytki krwi"

    PLT = morphology.get_probe("PLT")
    PDW = morphology.get_probe("PDW")
    MPV = morphology.get_probe("MPV")

    draw(ax1, PLT.data_samples, PLT.data_limits, PLT.data_name, PLT.data_unit, morphology.dates)
    draw(ax2, PDW.data_samples, PDW.data_limits, PDW.data_name, PDW.data_unit, morphology.dates)
    draw(ax3, MPV.data_samples, MPV.data_limits, MPV.data_name, MPV.data_unit, morphology.dates)

    f.suptitle(u"%s\n%s\n%s" % (PLT, PDW, MPV), fontsize=12, fontweight='bold')
    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)

    output(plt, show_only, title)

def draw_leukocytes_and_plasma(morphology, show_only):
    f, (ax1, ax2) = plt.subplots(2, sharex=True)

    title = u"Leukocyty i osocze"

    WBC = morphology.get_probe("WBC")
    PCT = morphology.get_probe("PCT")

    draw(ax1, WBC.data_samples, WBC.data_limits, WBC.data_name, WBC.data_unit, morphology.dates)
    draw(ax2, PCT.data_samples, PCT.data_limits, PCT.data_name, PCT.data_unit, morphology.dates)

    f.suptitle(u"%s\n%s" % (WBC, PCT), fontsize=12, fontweight='bold')
    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)

    output(plt, show_only, title)

if __name__ == "__main__":
    morphology = Morphology()
    input_filename = "./data.csv"
    morphology.read_data(input_filename)
    show_only = False
    draw_first_part_of_erythrocytes(morphology, show_only)
    draw_second_part_of_erythrocytes(morphology, show_only)
    draw_third_part_of_erythrocytes(morphology, show_only)
    draw_thrombocytes(morphology, show_only)
    draw_leukocytes_and_plasma(morphology, show_only)
