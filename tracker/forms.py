from django import forms
from .models import FoodLog, ActivityLog


class FoodLogForm(forms.ModelForm):

    class Meta:
        model = FoodLog
        fields = ['food', 'quantity_grams']

    def clean_quantity_grams(self):
        quantity = self.cleaned_data['quantity_grams']

        if quantity <= 0:
            raise forms.ValidationError(
                "Quantity must be greater than 0."
            )

        return quantity


class ActivityLogForm(forms.ModelForm):

    class Meta:
        model = ActivityLog
        fields = [
            'activity',
            'duration_minutes',
            'body_weight_kg',
            'sets',
            'reps',
            'weight_lifted_kg'
        ]

    def clean_duration_minutes(self):
        duration = self.cleaned_data['duration_minutes']

        if duration <= 0:
            raise forms.ValidationError(
                "Duration must be greater than 0."
            )

        return duration

    def clean_body_weight_kg(self):
        weight = self.cleaned_data['body_weight_kg']

        if weight <= 0:
            raise forms.ValidationError(
                "Body weight must be greater than 0."
            )

        return weight
