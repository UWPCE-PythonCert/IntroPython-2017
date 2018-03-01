"""
conftest.py

This is a file that will automatically be read by pytest to find fixtures, etc.

It's a good place to put stuff that multiple test files need.
"""

import pytest
from mailroom import model, data_dir


@pytest.fixture
def sample_db():
    """
    creates a clean sample database for the tests to use
    """
    return model.DonorDB.load_from_file(data_dir / "sample_data.json")
