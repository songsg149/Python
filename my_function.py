import requests

# Make a GET request to a URL
response = requests.get('https://www.hyundai.com/sk/sk/modely/kona-hybrid/konfigurator.html#/trims')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the content of the response
    print(response.text)
else:
    print('Request failed with status code:', response.status_code)