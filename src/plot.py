import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as md

def fix_hour(date, offset):
    date_offset = datetime.timedelta(hours=offset)
    return date+date_offset

def amount_buses_per_time(states, line=None):
    """ Calcula a quantidade amount de ônibus por tempo dada a linha line """
    amount = []
    hours = []
    for state in states:
        list_buses = state["buses"]
        register_time = datetime.datetime.strptime(state["data_register"], "%Y-%m-%dT%H:%M:%SZ")
        
        if line == "8012":
            list_buses = list(filter(lambda x: x["bus_line"] == 8012, list_buses))
        elif line == "8022":
            list_buses = list(filter(lambda x: x["bus_line"] == 8022, list_buses))
        elif line == "8032":
            list_buses = list(filter(lambda x: x["bus_line"] == 8032, list_buses))
                
        amount.append(len(list_buses))
        hours.append(register_time)
    
    for i in range(len(hours)):
        hours[i] = fix_hour(hours[i], -3)

    return (amount, hours)

def plot_buses(states, category=None):   
    """ Plota os gráficos de dados dos ônibus de acordo com o conjunto de estados da API e a"
    categoria de gráfico correspondente """
    if category == None:
        amount, hours = amount_buses_per_time(states)
        
        fig, ax = plt.subplots(figsize=(8,6))

        plt.plot(hours, amount)
        ax.set_xlim(min(hours)-datetime.timedelta(hours=1),
                    max(hours)+datetime.timedelta(hours=1))

        ax.xaxis.set_major_locator(md.HourLocator(interval = 1))
        ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))

        fig.autofmt_xdate()

        plt.show()