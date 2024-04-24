from django.urls import path

from .views import MyAPIView

urlpatterns = [
    # path('post', views.post, name='post'),
    path('api/data/', MyAPIView.as_view(), name='api-data'),
    # path('get', views.get, name='get'),
    # path("post", views.MyAPIView.post, name="post"),  # For handling POST requests
    # path("get", views.MyAPIView.get, name="get"),
]

# urlpatterns = [
#     path("post", views.post, name="post"),
#     # path("", views.index, name="index"),  # For handling GET requests
#     # path("post/", views.post, name="post"),
#     # path("post", views.MyAPIView.post, name="post"), # For handling POST requests
#     # path("get", views.MyAPIView.get, name="get"),
# ]
