from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sys

sys.path.append('../')
from modules import yt

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
    res= "result"
    url = request.POST['url']
    # audio_file_path = yt.download_shorts(url)
    # if audio_file_path is None:
    #     return HttpResponse("error occurred")
    result = {res: url}
    return JsonResponse(result)