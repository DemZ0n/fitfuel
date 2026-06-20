from django.urls import path

from .views import (
    home,
    foods,
    activities,
    summary,
    delete_food,
    delete_activity
)
from django.http import HttpResponse
from django.contrib.auth.models import User

def create_admin(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            'admin',
            'admin@gmail.com',
            'Admin123456'
        )
        return HttpResponse("Admin created")

    return HttpResponse("Admin already exists")

urlpatterns = [

    path('', home),

    path('foods/', foods),

    path('activities/', activities),

    path('summary/', summary),

    path('delete-food/<int:log_id>/', delete_food),

    path('delete-activity/<int:log_id>/', delete_activity),
]