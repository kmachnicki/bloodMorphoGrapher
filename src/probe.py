# -*- coding:utf-8 -*-

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
        return u"%s: %s-%s %s - %s" % (self.name, str(self.limits_men[0]), str(self.limits_men[1]),
                                       self.unit, self.description)

    def __eq__(self, other):
        return self.name == other.name
