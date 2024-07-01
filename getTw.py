import requests
import os
import sys

args = sys.argv
from dotenv import load_dotenv

load_dotenv()

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAALoijwEAAAAA8g2j50bcnjHow3FdKSliZ6Y%2FtvQ%3D5AZIt8BnxeZgbU8hunihLaV1sILgmxZwj41ndi0DAIr37X5Vvo'

userid = '857422934847086592'

search_url = f"https://api.twitter.com/2/users/{userid}/tweets"


syymmdd = args[1]
eyymmdd = args[2]
start_time = f'{syymmdd}T00:00:00Z'
end_time = f'{eyymmdd}T00:00:00Z'

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {"tweet.fields":"attachments","expansions":"attachments.media_keys","media.fields":"url","max_results":100, "start_time":start_time, "end_time":end_time}

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
    # json_result = json.dumps(json_response, indent=4, sort_keys=True)
    # print(json_result[0])
    print(len(json_response['data']))
    for tweet in json_response['data']:
        if 'attachments' in tweet:
            try :
              for media_key in tweet['attachments']['media_keys']:
                  for media in json_response['includes']['media']:
                      if media['media_key'] == media_key:
                          # 画像のURLを取得します。
                            if media['type'] == 'photo':
                              url = media['url']
                              response = requests.get(url, stream=True)
                              if response.status_code == 200:
                                  with open(os.path.join('imgs', url.split('/')[-1]), 'wb') as f:
                                      f.write(response.content)

            except Exception :
                print(tweet)

# 2021-08-01以前未取得
# 2021-08中旬大量同一画像
main()
