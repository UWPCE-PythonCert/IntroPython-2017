#!/usr/bin/env python3

import os
import sys
import pytest
from windrevenue.electricity_pricing import ElectricityPricing

dirname = os.path.dirname(sys.modules["windrevenue"].__file__)
sample_data = os.path.join(dirname, "sample_data")
price_file = os.path.join(sample_data, "sample_pricing.txt")
price_file2 = os.path.join(sample_data, "sample_pricing2.txt")


@pytest.fixture
def sample_data():
    price = ElectricityPricing(fname=price_file)
    return price


class TestPricing():

    def test_data_length(self, sample_data):
        assert len(sample_data.powerdf) == 9717

    def test_data_nonans(self, sample_data):
        q = sample_data.get_pricing_field().isna().sum()
        assert q.sum() == 0


