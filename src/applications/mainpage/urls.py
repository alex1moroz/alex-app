from django.urls import path

from applications.mainpage.apps import MainpageConfig
from applications.mainpage.views import IndexView

app_name = MainpageConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
