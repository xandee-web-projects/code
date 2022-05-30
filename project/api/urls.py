from . import views
from django.urls import path

urlpatterns = [path("check_code/<int:area_code>/", views.get_numbers)]