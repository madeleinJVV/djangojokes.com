from django.urls import path
from pages.views import HomePageView, AboutUsView

app_name = 'pages'

urlpatterns = [
    path('',HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
]