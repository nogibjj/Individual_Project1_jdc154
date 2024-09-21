import pandas as pd
import matplotlib.pyplot as plt


def load_data(filename):
    """load in your data"""
    data = pd.read_csv(filename)
    return data


def generate_summary_stats(filename):
    """Generate summary stats of data"""
    data = load_data(filename)
    return data.describe()


def clean_ratings(data):
    """Cleans up rating column of data"""
    data = data[data["rating"] != "74 min"]
    data = data[data["rating"] != "84 min"]
    data = data[data["rating"] != "66 min"]
    return data


def years_and_ratings(data):
    """Looks at the number of films released per rating"""
    return data.groupby(["rating"]).aggregate({"release_year": "mean"})


def years_ratings_trends(data):
    """Looks at number of films released per year with each rating"""
    return data.groupby(["release_year", "rating"]).size().unstack(fill_value=0)


def plot_trends(data, category):
    """Plots the number of films released per year with each rating"""
    data.plot.bar(
        stacked=True,
        figsize=(10, 6),
        ylabel="Count",
        xlabel="Year",
        title=f"{category} Ratings over the Years",
    )
    plt.show()
