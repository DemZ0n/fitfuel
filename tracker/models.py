from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    sugar = models.FloatField()

    def __str__(self):
        return self.name


class Activity(models.Model):
    CATEGORY_CHOICES = [
        ('Cardio', 'Cardio'),
        ('Gym', 'Gym'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
    max_length=20,
    choices=CATEGORY_CHOICES,
    default='Cardio'
    )
    met_value = models.FloatField()
    target_muscle = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


# -----------------------
# FOOD LOG (USER INPUT)
# -----------------------
class FoodLog(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity_grams = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.food.name} - {self.quantity_grams}g"


# -----------------------
# ACTIVITY LOG (USER INPUT)
# -----------------------
class ActivityLog(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    duration_minutes = models.FloatField()
    body_weight_kg = models.FloatField()

    sets = models.IntegerField(null=True, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    weight_lifted_kg = models.FloatField(null=True, blank=True)

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity.name}"