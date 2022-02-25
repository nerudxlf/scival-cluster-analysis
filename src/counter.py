class Counter:
    def __init__(
            self,
            cluster_names: list[str],
            cluster_fwci: list[float],
            prominence_percentile: list[float],
            cluster_proportion: list[float],
            scholarly_output: list[int],
    ):
        self.cluster_names: list[str] = cluster_names
        self.cluster_fwci: list[float] = cluster_fwci
        self.prominence_percentile: list[float] = prominence_percentile
        self.cluster_proportion: list[float] = cluster_proportion
        self.scholarly_output: list[int] = scholarly_output

    def get_average_value_fwci(self):
        return sum(self.cluster_fwci) / len(self.cluster_names)

    def get_value_clusters(self):
        return len(self.cluster_names)

    def get_average_prominence_percentile(self):
        return sum(self.prominence_percentile) / len(self.cluster_names)

    def get_average_scholarly_output(self):
        return sum(self.scholarly_output) / len(self.cluster_names)

    def __str__(self):
        return f"Average FWCI: {self.get_average_value_fwci()}\n" \
               f"Average Scholarly Output: {self.get_average_scholarly_output()}\n" \
               f"Total: {self.get_value_clusters()}\n" \
               f"Prominence percentile: {self.get_average_prominence_percentile()}\n"
