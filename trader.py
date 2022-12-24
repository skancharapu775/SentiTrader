import requests
import os
import json
import yfinance as yf


# Stocks with historically high percentage of retail investors
company_terms = {
"TSLA": ["Tesla", "TSLA", "electric car", "Elon Musk"],
"FB": ["Meta", "Facebook", "Metaverse", "Mark Zuckerberg"],
"APPL": ["iPhone", "phone", "iPad", "AppleTV", "AppleTV"],
"GOOGL": ["Google", "website", ""],
"AMZN": ["Amazon", "amazon prime", "Jeff Bezos", "Bezos", "Whole Foods"],
"BTC-USD": ["crypto", "bitcoin", "decentralized"],
"WFC": ["Wells Fargo", "Charles Scharf", "first clearing"],
"NKE": ["nike", "John Donahoe"],
"LVMH": ["LVMH", "Louis Vuitton", "Bernard Arnault", "Fendi", "Givenchi"],
"PARA": ["Paramount", "Brian Robbins"],
}

company_names = company_terms.keys()
summary = []

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/2/tweets/search/all"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': '(from:twitterdev -is:retweet) OR #twitterdev','tweet.fields': 'author_id'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()





