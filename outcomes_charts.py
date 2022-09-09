import csv
import matplotlib.pyplot as plt
import numpy as np


def pie_chart(data):
    """This function creates a pie chart
    out of outcomes of stop and searches in London
    between June 2021-June 2022."""

    # Opening and reading the .csv file.
    csv_file = open(data)
    csvreader = csv.reader(csv_file)

    # Cleaning the unwanted data
    # Creating a dictionary of outcomes of stop and searches and adding their numbers
    outcome_count = {}
    for row in csvreader:
        if row[12] != "Outcome":
            if not row[12] in list(outcome_count.keys()):
                outcome_count[row[12]] = 0
            else:
                outcome_count[row[12]] += 1

    # Assigning labels and values for the pie chart.
    outcome_labels = list(outcome_count.keys())
    outcome_numbers = np.array(list(outcome_count.values()))

    # Adding the percentage of the outcomes next to each label.
    labels_percentage = [f'{outcome}, {(number * 100) / sum(outcome_numbers):0.1f}%'
                         for outcome, number in zip(outcome_labels, outcome_numbers)]

    # Exploding the labels in order to improve readability of the labels that have fewer values.
    my_explode = [0.1, 0.1, 0.1, 0.6, 0.6, 0.6, 0.6]

    # Drawing the chart, adding the title and the legend.
    plt.pie(outcome_numbers, labels=labels_percentage, explode=my_explode, rotatelabels=True)
    plt.title("Outcomes of Stop and Searches in London\n(June 2021 - June 2022)", fontdict={'fontsize': 12})
    plt.legend(loc='lower right', bbox_to_anchor=(0.32, 0))

    # Saving the chart and displaying it.
    plt.savefig("Outcomes_pie_chart.png", bbox_inches='tight')
    plt.show()


def bar_chart(data):
    """This function creates a bar chart
        out of outcomes of stop and searches in London
        between June 2021-June 2022."""

    # Opening and reading the .csv file.
    csv_file = open(data)
    csvreader = csv.reader(csv_file)

    # Cleaning the unwanted data and adding new line to improve readability.
    # Creating a dictionary of outcomes of stop and searches and adding their numbers
    outcome_count = {}
    for row in csvreader:
        if row[12] != "Outcome":
            x = row[12].split(" ")
            if len(x) > 2:
                x.insert(2, "\n")
                row[12] = " ".join(x)
            if not row[12] in list(outcome_count.keys()):
                outcome_count[row[12]] = 1
            else:
                outcome_count[row[12]] += 1

    # Assigning labels and values for the chart.
    outcome_labels = list(outcome_count.keys())
    outcome_numbers = np.array(list(outcome_count.values()))

    # Rotating the labels in order to improve readability.
    plt.xticks(rotation=60)

    # Drawing the chart and adding the title.
    graph = plt.bar(outcome_labels, outcome_numbers, align='center', alpha=0.5)
    plt.title("Numbers and Percentage of the Outcomes of Stop and Searches in London\n(June 2021 - June 2022)",
              fontdict={'fontsize': 12})

    # Calculating and adding the percentage on the top of each bar.
    percentage = [f"{(number * 100) / sum(outcome_numbers):0.1f}%" for number in outcome_numbers]
    c = 0
    for bar in graph:
        width = bar.get_width()     # Getting the width of every bar
        height = bar.get_height()   # Getting the height of every bar
        x, y = bar.get_xy()     # Getting the X and Y coordinates of lower left point of every bar
        plt.text(x + width / 2,     # Adjusting the location, content and features of the text
                 y + height * 1.01,
                 f"{height}-{percentage[c]}",
                 ha='center',
                 weight='bold')
        c += 1

    # Saving the chart and displaying it.
    plt.savefig("Outcomes_bar_chart.png", bbox_inches='tight')
    plt.show()


def scatter(data):
    """This function creates scatter plots
            out of outcomes of stop and searches in London
            between June 2021-June 2022."""

    # Opening and reading the .csv file.
    csv_file = open(data)
    csvreader = csv.reader(csv_file)

    # Cleaning the unwanted data and adding new line to improve readability.
    # Creating a dictionary of outcomes of stop and searches and adding their numbers
    outcome_count = {}
    for row in csvreader:
        if row[12] != "Outcome":
            x = row[12].split(" ")
            if len(x) > 2:
                x.insert(2, "\n")
                row[12] = " ".join(x)
            if not row[12] in list(outcome_count.keys()):
                outcome_count[row[12]] = 1
            else:
                outcome_count[row[12]] += 1

    # Assigning labels and values for the chart.
    outcome_labels = list(outcome_count.keys())
    outcome_numbers = np.array(list(outcome_count.values()))

    # Drawing the chart, rotating the labels and adding the title.
    plt.scatter(outcome_labels, outcome_numbers)
    plt.xticks(rotation=60)
    plt.title("Outcomes of Stop and Searches in London\n(June 2021 - June 2022)")

    # Saving the chart and displaying it.
    plt.savefig("Outcomes_scatter_plots.png", bbox_inches='tight')
    plt.show()
