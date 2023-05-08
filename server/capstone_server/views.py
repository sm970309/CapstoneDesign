from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sys

sys.path.append('../')
from modules import yt,stt

article = '''
<!DOCTYPE html>
<html>
  <head>
    <title>Android Studio</title>
  </head>
  <body>
    <h1>UI 구현부분</h1>
    <form method="get" action="/check/">
      <label for="id">URL:</label>
      <input type="text" id="id" name="url">
      <br>
      <input type="submit" value="Submit">
    </form>
  </body>
</html>

    '''
def index(request):
    return HttpResponse(article)

@csrf_exempt
def check(request):
    url = request.POST['url']
    audio_file_path = yt.download_shorts(url)
    if audio_file_path is None:
        return HttpResponse("error occurred")
    res_id = stt.useAPI(audio_file_path)
    text = stt.makeTextline(res_id)
    
    # 프론트 연동 테스트용
    # result = {'result': url}
    # return JsonResponse(result)
    # html에서 한글 깨지는 거 수정
    return JsonResponse(text,json_dumps_params={'ensure_ascii': False}, status=200)