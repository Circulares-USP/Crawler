import json
import datetime
import time
from templates.State import State

def data_register(duration_time, x, url):
    """ Dado um tempo duration_time em segundos, registra os dados de estados em um arquivo JSON
    a cada x segundos """
    
    now = datetime.datetime.now()
    duration = datetime.timedelta(seconds=duration_time)
    endtime = now + duration
    
    while datetime.datetime.now() <= endtime:
        curr_state = State(url)
        with open('data/states.json', 'a') as f:
            f.write(curr_state.dump_list() + '\n')
        time.sleep(x)

def data_read(file):
    """ Retorna uma lista de estados dado um arquivo file que os contenha no formato definido na função
    data_register """
    
    states = []
    with open(file, 'r') as f:
        for line in f.readlines():
            state = json.loads(line)
            states.append(state)
    return states

