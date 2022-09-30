import data
import plot

estados = data.data_read("../data/states_incomplete.json")
plot.amount_buses_per_time(estados)