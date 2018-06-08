# -*- coding:utf-8 -*-

from argparse import ArgumentParser
from morphology import Morphology
from plots import Drawer

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

    drawer = Drawer(morphology, show_only)
    drawer.draw_plots()
