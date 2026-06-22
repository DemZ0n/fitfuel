from django.urls import path

from .views import (
    home,
    foods,
    activities,
    summary,
    delete_food,
    delete_activity,
    create_admin
)


urlpatterns = [

    path('', home),

    path('foods/', foods),

    path('activities/', activities),

    path('summary/', summary),

    path('delete-food/<int:log_id>/', delete_food),

    path('delete-activity/<int:log_id>/', delete_activity),

    path('create-admin/', create_admin),
]
