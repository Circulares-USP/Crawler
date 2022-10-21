import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as md

def fix_hour(date, offset):
    date_offset = datetime.timedelta(hours=offset)
    return date+date_offset

def amount_buses(states, line=None):
    """ Calcula a quantidade amount de ônibus por tempo dada a linha line """
    amount = []
    for state in states:
        list_buses = state["buses"]
        
        if line == "8012":
            list_buses = list(filter(lambda x: x["bus_line"] == 8012, list_buses))
        elif line == "8022":
            list_buses = list(filter(lambda x: x["bus_line"] == 8022, list_buses))
        elif line == "8032":
            list_buses = list(filter(lambda x: x["bus_line"] == 8032, list_buses))
                
        amount.append(len(list_buses))

    return amount

def times_register(states):
    """ Calcula os tempos de registro de cada estado """ 
    hours = []
    for state in states:
        register_time = datetime.datetime.strptime(state["data_register"], "%Y-%m-%dT%H:%M:%SZ")
        hours.append(register_time)
        
    for i in range(len(hours)):
        hours[i] = fix_hour(hours[i], -3)
        
    return hours

def plot_buses(states, imgs_path, category=None):   
    """ Plota os gráficos de dados dos ônibus de acordo com o conjunto de estados da API e a"
    categoria de gráfico correspondente """
    hours = times_register(states)
    amount_all = amount_buses(states)
    amount_c1 = amount_buses(states, "8012")
    amount_c2 = amount_buses(states, "8022")
    amount_c3 = amount_buses(states, "8032")
    
    fig, ax = plt.subplots(figsize=(12,8))
    
    if category == "8012":
        plt.plot(hours, amount_c1, color="red", label="Linha 8012")
        plt.yticks(range(0, max(amount_c1), 2))
    elif category == "8022":
        plt.plot(hours, amount_c2, color="green", label="Linha 8022")
        plt.yticks(range(0, max(amount_c2), 2))
    elif category == "8032":
        plt.plot(hours, amount_c3, color="blue", label="Linha 8032")
        plt.yticks(range(0, max(amount_c3), 2))
    else:
        plt.plot(hours, amount_c1, color="red", label="Linha 8012")
        plt.plot(hours, amount_c2, color="green", label="Linha 8022")
        plt.plot(hours, amount_c3, color="blue", label="Linha 8032")
        plt.plot(hours, amount_all, color="black", label="Todas as linhas")
        plt.yticks(range(0, max(amount_all), 2))
        plt.axhline(y=18, color="black", linestyle='--')
        
    ax.set_xlim(min(hours)-datetime.timedelta(hours=1),
                max(hours)+datetime.timedelta(hours=1))
    ax.legend(loc="upper right")

    ax.xaxis.set_major_locator(md.HourLocator(interval = 1))
    ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))

    fig.autofmt_xdate()

    now = datetime.datetime.now()
    name = now.strftime(str(category) + '-%Y-%m-%d-%H-%M-%S')
    plt.savefig(imgs_path + name + '.png')
