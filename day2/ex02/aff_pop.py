from load_csv import load
from matplotlib import pyplot as plt
import numpy as np


def to_int(data: list[str]) -> list[int]:
    ret = []
    for elem in data:
        if elem[-1] == 'k':
            ret.append(int(float(elem[:-1])*1000))
        elif elem[-1] == 'M':
            ret.append(int(float(elem[:-1])*1000000))
        elif elem[-1] == 'B':
            ret.append(int(float(elem[:-1])*1000000000))
    return ret


def main():
    data = load("../population_total.csv")
    armenia_data = data[data['country'] == 'Armenia']
    albania_data = data[data['country'] == 'Nigeria']
    years = np.array(armenia_data.columns[1:251], dtype=int)
    armenia_population = np.array(armenia_data.values[0][1:251])
    armenia_population = to_int(armenia_population)
    albania_population = np.array(albania_data.values[0][1:251])
    albania_population = to_int(albania_population)
    plt.title('Population Projections')
    plt.plot(years, armenia_population, 'r', label='Armenia')
    plt.plot(years, albania_population, 'g', label='Albania')
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(np.arange(1800, 2051, 40))
    plt.show()


if __name__ == "__main__":
    main()
