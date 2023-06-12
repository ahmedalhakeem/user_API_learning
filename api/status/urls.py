from django.urls import path
from . import views

urlpatterns= [
    path("status/", views.StatusCreateListApi.as_view(), name="status"),
    path("change_status/<int:pk>/", views.RetrieveUpdateDeleteStatus.as_view(), name="change")
    
]