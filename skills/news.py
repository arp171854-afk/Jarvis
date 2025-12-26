import requests

def get_news(api_key="59da96c31cba4404b9933d0aa2d88c76"):
    """
    Fetches top headlines for India using NewsAPI.
    """
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    try:
        articles = requests.get(url, timeout=8).json().get("articles", [])
        if articles:
            headlines = [a.get("title","No title") for a in articles[:3]]
            return headlines
        else:
            return ["No headlines available at the moment."]
    except:
        return ["News service is not responding."]
