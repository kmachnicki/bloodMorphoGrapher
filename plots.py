# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

from sys import exit
from csv import DictReader
from matplotlib import rcParams
from argparse import ArgumentParser

rcParams["font.family"] = "Liberation Sans"
rcParams["font.sans-serif"] = ["Liberation Sans"]
rcParams["text.latex.unicode"] = True
plt.style.use("classic")

class Probe(object):
    def __init__(self, name, unit, limits_men, limits_women, description):
        self.name = name
        self.unit = unit
        self.limits_men = limits_men
        self.limits_women = limits_women
        self.description = description
        self.samples = []

    def get_name(self):
        return self.name

    def get_unit(self):
        return self.unit

    def get_limits(self, for_women):
        if for_women is True:
            return self.limits_women
        return self.limits_men

    def get_limits_men(self):
        return self.limits_men

    def get_samples(self):
        return self.samples

    def add_sample(self, sample):
        self.samples.append(sample)

    def __str__(self):
        return u"%s - %s" % (self.name, self.description)

    def __repr__(self):
        return u"%s: %s-%s %s - %s" % (self.name, str(self.limits[0]), str(self.limits[1]), self.unit, self.description)

    def __eq__(self, other):
        return self.name == other.name

class Morphology(object):
    def __init__(self, data_limits_for_women):
        self.data_limits_for_women = data_limits_for_women
        self.dates = []
        self.probes = {
            "RBC": Probe("RBC", "[mln/µl]", [4.5, 5.9], [4.2, 5.4], u"Ilość czerwonych krwinek (erytrocytów)"),
            "HGB": Probe("HGB", "[g/dl]", [13.5, 18.5], [12, 16], u"Ilość hemoglobiny w ogólnej masie erytrocytów"),
            "HCT": Probe("HCT", "[%]", [40, 54], [40, 51], u"Hematokryt - procentowa objętość erytrocytów we krwi"),
            "MCV": Probe("MCV", "[fl]", [76, 102.9], [76, 102.9], u"Średnia objętość erytrocytu"),
            "MCH": Probe("MCH", "[pg]", [25.7, 35.7], [25.7, 35.7], u"Stężenie hemoglobiny w erytrocycie"),
            "MCHC": Probe("MCHC", "[g/dl]", [29.5, 38.8], [29.5, 38.8], u"Stężenie hemoglobiny w ogólnej masie erytrocytów"),
            "RDW": Probe("RDW", "[%]", [10.3, 15.9], [10.3, 15.9], u"Anizocytoza erytrocytów - rozpiętość rozkładu objętości erytrocytów"),
            "PLT": Probe("PLT", "[tys/µl]", [135, 495], [135, 495], u"Ilość płytek krwi (trombocytów)"),
            "PDW": Probe("PDW", "[%]", [11, 18], [11, 18], u"Anizocytoza trombocytów - rozpiętość rozkładu objętości trombocytów"),
            "MPV": Probe("MPV", "[fl]", [6, 11], [6, 11], u"Średnia objętość trombocytu"),
            "WBC": Probe("WBC", "[tys/µl]", [3.8, 10.5], [3.8, 10.5], u"Ilość białych krwinek (leukocytów)"),
            "PCT": Probe("PCT", "[%]", [0.2, 0.5], [0.2, 0.5], u"Poziom prokalcytoniny (białka tarczycy) w osoczu krwi"),
            }

    def get_probe(self, probe_name):
        return self.probes[probe_name]

    def get_probes_size(self):
        probes_size = []
        for probe in self.probes.values():
            probes_size.append(len(probe.get_samples()))
        return probes_size
        
    def show_data_limits_for_women(self):
        return self.data_limits_for_women

    def is_data_complete(self):
        return all(probe_size == len(self.dates) for probe_size in self.get_probes_size())

    def is_data_empty(self):
        return len(self.dates) == 0

    def file_not_found_error(self, filename):
        print("File %s not found. Will now exit." % filename)
        exit()

    def incomplete_data_error(self, filename):
        print("File %s contains incomplete data - either uneven number of probes or missing some parameter.\n"
            "Please check if it contains even number of probes for every parameter." % filename)
        exit()

    def empty_data_error(self, filename):
        print("File %s seems to be empty or is missing a header row with parameters' name" % filename)
        exit()

    def read_data(self, filename):
        try:
            with open(filename, "r", newline="", encoding="utf8") as csv_file:
                reader = DictReader(csv_file, delimiter=";")
                for row in reader:
                    for (key, val) in row.items():
                        if key == "date":
                            self.dates.append(val)
                        elif key in self.probes:
                            self.probes.get(key).add_sample(float(val))
            if self.is_data_empty():
                self.empty_data_error(filename)
            if not self.is_data_complete():
                self.incomplete_data_error(filename)
        except (OSError, IOError):
            self.file_not_found_error(filename)
        except TypeError:
            self.incomplete_data_error(filename)

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
        plt.savefig(u"%s.pdf" % (filename), bbox_inches="tight")

def draw_first_part_of_erythrocytes(morphology, show_only):
    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)

    title = u"Czerwone krwinki 1"

    RBC = morphology.get_probe("RBC")
    HGB = morphology.get_probe("HGB")
    HCT = morphology.get_probe("HCT")

    for_women = morphology.show_data_limits_for_women()
    
    draw(ax1, RBC.get_samples(), RBC.get_limits(for_women), RBC.get_name(), RBC.get_unit(), morphology.dates)
    draw(ax2, HGB.get_samples(), HGB.get_limits(for_women), HGB.get_name(), HGB.get_unit(), morphology.dates)
    draw(ax3, HCT.get_samples(), HCT.get_limits(for_women), HCT.get_name(), HCT.get_unit(), morphology.dates)

    f.suptitle(u"%s\n%s\n%s" % (RBC, HGB, HCT), fontsize=12, fontweight="bold")
    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)

    output(plt, show_only, title)

def draw_second_part_of_erythrocytes(morphology, show_only):
    f, (ax1, ax2) = plt.subplots(2, sharex=True)

    title = u"Czerwone krwinki 2"

    MCV = morphology.get_probe("MCV")
    MCH = morphology.get_probe("MCH")

    for_women = morphology.show_data_limits_for_women()
    
    draw(ax1, MCV.get_samples(), MCV.get_limits(for_women), MCV.get_name(), MCV.get_unit(), morphology.dates)
    draw(ax2, MCH.get_samples(), MCH.get_limits(for_women), MCH.get_name(), MCH.get_unit(), morphology.dates)

    f.suptitle(u"%s\n%s" % (MCV, MCH), fontsize=12, fontweight="bold")
    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)

    output(plt, show_only, title)

def draw_third_part_of_erythrocytes(morphology, show_only):
    f, (ax1, ax2) = plt.subplots(2, sharex=True)

    title = u"Czerwone krwinki 3"

    MCHC = morphology.get_probe("MCHC")
    RDW = morphology.get_probe("RDW")

    for_women = morphology.show_data_limits_for_women()
    
    draw(ax1, MCHC.get_samples(), MCHC.get_limits(for_women), MCHC.get_name(), MCHC.get_unit(), morphology.dates)
    draw(ax2, RDW.get_samples(), RDW.get_limits(for_women), RDW.get_name(), RDW.get_unit(), morphology.dates)

    f.suptitle(u"%s\n%s" % (MCHC, RDW), fontsize=12, fontweight="bold")
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

    for_women = morphology.show_data_limits_for_women()
    
    draw(ax1, PLT.get_samples(), PLT.get_limits(for_women), PLT.get_name(), PLT.get_unit(), morphology.dates)
    draw(ax2, PDW.get_samples(), PDW.get_limits(for_women), PDW.get_name(), PDW.get_unit(), morphology.dates)
    draw(ax3, MPV.get_samples(), MPV.get_limits(for_women), MPV.get_name(), MPV.get_unit(), morphology.dates)

    f.suptitle(u"%s\n%s\n%s" % (PLT, PDW, MPV), fontsize=12, fontweight="bold")
    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)

    output(plt, show_only, title)

def draw_leukocytes_and_plasma(morphology, show_only):
    f, (ax1, ax2) = plt.subplots(2, sharex=True)

    title = u"Leukocyty i osocze"

    WBC = morphology.get_probe("WBC")
    PCT = morphology.get_probe("PCT")

    for_women = morphology.show_data_limits_for_women()
    
    draw(ax1, WBC.get_samples(), WBC.get_limits(for_women), WBC.get_name(), WBC.get_unit(), morphology.dates)
    draw(ax2, PCT.get_samples(), PCT.get_limits(for_women), PCT.get_name(), PCT.get_unit(), morphology.dates)

    f.suptitle(u"%s\n%s" % (WBC, PCT), fontsize=12, fontweight="bold")
    f.subplots_adjust(hspace=0.1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)

    output(plt, show_only, title)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", type=str, required=False, help="Input data csv filename")
    parser.add_argument("-s", action="store_true", required=False, help="Show data without saving")
    parser.add_argument("-k", action="store_true", required=False, help="Draw normal values for women instead of men")
    args = parser.parse_args()

    if args.f is not None:
        input_filename = args.f
    else:
        input_filename = "./data.csv"

    show_only = args.s
    data_limits_for_women = args.k

    morphology = Morphology(data_limits_for_women)
    morphology.read_data(input_filename)
    draw_first_part_of_erythrocytes(morphology, show_only)
    draw_second_part_of_erythrocytes(morphology, show_only)
    draw_third_part_of_erythrocytes(morphology, show_only)
    draw_thrombocytes(morphology, show_only)
    draw_leukocytes_and_plasma(morphology, show_only)
