import requests
import re 
from collections import Counter
import pandas as pd 
list=[]
dataframe = pd.DataFrame(columns=["url"])
headers = {
    'Host': 'graphql.api.dailymotion.com',
    # 'Content-Length': '1501',
    'Sec-Ch-Ua': '"Chromium";v="121", "Not A(Brand";v="99"',
    'X-Dm-Appinfo-Type': 'website',
    'X-Dm-Appinfo-Version': 'v2024-02-07T15:03:07.092Z',
    'Accept-Language': 'en-US',
    'Sec-Ch-Ua-Mobile': '?0',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhaWQiOiJmMWEzNjJkMjg4YzFiOTgwOTljNyIsInJvbCI6ImNhbi1tYW5hZ2UtcGFydG5lcnMtcmVwb3J0cyBjYW4tcmVhZC12aWRlby1zdHJlYW1zIGNhbi1zcG9vZi1jb3VudHJ5IGNhbi1hZG9wdC11c2VycyBjYW4tcmVhZC1jbGFpbS1ydWxlcyBjYW4tbWFuYWdlLWNsYWltLXJ1bGVzIGNhbi1tYW5hZ2UtdXNlci1hbmFseXRpY3MgY2FuLXJlYWQtbXktdmlkZW8tc3RyZWFtcyBjYW4tZG93bmxvYWQtbXktdmlkZW9zIGFjdC1hcyBhbGxzY29wZXMgYWNjb3VudC1jcmVhdG9yIGNhbi1yZWFkLWFwcGxpY2F0aW9ucyIsInNjbyI6InJlYWQgd3JpdGUgZGVsZXRlIGVtYWlsIHVzZXJpbmZvIGZlZWQgbWFuYWdlX3ZpZGVvcyBtYW5hZ2VfY29tbWVudHMgbWFuYWdlX3BsYXlsaXN0cyBtYW5hZ2VfdGlsZXMgbWFuYWdlX3N1YnNjcmlwdGlvbnMgbWFuYWdlX2ZyaWVuZHMgbWFuYWdlX2Zhdm9yaXRlcyBtYW5hZ2VfbGlrZXMgbWFuYWdlX2dyb3VwcyBtYW5hZ2VfcmVjb3JkcyBtYW5hZ2Vfc3VidGl0bGVzIG1hbmFnZV9mZWF0dXJlcyBtYW5hZ2VfaGlzdG9yeSBpZnR0dCByZWFkX2luc2lnaHRzIG1hbmFnZV9jbGFpbV9ydWxlcyBkZWxlZ2F0ZV9hY2NvdW50X21hbmFnZW1lbnQgbWFuYWdlX2FuYWx5dGljcyBtYW5hZ2VfcGxheWVyIG1hbmFnZV9wbGF5ZXJzIG1hbmFnZV91c2VyX3NldHRpbmdzIG1hbmFnZV9jb2xsZWN0aW9ucyBtYW5hZ2VfYXBwX2Nvbm5lY3Rpb25zIG1hbmFnZV9hcHBsaWNhdGlvbnMgbWFuYWdlX2RvbWFpbnMgbWFuYWdlX3BvZGNhc3RzIiwibHRvIjoiYkdkTEJ4OTRmMlJZWGtOVUZnVUJMMFVKYUJRVE1UWThIMDFfSWciLCJhaW4iOjEsImFkZyI6MSwiaWF0IjoxNzA3NTU0ODM4LCJleHAiOjE3MDc1OTAzOTIsImRtdiI6IjEiLCJhdHAiOiJicm93c2VyIiwiYWRhIjoid3d3LmRhaWx5bW90aW9uLmNvbSIsInZpZCI6IjNiNjk0N2NmLWU0ZDQtNDVhYi05Mzg0LTBjMjk2NWJhYWJiOSIsImZ0cyI6OTIyNjgwLCJjYWQiOjIsImN4cCI6MiwiY2F1IjoyLCJraWQiOiJBRjg0OURENzNBNTg2M0NEN0Q5N0QwQkFCMDcyMjQzQiJ9.lRc3vwrXf2U-tN4smLdvVY6Fdg-al3e72vDKKxOSn6k',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36',
    'Content-Type': 'application/json, application/json',
    'Accept': '*/*, */*',
    'X-Dm-Preferred-Country': 'in',
    'X-Dm-Neon-Ssr': '0',
    'X-Dm-Appinfo-Id': 'com.dailymotion.neon',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Origin': 'https://www.dailymotion.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.dailymotion.com/tseries2',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Priority': 'u=1, i',
    'Connection': 'close',
}
for page_no in range(1,6):
    data = '{"operationName":"CHANNEL_VIDEOS_QUERY","variables":{"channel_name":"tseries2","sort":"recent",'f'"page":{page_no},''"allowExplicit":true},"query":"fragment FRAG_VIDEO_BASE on Video {\\n  id\\n  xid\\n  title\\n  description\\n  thumbnail: thumbnailURL(size: \\"x240\\")\\n  thumbnailx60: thumbnailURL(size: \\"x60\\")\\n  thumbnailx120: thumbnailURL(size: \\"x120\\")\\n  thumbnailx240: thumbnailURL(size: \\"x240\\")\\n  thumbnailx360: thumbnailURL(size: \\"x360\\")\\n  thumbnailx480: thumbnailURL(size: \\"x480\\")\\n  thumbnailx720: thumbnailURL(size: \\"x720\\")\\n  bestAvailableQuality\\n  duration\\n  createdAt\\n  viewerEngagement {\\n    id\\n    liked\\n    favorited\\n    __typename\\n  }\\n  isExplicit\\n  canDisplayAds\\n  aspectRatio\\n  stats {\\n    id\\n    views {\\n      id\\n      total\\n      __typename\\n    }\\n    __typename\\n  }\\n  language {\\n    id\\n    codeAlpha2\\n    __typename\\n  }\\n  videoHeight: height\\n  videoWidth: width\\n  __typename\\n}\\n\\nquery CHANNEL_VIDEOS_QUERY($channel_name: String!, $sort: String, $page: Int!, $allowExplicit: Boolean) {\\n  channel(name: $channel_name) {\\n    id\\n    xid\\n    channel_videos_all_videos: videos(\\n      sort: $sort\\n      page: $page\\n      first: 100\\n      allowExplicit: $allowExplicit\\n    ) {\\n      pageInfo {\\n        hasNextPage\\n        nextPage\\n        __typename\\n      }\\n      edges {\\n        node {\\n          id\\n          ...FRAG_VIDEO_BASE\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}'
    # print(data)
    response = requests.post('https://graphql.api.dailymotion.com/', headers=headers, data=data, verify=False)
# exit()
# print(response.json)
    match = re.findall(r'"xid":"([^"]+)"', str(response.text))

    print(match)
    for i in match:
        if i not in list:
            list.append(i)

df=pd.DataFrame(list)
dataframe["url"]=list
# dataframe["url"]=dataframe["url"].drop_duplicates()
print(dataframe['url'].count)
# dataframe.to_csv("url.csv")
for i in match:
    print(i)
if match:
    xid_value = match.group(1)
    print(xid_value)
    
else:
    print("No match found.")
Number = dataframe
# Number=Number["url"].drop_duplicates()
def find_most_frequent_char(video_urls):

    all_urls = "".join(video_urls).lower()
    # all_urls = video_urls
    char_counter = Counter(all_urls)
    most_common_char, count = char_counter.most_common(1)[0]
    print(
        f"'{most_common_char}' : {count} "
    )


video_urls = Number["url"]

find_most_frequent_char(video_urls)