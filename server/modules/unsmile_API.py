import requests

API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/smilegate-ai/kor_unsmile"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(text):
    payload = {'inputs': text, }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

if __name__=="__main__":
    output = query(input('텍스트 입력: '))

    print(output)