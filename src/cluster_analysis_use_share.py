from src.cluster_analysis import ClusterAnalysis
from src.counter import Counter


class ClusterAnalysisUseShare(ClusterAnalysis):
    def get_d(self, fwci_average: float, proportion_list: list[float], value_so: int = 0) -> Counter:
        cluster_names = []
        cluster_fwci = []
        prominence_percentile = []
        cluster_proportion = []
        scholarly_output = []
        for i in range(len(self.topic_cluster)):
            if self.fwci[i] > fwci_average and proportion_list[i] > self.value:
                cluster_names.append(self.topic_cluster[i].replace('\n', ''))
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
            if self.fwci[i] < fwci_average and proportion_list[i] > self.value:
                cluster_names.append(self.topic_cluster[i].replace('\n', ''))
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
            if self.fwci[i] > fwci_average and proportion_list[i] < self.value:
                cluster_names.append(self.topic_cluster[i].replace('\n', ''))
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
            if self.fwci[i] < fwci_average and proportion_list[i] < self.value:
                cluster_names.append(self.topic_cluster[i].replace('\n', ''))
                cluster_fwci.append(self.fwci[i])
                prominence_percentile.append(self.prominence_percentile[i])
                cluster_proportion.append(proportion_list[i])
                scholarly_output.append(self.scholarly_output[i])
        if value_so != 0:
            scholarly_output = [value_so]
        return Counter(cluster_names, cluster_fwci, prominence_percentile, cluster_proportion, scholarly_output)