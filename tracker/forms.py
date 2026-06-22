from django import forms
from .models import FoodLog, ActivityLog


class FoodLogForm(forms.ModelForm):
    class Meta:
        model = FoodLog
        fields = ['food', 'quantity_grams']


class ActivityLogForm(forms.ModelForm):
    class Meta:
        model = ActivityLog
        fields = ['activity', 'duration_minutes', 'body_weight_kg', 'sets', 'reps', 'weight_lifted_kg' ]