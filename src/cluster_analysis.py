import pandas as pd
from pandas import DataFrame
import numpy as np

from src.counter import Counter


class ClusterAnalysis:
    def __init__(self, scopus_df: DataFrame, fwci: float, value: float):
        self.topic_cluster = scopus_df['Topic Cluster'].to_list()
        self.topic_cluster_number = scopus_df['Topic Cluster Number'].to_list()
        self.scholarly_output = list(map(int, scopus_df['Scholarly Output'].to_list()))
        self.fwci = list(map(float, scopus_df['Field-Weighted Citation Impact'].to_list()))
        self.prominence_percentile = list(map(float, scopus_df['Prominence percentile'].to_list()))
        self.fwci_university_value: float = fwci
        self.value: float = value

    def get_average_fwci(self) -> float:
        return sum(np.array(self.fwci) * np.array(self.scholarly_output)) / sum(self.scholarly_output)

    def get_proportion(self) -> list[float]:
        return list(np.array(self.scholarly_output) / sum(self.scholarly_output))

    def get_d(self, fwci_average: float, proportion_list: list[float], value_so: int = 0) -> Counter:
        pass

    def get_e(self, fwci_average: float, proportion_list: list[float], value_so: int = 0) -> Counter:
        pass

    def get_g(self, fwci_average: float, proportion_list: list[float], value_so: int = 0) -> Counter:
        pass

    def get_f(self, fwci_average: float, proportion_list: list[float], value_so: int = 0) -> Counter:
        pass
