import pandas as pd
from pandas import DataFrame

from src.cluster_analysis import ClusterAnalysis
from src.cluster_analysis_use_scholarly_output import ClusterAnalysisUseScholarlyOutput
from src.cluster_analysis_use_share import ClusterAnalysisUseShare
from src.counter import Counter


def main():
    df: DataFrame = pd.read_excel("data/Германия.xlsx")
    fwci: float = 1
    # Для того, чтобы использовать долю используйте класс ClusterAnalysisUseShare
    # Для того, чтобы использовать количество публикаций используйте класс ClusterAnalysisScholarlyOutput

    cl = ClusterAnalysisUseShare(df, fwci, 0.0005)
    avr_fwci = cl.get_average_fwci()
    proportion_list = cl.get_proportion()

    counter_d: Counter = cl.get_d(fwci, proportion_list)
    counter_e: Counter = cl.get_e(fwci, proportion_list)
    counter_g: Counter = cl.get_g(fwci, proportion_list)
    counter_f: Counter = cl.get_f(fwci, proportion_list)
    print(f"A find\n{counter_d}")
    print(f"B find\n{counter_e}")
    print(f"C find\n{counter_g}")
    print(f"D find\n{counter_f}")


