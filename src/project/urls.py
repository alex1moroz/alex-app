from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path

from project.views import view_favicon

urlpatterns = [
    # --- admin urls ---
    path("admin/", admin.site.urls),
    # --- static views ---
    path("favicon.ico", view_favicon, name="favicon"),
    # --- applications ---
    path("", include("applications.mainpage.urls")),
]

if settings.DEBUG and settings.PROFILING:  # pragma: no cover
    urlpatterns.append(re_path(r"^silk/", include("silk.urls", namespace="silk")))
