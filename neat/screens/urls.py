from django.urls import path

from . import views

urlpatterns = [
    path("main-screen/<int:presentation_id>/", views.index, name="index"),
    path("get-slot-page", views.get_slot_page, name="get-slot-page"),
]
