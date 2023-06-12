import os
import arabic_reshaper
import uuid
import redis

from captcha.image import ImageCaptcha
from bidi.algorithm import get_display


redis_connection = redis.Redis(host="localhost", port=6379, db=0, charset="utf-8", decode_responses=True)


def generate_captcha(text, save_path) -> None:
    uid = str(uuid.uuid4())
    image_captcha = ImageCaptcha(fonts=['/usr/share/fonts/truetype/farsiweb/nazli.ttf'])
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    image = image_captcha.generate(bidi_text)
    redis_connection.set(uid, text, ex=120)
    image_path = os.path.join(save_path, f"{uid}.png")
    print(f'uid: {uid}, captcha_text: {text}')
    with open(image_path, 'wb') as f:
        f.write(image.getvalue())
