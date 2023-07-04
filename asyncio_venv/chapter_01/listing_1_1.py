import requests

responce = requests.get('https://www.example.com')
items = responce.headers.items()

headers = [f"{key} : {header}" for key, header in items]

formatted_headers = '\n'.join(headers)

print(formatted_headers)

with open('headers.txt', 'w') as file:
    file.write(formatted_headers)