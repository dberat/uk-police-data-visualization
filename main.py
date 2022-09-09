from src.outcomes_charts import pie_chart, bar_chart, scatter
from src.genders import genders_chart
from src.ages import age_chart

file_name = input("Please enter the name of the file you would like to visualize: ").lower()

while True:
    chart = input("""Which type of chart would you like to see?
(OP for Pie Chart of Outcomes
OS for Scatter Plots of Outcomes
OB for Bar Chart of Outcomes
AP for Pie Chart of Ages
GP for Pie Chart of Genders
E to Exit): """).lower()

    if chart == "op":
        pie_chart(file_name)
    elif chart == "os":
        scatter(file_name)
    elif chart == "ob":
        bar_chart(file_name)
    elif chart == "ap":
        age_chart(file_name)
    elif chart == "gp":
        genders_chart(file_name)
    elif chart == "e":
        print("See you next time.")
        break
    else:
        print("Please enter a valid chart type.")