from . import views
from rest_framework.urls import path


urlpatterns = [
    path('captcha/', views.CreateAndVerifyCaptcha.as_view(), name="get_captcha"),
]





