import requests

API_URL = "https://api.api-ninjas.com/v1/dadjokes"

def get_joke(api_key):
    headers = {'X-Api-Key': api_key}
    response = requests.get(API_URL, headers=headers)
    if response.status_code == requests.codes.ok:
        joke_data = response.json()[0]
        return joke_data['joke']
    else:
        return f"Time flies like an arrow. Fruit flies like a banana."
# page 146