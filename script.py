"""Code to look at Netflix Movie and Show rating trends"""

from lib import (
    load_data,
    generate_summary_stats,
    clean_ratings,
    years_and_ratings,
    years_ratings_trends,
    plot_trends,
)


def main():
    df = load_data("netflix_titles.csv")
    movies = df[df["type"] == "Movie"]
    shows = df[df["type"] == "TV Show"]
    generate_summary_stats("netflix_titles.csv")
    clean_ratings(df)
    print("Ratings types:", df["rating"].value_counts())
    movie_years_and_ratings = years_and_ratings(movies)
    print("Movie years and ratings:", movie_years_and_ratings)
    shows_years_and_ratings = years_and_ratings(shows)
    print("Shows years and ratings:", shows_years_and_ratings)
    movie_trends = years_ratings_trends(movies)
    shows_trends = years_ratings_trends(shows)
    plot_trends(movie_trends, "Movie")
    plot_trends(shows_trends, "Shows")
    return 1


if __name__ == "__main__":
    main()
