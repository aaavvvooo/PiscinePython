from load_csv import load
from matplotlib import pyplot as plt


def main():
    """Plot life expectancy vs income per person in 1900."""
    inc = load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("../life_expectancy_years.csv")
    year = '1900'
    inc_1900 = inc[year]
    life_1900 = life[year]
    plt.scatter(inc_1900, life_1900)
    plt.xlabel('Income per person')
    plt.ylabel('Life expectancy')
    plt.title('Income vs Life Expectancy in 1900')
    plt.xscale('log')
    plt.show()


if __name__ == "__main__":
    main()
