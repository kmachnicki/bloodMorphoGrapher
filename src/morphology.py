# -*- coding:utf-8 -*-

from sys import exit
from csv import DictReader
from probe import Probe

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
