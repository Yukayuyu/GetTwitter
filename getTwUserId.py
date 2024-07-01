import requests
import os
import json
import re

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAALoijwEAAAAA8g2j50bcnjHow3FdKSliZ6Y%2FtvQ%3D5AZIt8BnxeZgbU8hunihLaV1sILgmxZwj41ndi0DAIr37X5Vvo'

username = 'cogimyun_sanrio'

search_url = f"https://api.twitter.com/2/users/by/username/{username}"


query_string = ''
# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'user.fields': 'id,name'}

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def main():
    json_response = connect_to_endpoint(search_url, query_params)
    json_result = json.dumps(json_response, indent=4, sort_keys=True)
    print(json_result)


main()
