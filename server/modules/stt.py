import requests
import json
import time
if __name__ != '__main__':    
    from modules import auth
    access_token = auth.get_auth()

    URL = 'https://openapi.vito.ai/v1/transcribe'
    config = {
    "diarization": {
        "use_verification": False,
        # "user_id": "user-id-1",
        # "partner_id": "partner-id-1"
    },
    "use_multi_channel": False,
    "use_disfluency_filter": True,
    }
    headers = {
        'Authorization': f'bearer {access_token}',
    }
    data = {
        'config': {json.dumps(config)}
    }



def useAPI(audio_file_path):
    
    files = {'file': open(audio_file_path, 'rb')}    
    res = requests.post(URL, headers=headers, data=data, files=files)
    res_id=res.json()['id']
    return res_id

def makeTextline(res_id):
    while True:
        text = requests.get(url=f'{URL}/{res_id}',headers=headers)
        if text.json()['status']=='transcribing':
            print(text.json()['status'])
            time.sleep(5)
            continue
        elif text.json()['status']=='failed':
            text= json.dumps({'result':'error'})
            break
        else:
            break
    return text.json()

if __name__ == '__main__':
    import auth
    access_token = auth.get_auth()
    
    URL = 'https://openapi.vito.ai/v1/transcribe'
    config = {
    "diarization": {
        "use_verification": False,
        # "user_id": "user-id-1",
        # "partner_id": "partner-id-1"
    },
    "use_multi_channel": False,
    "use_disfluency_filter": True,
    }
    headers = {
        'Authorization': f'bearer {access_token}',
    }
    data = {
        'config': {json.dumps(config)}
    }

    res_id= useAPI(input("파일 경로를 입력하세요 : "))
    text = makeTextline(res_id)
    print(text)

