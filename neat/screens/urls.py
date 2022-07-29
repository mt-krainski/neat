from django.urls import path

from . import views

urlpatterns = [
    path("main-screen/<int:presentation_id>/<int:page>/", views.index, name="index"),
    path("main-screen/<int:presentation_id>/", views.index, name="index"),
    path("test-drive", views.test_drive, name="test drive"),
]
