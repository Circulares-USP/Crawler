import pytest
from templates.State import State
from templates.Bus import Bus

@pytest.mark.parametrize("url, expected", [
    ("", []),
    (None, []),
    ("urlinvalida", []),
])
def test_request_api_state(url, expected):
    estado = State(url)
    assert estado.request_api_state(url) == expected

@pytest.mark.parametrize("dict, expected", [
    ([], []),
    ({}, []),
    ([{"cl": 0,"l": 0,"hr": "00:00","vs":[{"p":"","a":False,"ta":"","py": 0,"px": 0,}]}], [Bus("", 0, "", (0, 0))])
])
def test_create_vehicles(dict, expected):
    estado = State("")
    estado.create_vehicles(dict)
    if (len(estado.bus_list) == 0):
        assert estado.bus_list == expected
    else:
        for i in range(len(estado.bus_list)):
            bus = estado.bus_list[i]
            assert bus.bus_id == expected[i].bus_id
            assert bus.bus_line == expected[i].bus_line
            assert bus.last_register == expected[i].last_register
            assert bus.position == expected[i].position

@pytest.mark.parametrize("dict, expected", [
    ([], '{"data_register": , "buses": []}'),
    ([{"cl": 0,"l": 0,"hr": "00:00","vs":[{"p":"","a":False,"ta":"","py": 0,"px": 0,}]}], '{"data_register": , "buses": [{"bus_id": "", "bus_line": 0, "last_register": "", "position": [0, 0]}]}'),
    ([{'cl': 2023, 'l': 8012, 'hr': '21:29', 'vs': [{'p': '82498', 'a': True, 'ta': '2022-10-06T00:29:09Z', 'py': -23.568141, 'px': -46.7400545}, {'p': '82374', 'a': True, 'ta': '2022-10-06T00:28:57Z', 'py': -23.559725, 'px': -46.739392249999995}, {'p': '82512', 'a': True, 'ta': '2022-10-06T00:28:59Z', 'py': -23.568271, 'px': -46.739903}, {'p': '82490', 'a': True, 'ta': '2022-10-06T00:28:59Z', 'py': -23.5715955, 'px': -46.709297500000005}]}], '{"data_register": , "buses": [{"bus_id": "82498", "bus_line": 8012, "last_register": "2022-10-06T00:29:09Z", "position": [-46.7400545, -23.568141]},{"bus_id": "82374", "bus_line": 8012, "last_register": "2022-10-06T00:28:57Z", "position": [-46.739392249999995, -23.559725]},{"bus_id": "82512", "bus_line": 8012, "last_register": "2022-10-06T00:28:59Z", "position": [-46.739903, -23.568271]},{"bus_id": "82490", "bus_line": 8012, "last_register": "2022-10-06T00:28:59Z", "position": [-46.709297500000005, -23.5715955]}]}')
])
def test_dump_list(dict, expected):
    estado = State("")
    estado.create_vehicles(dict)
    output = estado.dump_list()
    output = output[:18] + output[40:]

    assert output == expected
