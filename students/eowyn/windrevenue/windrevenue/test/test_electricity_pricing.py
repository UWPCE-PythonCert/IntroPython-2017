#!/usr/bin/env python3

import os
import pytest
import pandas as pd
from windrevenue.electricity_pricing import ElectricityPricing

@pytest.fixture
def sample_data():
    fname=os.path.abspath("sample_data/sample_pricing.txt")
    price = ElectricityPricing(fname=fname)
    return price

class TestPricing():

    def test_data_length(self, sample_data):
        assert len(sample_data.powerdf) == 9717

    def test_data_nonans(self, sample_data):
        q = sample_data.get_pricing_field().isna().sum()
        assert q.sum() == 0



