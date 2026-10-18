from django.contrib import admin
from django.urls import path, include
from events.views import event_registration

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("events.urls")),
    path(
        "api/events/<int:pk>/register/",
        event_registration,
        name="event-registration"
    ),
]
