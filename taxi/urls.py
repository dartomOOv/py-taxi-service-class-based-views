from django.urls import path

from .views import (index,
                    CarListView,
                    CarDetailView,
                    DriverListView,
                    DriverDetailView,
                    ManufacturerListView)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturer/",
        ManufacturerListView.as_view(),
        name="manufacturer-list"
    ),
    path("car/", CarListView.as_view(), name="car-list"),
    path("car/p<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("driver/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
]

app_name = "taxi"
