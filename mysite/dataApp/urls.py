from django.urls import path

from .views import MyAPIView

urlpatterns = [
    path('api/data/', MyAPIView.as_view(), name='api-data'),
    # path('api/add_data/', MyAPIView.as_view(methods=['post']), name='api-add-data'),

    # path('api/add_data/', MyAPIView.add_data, name='api-add-data'),
]

# urlpatterns = [
#     path("post", views.post, name="post"),
#     # path("", views.index, name="index"),  # For handling GET requests
#     # path("post/", views.post, name="post"),
#     # path("post", views.MyAPIView.post, name="post"), # For handling POST requests
#     # path("get", views.MyAPIView.get, name="get"),
# ]
