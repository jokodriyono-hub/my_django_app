from django.urls import path
from .views import homePageView
from .views import HomePageView, AboutPageView

urlpatterns = [
    #path("", homePageView, name="home"),
    path("About/", AboutPageView.as_view(), name="About"),    
    path("", HomePageView.as_view(), name="Home"),    
]