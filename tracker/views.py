from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import date

from .models import FoodLog, ActivityLog
from .forms import FoodLogForm, ActivityLogForm

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


# HOME PAGE

def home(request):

    return render(request, 'tracker/home.html')


# FOOD PAGE

def foods(request):

    food_form = FoodLogForm()

    if request.method == 'POST':

        food_form = FoodLogForm(request.POST)

        if food_form.is_valid():
            food_form.save()

            return redirect('/foods/')

    today = date.today()

    food_logs = FoodLog.objects.filter(date=today)

    context = {
        'food_form': food_form,
        'food_logs': food_logs,
    }

    return render(request, 'tracker/foods.html', context)


# ACTIVITY PAGE

def activities(request):

    activity_form = ActivityLogForm()

    if request.method == 'POST':

        activity_form = ActivityLogForm(request.POST)

        if activity_form.is_valid():
            activity_form.save()

            return redirect('/activities/')

    today = date.today()

    activity_logs = ActivityLog.objects.filter(date=today)

    context = {
        'activity_form': activity_form,
        'activity_logs': activity_logs,
    }

    return render(request, 'tracker/activities.html', context)


# SUMMARY PAGE

def summary(request):

    today = date.today()

    food_logs = FoodLog.objects.filter(date=today)
    activity_logs = ActivityLog.objects.filter(date=today)

    calories_consumed = 0
    protein = 0
    carbs = 0
    fat = 0
    sugar = 0

    for log in food_logs:

        factor = log.quantity_grams / 100

        calories_consumed += log.food.calories * factor
        protein += log.food.protein * factor
        carbs += log.food.carbs * factor
        fat += log.food.fat * factor
        sugar += log.food.sugar * factor

    calories_burned = 0

    for log in activity_logs:
        
        duration_hours = log.duration_minutes / 60
        
        if log.activity.category == "Gym":
            
            if (
                log.sets > 0 and
                log.reps > 0 and
                log.weight_lifted_kg > 0
                ):
                
                calories_burned += (
                    log.activity.met_value *
                    log.body_weight_kg *
                    duration_hours
                    ) + (
                        log.sets *
                        log.reps *
                        log.weight_lifted_kg *
                        0.01
                        )
                
        else:
            calories_burned += (
                log.activity.met_value *
                log.body_weight_kg *
                duration_hours
                )

    net_calories = calories_consumed - calories_burned

    context = {

        'calories_consumed': round(calories_consumed, 2),
        'calories_burned': round(calories_burned, 2),
        'net_calories': round(net_calories, 2),

        'protein': round(protein, 2),
        'carbs': round(carbs, 2),
        'fat': round(fat, 2),
        'sugar': round(sugar, 2),
    }

    return render(request, 'tracker/summary.html', context)


# DELETE FOOD

def delete_food(request, log_id):

    food_log = FoodLog.objects.get(id=log_id)

    food_log.delete()

    return redirect('/foods/')


# DELETE ACTIVITY

def delete_activity(request, log_id):

    activity_log = ActivityLog.objects.get(id=log_id)

    activity_log.delete()

    return redirect('/activities/')