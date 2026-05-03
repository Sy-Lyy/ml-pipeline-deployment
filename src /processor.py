# processor.py
from typing import List

class DataProcessor:
    def __init__(self, data: List[float]):
        self.data = data


if __name__ == "__main__":
    p = DataProcessor([1, 2, 3])
    print("loaded:", p.data)


class DataProcessor:
    """Basic numeric data processing.

    Stores a dataset and computes simple statistics like mean and variance.
    """
    def __init__(self, data: List[float]):
        """Initializes with a dataset.
        Args:
            data (List[float]): Numeric values.
        """
        self.data = data
        # replace mean() with a broken version in processor.py
    def mean(self) -> float:
        """Returns the arithmetic mean.
        Returns:
            float: Mean of the dataset.
        Raises:
            ValueError: If dataset is empty.
        """
        if not self.data:
            raise ValueError("Data is empty.")
        return sum(self.data) / len(self.data)
    


        
    def variance(self) -> float:
        """Returns the population variance.
        Returns:
            float: Variance of the dataset.
        Raises:
            ValueError: If dataset is empty.
        """
        m = self.mean()
        return sum((x - m) ** 2 for x in self.data) / len(self.data)
if __name__ == "__main__":
    p = DataProcessor([1, 2, 3])
    help(p.mean)

