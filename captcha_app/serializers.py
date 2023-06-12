from rest_framework import serializers
from .captcha import generate_captcha


class PostCaptchaSerializer(serializers.Serializer):
    captcha = serializers.CharField(max_length=4)
    uid = serializers.CharField()

    def validate_captcha(self, captcha: str) -> str:
        if not captcha.isnumeric():
            raise serializers.ValidationError("Please Enter Valid Amount")
        return captcha
