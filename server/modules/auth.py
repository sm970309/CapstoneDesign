import requests

def get_auth():    
    url = 'https://openapi.vito.ai/v1/authenticate'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'client_id': 'cnmHnK76zCvWY_piiHN2', 'client_secret': 'IaFtQHwvBOgE9AHG3kuZz3OsWE9hzGA9XeNV-4m4'}

    response = requests.post(url, headers=headers, data=data)
    response_json = response.json()

    if response.status_code == 200:
        access_token = response_json['access_token']
    else:
        print(f"Error: {response_json['error_description']}")
    return access_token