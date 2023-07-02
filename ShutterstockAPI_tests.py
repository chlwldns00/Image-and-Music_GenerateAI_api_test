import requests

url ='https://api.shutterstock.com/v2/audio/search'

headers = {
    'Authorization': 'Bearer v2/aVJWUXg0ZU1yNGhqazNVYkhRQ1dxNTUyQTJHNElPM08vMzg4OTk0Nzg3L2N1c3RvbWVyLzQvSzZITE1hZHBEcGdiVGZaMGpVX01BaTh3bUkyc3RiVnBNbkhCNWZlMlFVc1VmamppN21CV2RiX1U0TlZkeXN5MWlYa3V4UHkzU0VNRVpFa1RzSFRJWUxCZmY5bG5iZzNwV0JZTU9LZWtpbGVveVdCcXVGRUJTakdITFl4WF9kRlV3M25ROGg4OGRoNW03M3ZXVXEyME92SzRxT3JkTkVLTHc0TlFscDBNLVgyYVRNbjRRRjJhT3VwNTF1Vng1SmEtSm15bzNLVlA5bjdYZE9vVURmNEdTQS9mRDVTY0NQdkp2bnl4a2c4aHpLZ2FB'
}

params = {
    
}

response = requests.get(url, headers=headers, params={'per_page':80})
if response.status_code == 200:
    results = response.json()
    print(results)
    
else:
    print(f"Error searching audio: {response.status_code} - {response.text}")
