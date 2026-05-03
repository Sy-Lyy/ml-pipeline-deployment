# test_processor.py
from processor import DataProcessor
import math
import pytest

def test_mean_basic():
    p = DataProcessor([1, 2, 3, 4, 5])
    assert p.mean() == 3.0

def test_variance_basic():
    p = DataProcessor([1, 2, 3, 4, 5])
    assert math.isclose(p.variance(), 2.0, rel_tol=1e-9)
