import requests

def fetch_news(api_key, query="technology", page_size=10):
    url = f"https://newsapi.org/v2/everything?q={query}&pageSize={page_size}&apiKey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        news_data = response.json()
        return news_data.get("articles", [])
    else:
        print("Error fetching news:", response.status_code, response.text)
        return []


def fetch_random_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    
    if response.status_code == 200:
        joke_data = response.json()
        if joke_data["type"] == "single":
            return joke_data["joke"]  # Return single-line joke
        else:
            return f"{joke_data['setup']} - {joke_data['delivery']}"  # Return two-part joke
    else:
        print("Error fetching joke:", response.status_code, response.text)
        return "Oops! Could not fetch a joke at the moment."