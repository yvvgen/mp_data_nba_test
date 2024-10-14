import requests
import json

url = 'http://localhost:1717/predict'

with open('../data/test_data.json') as f:
    test_data = json.load(f)

response = requests.post(url, json=test_data).json()


if response['prediction']:
        print(f'{test_data['Name']} aura une carrière de plus de 5 ans : OUI')
else:
        print(f'{test_data['Name']} aura une carrière de plus de 5 ans : NON')