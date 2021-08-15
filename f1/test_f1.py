import pytest
from .f1 import F1, LapTime

f = F1()
d1 = f.drivers_standings[0]
t1 = f.teams_standings[0]
d2 = f.drivers_standings[1]
t2 = f.teams_standings[1]
l1 = LapTime('XD', 'Siema', 'Witam', '1.30.20')
l2 = LapTime('Dx', 'SiemaEMA', 'Witam!!!', '1.20.20')
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


def test_current_fastest():
    assert f.fastest_laps
    assert len(f.fastest_laps) > 0


def test_current_drivers():
    assert f.drivers_standings
    assert len(f.drivers_standings) > 0


def test_current_teams():
    assert f.teams_standings
    assert len(f.teams_standings) > 0


def test_len():
    assert len(f) == len(f.drivers_standings)


def test_side_functionalities_driver():
    assert d1 > d2
    assert not d1 < d2
    assert d1 >= d2
    assert not d1 <= d2
    assert type(d1.__str__()) is str


def test_side_functionalities_teams():
    assert t1 > t2
    assert not t1 < t2
    assert t1 >= t2
    assert not t1 <= t2
    assert type(t1.__str__()) is str


def test_side_functionalities_laps():
    assert l1 > l2
    assert not l1 < l2
    assert l1 >= l2
    assert not l1 <= l2
    assert type(l1.__str__()) is str


def test_conversion_driver():
    assert d1.as_pickle()
    assert d1.as_dict()
    assert d1.as_yaml()
    assert d1.as_json()


def test_conversion_lap():
    assert l1.as_pickle()
    assert l1.as_dict()
    assert l1.as_yaml()
    assert l1.as_json()


def test_conversion_team():
    assert t1.as_pickle()
    assert t1.as_dict()
    assert t1.as_yaml()
    assert t1.as_json()


def test_exceptions():
    with pytest.raises(ValueError):
        f.get_fastest_laps(20202)
        f.get_teams(2020202)
        f.get_drivers_by_year(202020)

