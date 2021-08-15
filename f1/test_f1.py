import pytest
from .f1 import F1

f = F1()
# print(f.)


def test_get_driver_year():
    assert len(f.get_drivers_by_year(2020)) > 0
    assert len(f.get_drivers_by_year(2017)) > 0


def test_get_fastest_laps():
    assert len(f.get_fastest_laps(2020)) > 0
    assert len(f.get_fastest_laps(2017)) > 0


def test_get_teams():
    assert len(f.get_teams(2020)) > 0
    assert len(f.get_teams(2017)) > 0


def test_exceptions():
    with pytest.raises(ValueError):
        f.get_fastest_laps(20202)
        f.get_teams(2020202)
        f.get_drivers_by_year(202020)
