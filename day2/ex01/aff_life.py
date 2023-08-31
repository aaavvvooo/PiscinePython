from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load life expectancy data, filter for Armenia, and display a line graph.

    Loads the life expectancy dataset from a CSV file, filters the data for
    Armenia, and displays a line graph showing the life expectancy in Armenia
    over the years. The x-axis of the graph includes year labels from
    1800 to 2080, with every 40th year label displayed and rotated for clarity.
    The graph includes a title, axis labels, legend, and grid.
    """
    dataset = load("../life_expectancy_years.csv")
    armenia_data = dataset[dataset['country'] == 'Armenia']
    years = armenia_data.columns[1:]
    life_expectancy = armenia_data.values[0][1:]

    plt.plot(years, life_expectancy, label='Armenia')
    plt.title('Life Expectancy in Armenia Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.xticks(years[::40])
    plt.show()


if __name__ == "__main__":
    main()
