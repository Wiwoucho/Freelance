import requests, uuid, json

# Add your key and endpoint
key = "Your-Azure-Key"
endpoint = "Your-Azure-Endpoint"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "your-location"

path = 'translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': 'bg'
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

with open("filename-to-read-from", "r") as f, open("filename-to-append-data-in", "wb") as g:
    for line in f:
        line = [{
            'text': line
        }]
        request = requests.post(constructed_url, params=params, headers=headers, json=line)
        response = request.json()
        last_response = response[0]['translations'][0]['text']
        b = last_response.encode('utf-8')
        g.write(b)