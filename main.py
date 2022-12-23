import os
import requests
# env
api_key = os.environ['API_KEY']

# endpoint 
api_url = 'https://newsapi.org/v2/top-headlines'

print("Enter the topic that you want to search for ")
q = input()

params = {
  "apiKey":api_key,
  "q": q,
  "pageSize" : 100,
  "page": 1,
  "language": "en"
}
response = requests.get(api_url,params=params)

if response.status_code == 200:
  print(response.json())
  