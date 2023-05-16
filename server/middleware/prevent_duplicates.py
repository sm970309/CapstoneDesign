from django.core.cache import cache

class PreventDuplicateRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 요청의 고유 식별자 생성
        request_identifier = self.generate_request_identifier(request)

        # 이미 처리된 요청인지 확인
        if cache.get(request_identifier):
            # 이미 처리된 요청인 경우 처리하지 않고 바로 응답 반환
            print('중복요청')
            return HttpResponse("Duplicate request detected.")

        # 처리된 요청이 아니면 캐시에 저장
        cache.set(request_identifier, True, timeout=60)  # 적절한 타임아웃 설정

        # 다음 미들웨어 또는 뷰로 요청 전달
        response = self.get_response(request)

        return response

    def generate_request_identifier(self, request):
        # 요청의 고유 식별자를 생성하는 로직 구현
        # 예시로는 POST 데이터와 URL 경로를 기반으로 생성하도록 했습니다.
        # 필요에 따라 고유 식별자 생성 로직을 변경해야 할 수도 있습니다.
        data = request.POST.dict()
        path = request.path
        identifier = f"{path}:{data}"
        return identifier