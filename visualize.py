import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    Generates a bar chart to visualize the distribution of sentiments.

    Args:
        sentiments (list): A list of sentiment counts in the order [positive, negative, neutral, irrelevant].

    Returns:
        None
    """
    if not isinstance(sentiments, list) or not all(isinstance(item, str) for item in sentiments):
        return "Input must be a list of strings representing sentiment counts."

    labels = ["positive", "negative", "neutral", "irrelevant"]
    
    counts = [sentiments.count(label) for label in labels]
    
    

    fig, ax = plt.subplots()

    ax.bar(labels, counts)
    ax.set_title("Sentiment Reviews of Zico Coconut Water")
    ax.set_xlabel("Sentiments")
    ax.set_ylabel("Number of Reviews")
    fig.savefig("sentiment_plot.png")
    plt.show()


if __name__ == "__main__":
   
    sentiment_results = ["postive", "negative", "neutral", "irrelevant"]
    make_plot(sentiment_results)

    print(make_plot(sentiment_results))