from django.urls import path

from . import views

urlpatterns = [
    path("main-screen/", views.main_screen, name="main-screen"),
    path(
        "presenter-screen/<int:slot_id>/",
        views.presenter_screen,
        name="presenter-screen",
    ),
    path("get-slot-page", views.get_slot_page, name="get-slot-page"),
    path("get-active-slot", views.get_active_slot, name="get-active-slot"),
]
