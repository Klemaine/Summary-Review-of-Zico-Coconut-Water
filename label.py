from openai import OpenAI


def get_sentiment(text: list) -> list:
    """
    Analyzes the sentiment of text reviews and categorizes them into positive, neutral, negative, or irrelevant.

    Args:
        text (list): A list of strings containing text reviews.

    Returns:
        list: A list of sentiment categories corresponding to each review.
    
    """
    
    
    if not isinstance(text, list) or not all(isinstance(item, str) for item in text) or not text:
        return "Wrong input. text must be an array of strings." 
        
    client = OpenAI()
    
    system_prompt = f"""
    You are a sentiment analysis expert who specialize in reviews. Attached is a list of reviews of Zico Coconut Water,
    using your expertise, analyze each review critically to acertain the sentiment.    
    Once you are done, please sort these reviews into four categories, "positive", "negative", "neutral" or "irrelevant".
    """

    user_prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers. 
    {text}
    """

    text_response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return text_response.choices[0].message.content.strip().split()
