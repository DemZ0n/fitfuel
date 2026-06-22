from django.contrib import admin
from .models import Food, Activity, FoodLog, ActivityLog

admin.site.register(Food)
admin.site.register(Activity)
admin.site.register(FoodLog)
admin.site.register(ActivityLog)

