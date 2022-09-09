import csv
import matplotlib.pyplot as plt
import numpy as np


def age_chart(data):
    """This function creates a pie chart of
         age range of the people who were subjected to
         stop and search in London between June 2021-June 2022."""

    # Opening and reading the .csv file.
    csv_file = open(data)
    csvreader = csv.reader(csv_file)

    # Cleaning the unwanted data
    # Creating a dictionary of outcomes of stop and searches and adding their numbers
    age_count = {}
    for row in csvreader:
        if row[7] != "Age range" and row[7] != "":
            if not row[7] in list(age_count.keys()):
                age_count[row[7]] = 1
            else:
                age_count[row[7]] += 1

    # Assigning labels and values for the pie chart.
    age_labels = list(age_count.keys())
    age_range_numbers = np.array(list(age_count.values()))

    # Adding the percentage of the outcomes next to each label.
    age_labels_perc = [f'Age Range: {age}, {number} people, {(number * 100) / sum(age_range_numbers):0.1f}%'
                       for age, number in zip(age_labels, age_range_numbers)]

    # Drawing the chart, adding the title and the legend.
    plt.pie(age_range_numbers, labels=age_labels_perc, rotatelabels=False)
    plt.title("Age Range of the People who were subjected to Stop and Searches in London\n(June 2021 - June 2022)",
              fontdict={'fontsize': 12})
    plt.legend(loc='lower right', bbox_to_anchor=(0.32, 0))

    # Saving the chart and displaying it.
    plt.savefig("Age_ranges_pie_chart.png", bbox_inches='tight')
    plt.show()
