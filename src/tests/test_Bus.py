import pytest
from src.templates.Bus import Bus

@pytest.mark.parametrize("bus_id, bus_line, last_register, position, expected", [
    (None, None, None, None, (None, None, None, None)),
    ("", "", "", "", ("", "", "", "")),
    (82485, 8012, "2022-09-29T01:36:51Z", (-46.7398505, -23.5683355), (82485, 8012, "2022-09-29T01:36:51Z", (-46.7398505, -23.5683355)))
])
def test_bus(bus_id, bus_line, last_register, position, expected):
    bus = Bus(bus_id, bus_line, last_register, position)
    assert bus.bus_id == expected[0]
    assert bus.bus_line == expected[1]
    assert bus.last_register == expected[2]
    assert bus.position == expected[3]

