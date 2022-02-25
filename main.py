import pandas as pd
from pandas import DataFrame

from src.cluster_analysis import ClusterAnalysis
from src.counter import Counter


def main():
    df: DataFrame = pd.read_excel("data/scopus.xlsx")
    fwci: float = 1

    cl = ClusterAnalysis(df, fwci)
    avr_fwci = cl.get_average_fwci()
    proportion_list = cl.get_proportion()

    counter_d: Counter = cl.get_d(avr_fwci, proportion_list)
    counter_e: Counter = cl.get_e(avr_fwci, proportion_list)
    counter_g: Counter = cl.get_g(avr_fwci, proportion_list)
    counter_f: Counter = cl.get_f(avr_fwci, proportion_list)
    print(f"D\n{counter_d}")
    print(f"E\n{counter_e}")
    print(f"G\n{counter_g}")
    print(f"F\n{counter_f}")


