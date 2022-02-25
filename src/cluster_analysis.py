import pandas as pd
from pandas import DataFrame
import numpy as np

from src.counter import Counter


class ClusterAnalysis:
    def __init__(self, scopus_df: DataFrame, fwci: float):
        self.topic_cluster = scopus_df['Topic Cluster'].to_list()
        self.topic_cluster_number = scopus_df['Topic Cluster Number'].to_list()
        self.scholarly_output = list(map(int, scopus_df['Scholarly Output'].to_list()))
        self.publication_share = scopus_df['Publication share (%)'].to_list()
        self.publication_share_growth = scopus_df['Publication Share growth (%)'].to_list()
        self.fwci = list(map(float, scopus_df['Field-Weighted Citation Impact'].to_list()))
        self.prominence_percentile = list(map(float, scopus_df['Prominence percentile'].to_list()))
        self.fwci_university_value: float = fwci

    def get_average_fwci(self) -> float:
        return sum(np.array(self.fwci) * np.array(self.scholarly_output)) / sum(self.scholarly_output)

    def get_proportion(self) -> list[float]:
        return list(np.array(self.scholarly_output) / sum(self.scholarly_output))

    def get_d(self, fwci_average: float, proportion_list: list[float], value_so: int = 0) -> Counter:
        cluster_names = []
        cluster_fwci = []
        prominence_percentile = []
        cluster_proportion = []
        scholarly_output = []
        for i in range(len(self.topic_cluster)):
            if self.fwci[i] > fwci_average and proportion_list[i] > 0.005:
                cluster_names.append(self.topic_cluster[i])
                cluster_fwci.append(self.fwci[i])
                prominence_percentile.append(self.prominence_percentile[i])
                cluster_proportion.append(proportion_list[i])
                scholarly_output.append((self.scholarly_output[i]))
        if value_so != 0:
            scholarly_output = [value_so]
        return Counter(cluster_names, cluster_fwci, prominence_percentile, cluster_proportion, scholarly_output)

    def get_e(self, fwci_average: float, proportion_list: list[float], value_so: int = 0) -> Counter:
        cluster_names = []
        cluster_fwci = []
        prominence_percentile = []
        cluster_proportion = []
        scholarly_output = []
        for i in range(len(self.topic_cluster)):
            if self.fwci[i] < fwci_average and proportion_list[i] > 0.005:
                cluster_names.append(self.topic_cluster[i])
                cluster_fwci.append(self.fwci[i])
                prominence_percentile.append(self.prominence_percentile[i])
                cluster_proportion.append(proportion_list[i])
                scholarly_output.append(self.scholarly_output[i])
        if value_so != 0:
            scholarly_output = [value_so]
        return Counter(cluster_names, cluster_fwci, prominence_percentile, cluster_proportion, scholarly_output)

    def get_g(self, fwci_average: float, proportion_list: list[float], value_so: int = 0) -> Counter:
        cluster_names = []
        cluster_fwci = []
        prominence_percentile = []
        cluster_proportion = []
        scholarly_output = []
        for i in range(len(self.topic_cluster)):
            if self.fwci[i] > fwci_average and proportion_list[i] < 0.005:
                cluster_names.append(self.topic_cluster[i])
                cluster_fwci.append(self.fwci[i])
                prominence_percentile.append(self.prominence_percentile[i])
                cluster_proportion.append(proportion_list[i])
                scholarly_output.append(self.scholarly_output[i])
        if value_so != 0:
            scholarly_output = [value_so]
        return Counter(cluster_names, cluster_fwci, prominence_percentile, cluster_proportion, scholarly_output)

    def get_f(self, fwci_average: float, proportion_list: list[float], value_so: int = 0) -> Counter:
        cluster_names = []
        cluster_fwci = []
        prominence_percentile = []
        cluster_proportion = []
        scholarly_output = []
        for i in range(len(self.topic_cluster)):
            if self.fwci[i] < fwci_average and proportion_list[i] < 0.005:
                cluster_names.append(self.topic_cluster[i])
                cluster_fwci.append(self.fwci[i])
                prominence_percentile.append(self.prominence_percentile[i])
                cluster_proportion.append(proportion_list[i])
                scholarly_output.append(self.scholarly_output[i])
        if value_so != 0:
            scholarly_output = [value_so]
        return Counter(cluster_names, cluster_fwci, prominence_percentile, cluster_proportion, scholarly_output)
