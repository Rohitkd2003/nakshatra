from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Meal(models.Model):
    CONDITION_CHOICES = (
        ('PCOD', 'PCOD'),
        ('Fertility', 'Fertility'),
        ('General', 'General'),
        ('Hormonal', 'Hormonal'),
        ('weight_loss', 'Weight Loss'),
        ('weight_gain', 'Weight Gain'),
        ('diabetes', 'Diabetes'),
        ('healthy', 'Healthy'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    calories = models.IntegerField()
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES, default='General')
    preparation_time = models.IntegerField(help_text="minutes", default=0)
    servings = models.IntegerField(default=1)
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MealIngredient(models.Model):
    meal = models.ForeignKey(Meal, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100, blank=True)
    unit = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.name} ({self.meal.name})"


class MealLog(models.Model):
    patient = models.ForeignKey(User, related_name='meal_logs', on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, related_name='logs', on_delete=models.SET_NULL, null=True)
    meal_name = models.CharField(max_length=200)  # snapshot
    date = models.DateField()
    time = models.TimeField()
    quantity = models.FloatField(default=1.0)
    calories = models.IntegerField()
    custom_calories = models.IntegerField(null=True, blank=True)
    logged_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.calories and self.meal:
            self.calories = self.meal.calories
        super().save(*args, **kwargs)


class CalorieEntry(models.Model):
    patient = models.ForeignKey(User, related_name='calorie_entries', on_delete=models.CASCADE)
    food_description = models.CharField(max_length=300)
    calories = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_description} - {self.calories}"


class MealPlan(models.Model):
    CONDITION_CHOICES = [
        ('weight_gain', 'Weight Gain'),
        ('weight_loss', 'Weight Loss'),
        ('maintenance', 'Maintenance'),
    ]

    name = models.CharField(max_length=255)
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mealplans')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MealPlanItem(models.Model):
    mealplan = models.ForeignKey(MealPlan, on_delete=models.CASCADE, related_name='items')
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)
    servings = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.meal.name} in {self.mealplan.name}"