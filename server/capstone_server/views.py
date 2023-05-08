from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sys
from kss import split_sentences

sys.path.append('../')
from modules import yt,stt,unsmile

article = '''
<!DOCTYPE html>
<html>
  <head>
    <title>Android Studio</title>
  </head>
  <body>
    <h1>UI 구현부분</h1>
    <form method="post" action="/check/">
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
    result = stt.makeTextline(res_id)
    all_text= ''
    for t in result['results']['utterances']:
        all_text +=t['msg']
    texts = split_sentences(all_text)
    print(texts)
    for text in texts:
        print(text,unsmile.calcScore(text))

    # html에서 한글 깨지는 거 수정
    return JsonResponse({'result':texts},json_dumps_params={'ensure_ascii': False}, status=200)