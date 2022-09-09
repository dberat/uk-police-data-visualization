import csv
import matplotlib.pyplot as plt
import numpy as np


def genders_chart(data):
    """This function creates a pie chart of
     gender distribution of the people who were subjected to
     stop and search in London between June 2021-June 2022."""

    # Opening and reading the .csv file.
    csv_file = open(data)
    csvreader = csv.reader(csv_file)

    # Cleaning the unwanted data
    # Creating a dictionary of outcomes of stop and searches and adding their numbers
    gender_count = {}
    for row in csvreader:
        if row[6] != "Gender" and row[6] != "":
            if not row[6] in list(gender_count.keys()):
                gender_count[row[6]] = 1
            else:
                gender_count[row[6]] += 1

    # Assigning labels and values for the pie chart.
    genders = list(gender_count.keys())
    gender_numbers = np.array(list(gender_count.values()))

    # Adding the percentage of the outcomes next to each label.
    genders_percentage = [f'{number} {gender}, {(number * 100) / sum(gender_numbers):0.1f}%'
                          for gender, number in zip(genders, gender_numbers)]

    # Drawing the chart, adding the title and the legend.
    plt.pie(gender_numbers, labels=genders_percentage, rotatelabels=False)
    plt.title("Gender Distribution of People who were\nsubjected to "
              "Stop and Searches in London\n(June 2021 - June 2022)",
              fontdict={'fontsize': 12})
    plt.legend(loc='lower right', bbox_to_anchor=(0.32, 0))

    # Saving the chart and displaying it.
    plt.savefig("Genders_pie_chart.png", bbox_inches='tight')
    plt.show()
