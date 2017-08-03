import pytest
from simple import mean


class TestMean():
    def test_basic(self):
        assert mean(4, 5) == 4.5

    def test_floats(self):
        assert mean(4.0, 5.0) == 4.5

    def test_one_number(self):
        assert mean(4.0) == 4.0

    def test_none(self):
        with pytest.raises(Exception) as e_info:
            mean()
