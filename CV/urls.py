from django.urls import path
from . import views

urlpatterns = [
    path("", views.CV, name="CV"),
    # other url patterns...
]