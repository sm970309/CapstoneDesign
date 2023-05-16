import requests
import json

# POST 요청을 보낼 URL
url = 'http://127.0.0.1:8000/check/'

# JSON 데이터 준비
data = {
    'url': 'https://www.youtube.com/shorts/ju2z9wIgIfQ'
}

# JSON 형식으로 데이터 직렬화
json_data = json.dumps(data)

# POST 요청 보내기
response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

# 응답 확인
if response.status_code == 200:
    # 응답 JSON 데이터 파싱
    response_data = response.json()
    # 응답 데이터 처리
    # ...
    print(response_data)