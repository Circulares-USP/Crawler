import requests
import json
import datetime
from templates.Bus import Bus

class State:
    def __init__(self, url):
        self.bus_list = []
        self.data_register = datetime.datetime.now()
        
        dict_api_states = self.request_api_state(url)
        self.create_vehicles(dict_api_states)
        
    def request_api_state(self, url):
        """ A função tem o objetivo de realizar uma requisição a API de endereço url, 
        retornando um dicionário com o estado atual dos ônibus na universidade """
        
        try:
            s_dict = requests.get(url).text 
            dict = json.loads(s_dict)
        except Exception as e:
            dict = []
            print(e)
        
        return dict
    
    def create_vehicles(self, dict):
        for bus_line in dict:
            for bus in bus_line["vs"]:
                bus_position = (bus["px"], bus["py"])
                obj_bus = Bus(bus["p"], bus_line["l"], bus["ta"], bus_position)
                
                self.bus_list.append(obj_bus)
    
    def get_vehicles(self):
        return self.bus_list
    
    def dump_list(self):
        i = 0
        str = '{"data_register": "' + self.data_register.strftime("%Y-%m-%dT%H:%M:%SZ") + '", '
        str += '"buses": ['
        for bus in self.bus_list:
            str += json.dumps(vars(bus))
            if i < len(self.bus_list) - 1:
                str += ','
            i += 1
            
        return str + ']}'
