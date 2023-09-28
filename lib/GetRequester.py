import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_content = self.get_response_body()
        json_data = json.loads(response_content.decode('utf-8'))  # Decode bytes to a UTF-8 string
        return json_data

# Example usage:
# get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
# print(get_requester.load_json())
