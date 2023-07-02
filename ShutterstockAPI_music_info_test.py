import requests


###내가생성한 음악의 키워드,아티스트 네임, 장르,분위기,bpm,악기,짧게 잘라놓은 음악  등 여러가지 정보를 요청할수있다.2
idd='512444'
url='https://api.shutterstock.com/v2/audio/'+idd+'?view=full&search_id=00000000-0000-0000-0000-000000000000'

headers = {
    'Authorization': 'Bearer v2/aVJWUXg0ZU1yNGhqazNVYkhRQ1dxNTUyQTJHNElPM08vMzg4OTk0Nzg3L2N1c3RvbWVyLzQvSzZITE1hZHBEcGdiVGZaMGpVX01BaTh3bUkyc3RiVnBNbkhCNWZlMlFVc1VmamppN21CV2RiX1U0TlZkeXN5MWlYa3V4UHkzU0VNRVpFa1RzSFRJWUxCZmY5bG5iZzNwV0JZTU9LZWtpbGVveVdCcXVGRUJTakdITFl4WF9kRlV3M25ROGg4OGRoNW03M3ZXVXEyME92SzRxT3JkTkVLTHc0TlFscDBNLVgyYVRNbjRRRjJhT3VwNTF1Vng1SmEtSm15bzNLVlA5bjdYZE9vVURmNEdTQS9mRDVTY0NQdkp2bnl4a2c4aHpLZ2FB'
}

params = {
    
}

response = requests.get(url, headers=headers, params={"id":"512444"})

if response.status_code == 200:
    print(response.json())
    results_genre = response.json()['genres']
    results_inst=response.json()['instruments']
    #print(type(results_genre))
    print(results_genre)
    print(results_inst)
    
else:
    print(f"Error searching audio: {response.status_code} - {response.text}")

