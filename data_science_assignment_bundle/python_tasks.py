"""Data Science assignment examples.

Run with:
    python -m pip install requests pandas matplotlib
    python python_tasks.py

The API section needs an internet connection.
"""
from pathlib import Path
import requests
import pandas as pd
import matplotlib.pyplot as plt


def fetch_first_five_post_titles():
    """Fetch and print the first five posts returned by JSONPlaceholder."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    posts = response.json()
    print("\n--- First five JSONPlaceholder post titles ---")
    for post in posts[:5]:
        print(post["title"])


def count_songs_by_genre():
    """Load songs.csv and print the number of songs in each genre."""
    songs_path = Path(__file__).with_name("songs.csv")
    songs = pd.read_csv(songs_path)
    print("\n--- Number of songs in each genre ---")
    print(songs["genre"].value_counts())


def create_movie_genre_chart():
    """Create a bar chart for a small, simulated movie dataset."""
    movies = pd.DataFrame({
        "movie_name": [
            "Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5",
            "Movie 6", "Movie 7", "Movie 8", "Movie 9", "Movie 10"
        ],
        "genre": [
            "Action", "Comedy", "Drama", "Action", "Comedy",
            "Action", "Drama", "Comedy", "Action", "Drama"
        ],
    })
    counts = movies["genre"].value_counts()
    output_path = Path(__file__).with_name("plot.png")
    counts.plot(kind="bar")
    plt.title("Number of Movies per Genre")
    plt.xlabel("Genre")
    plt.ylabel("Number of Movies")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    print(f"\nSaved movie genre chart to: {output_path}")
    plt.show()


if __name__ == "__main__":
    try:
        fetch_first_five_post_titles()
    except requests.RequestException as exc:
        print(f"Could not reach JSONPlaceholder: {exc}")
    count_songs_by_genre()
    create_movie_genre_chart()
