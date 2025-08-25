import logging
import pytest

@pytest.fixture(autouse=True)
def start_test():
    return "Testing started"

@pytest.fixture(autouse=True)
def end_test():
    return "Testing Ended"