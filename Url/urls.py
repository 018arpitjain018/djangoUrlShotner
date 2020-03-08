from django.urls import path
from Url.views import url_hit

urlpatterns = [
    path('<str:short_url>/', url_hit)
]