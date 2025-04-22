from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    Reads a JSON file containing reviews, analyzes sentiment, and creates a visualtization based on the results.

    Args:  
        filepath (str): Path to the JSON file containing reviews.

    Returns:
        list: A list of sentiment categories corresponding to each review.
    """

    filepath = "data/raw/reviews.json"
    with open(filepath) as file:
        r = json.load(file)

    
    reviews = r.get("results", [])

    
    sentiments = get_sentiment(reviews)


    make_plot(sentiments)

    return sentiments


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
