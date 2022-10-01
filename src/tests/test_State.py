import pytest
from templates.State import State
from templates.Bus import Bus

@pytest.mark.parametrize("url, expected", [
    ("", []),
    (None, []),
    ("https://mocki.io/v1/b6a9c774-c275-49db-afbd-6d4d83aee3a7", {}),
    ("https://mocki.io/v1/3bb24c78-69d8-40d4-9a18-c318dc76ef27", [{"cl": 2023, "l": 8012, "hr": "21:00", "vs": [{"p": "82449","a": True,"ta": "2022-09-30T23:59:31Z","py": -23.5611355,"px": -46.72562275}]}])

])
def test_request_api_state(url, expected):
    estado = State(url)
    assert estado.request_api_state(url) == expected

@pytest.mark.parametrize("dict, expected", [
    ([], []),
    ({}, []),
    ([{"cl": 0,"l": 0,"hr": "00:00","vs":[{"p":"","a":False,"ta":"","py": 0,"px": 0,}]}], [Bus("", 0,  "", (0, 0))])
])
def test_create_vehicles(dict, expected):
    estado = State("https://mocki.io/v1/b6a9c774-c275-49db-afbd-6d4d83aee3a7")
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