from django.urls import path

from . import views

urlpatterns = [
    path("main-screen/<int:slot_id>/", views.main_screen, name="index"),
    path("presenter-screen/<int:slot_id>/", views.presenter_screen, name="index"),
    path("get-slot-page", views.get_slot_page, name="get-slot-page"),
]
