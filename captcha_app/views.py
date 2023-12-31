import random
from rest_framework import generics
from rest_framework.response import Response
from .serializers import PostCaptchaSerializer
from .captcha import generate_captcha, redis_connection  # , generate_captcha_text
from core.settings import path_of_captcha_picture as path


class CreateAndVerifyCaptcha(generics.RetrieveAPIView):
    serializer_class = PostCaptchaSerializer

    def get(self, request, *args, **kwargs) -> Response:
        captcha_text = ''.join(random.choice('0123456789') for _ in range(4))
        generate_captcha(captcha_text, path)
        return Response()

    def post(self, request, *args, **kwargs) -> Response:
        captcha = request.data.get("captcha")
        uid = request.data.get("uid")
        cached_captcha = redis_connection.get(uid)
        redis_connection.delete(uid)
        if cached_captcha == captcha:
            return Response({'message': 'Captcha verification successful'})
        return Response({'message': 'Captcha verification failed. Please try again'})
