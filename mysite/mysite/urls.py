
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("dataApp/", include("dataApp.urls")),
    path('admin/', admin.site.urls),
]
