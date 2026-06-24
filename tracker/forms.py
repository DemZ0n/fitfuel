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
        value = self.cleaned_data['duration_minutes']

        if value < 1:
            raise forms.ValidationError(
                "Duration must be at least 1 minute."
            )

        if value > 600:
            raise forms.ValidationError(
                "Duration cannot exceed 600 minutes."
            )

        return value

    def clean_body_weight_kg(self):
        value = self.cleaned_data['body_weight_kg']

        if value < 20:
            raise forms.ValidationError(
                "Body weight must be at least 20 kg."
            )

        if value > 300:
            raise forms.ValidationError(
                "Body weight cannot exceed 300 kg."
            )

        return value

    def clean_sets(self):
        value = self.cleaned_data['sets']

        if value < 0:
            raise forms.ValidationError(
                "Sets cannot be negative."
            )

        if value > 20:
            raise forms.ValidationError(
                "Sets cannot exceed 20."
            )

        return value

    def clean_reps(self):
        value = self.cleaned_data['reps']

        if value < 0:
            raise forms.ValidationError(
                "Reps cannot be negative."
            )

        if value > 100:
            raise forms.ValidationError(
                "Reps cannot exceed 100."
            )

        return value

    def clean_weight_lifted_kg(self):
        value = self.cleaned_data['weight_lifted_kg']

        if value < 0:
            raise forms.ValidationError(
                "Weight lifted cannot be negative."
            )

        if value > 1000:
            raise forms.ValidationError(
                "Weight lifted cannot exceed 1000 kg."
            )

        return value
