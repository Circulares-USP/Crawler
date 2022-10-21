import sys
import data
import plot

def main():
    if len(sys.argv) < 0:
        print("Usage:")
        print(f"\tpython main.py <funcao> <argumentos>")
    else:
        if sys.argv[1] == "plot":
            name_data = sys.argv[2]
            imgs_path = sys.argv[3]
            estados = data.data_read(name_data)
            plot.plot_buses(estados, imgs_path)
        elif sys.argv[1] == "crawl":
            name_data = sys.argv[2]
            time = sys.argv[3]
            interval = sys.argv[4]
            url = sys.argv[5]
            data.data_register(name_data, int(time), int(interval), url)

if __name__ == "__main__":
    main()
