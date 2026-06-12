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
    name = models.CharField(max_length=100)
    met_value = models.FloatField()  # MET value

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
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity.name} - {self.duration_minutes} min"