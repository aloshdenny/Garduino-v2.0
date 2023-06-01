from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.home, name='home'),
    path("api/", views.get_alldata, name="modifyall"),
    path("api/<int:pk>/", views.modify_singleplant, name="modify_single"),
]