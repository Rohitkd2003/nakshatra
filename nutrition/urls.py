from django.urls import path
from .views import (
    MealListView,
    MealDetailView,
    MealLogCreateView,
    MealLogListView,
    CalorieEntryCreateView,
    MealPlanAddFoodView,
)

urlpatterns = [
    path('meals/', MealListView.as_view(), name='meals'),  # GET list, POST create
    path('meals/<int:id>/', MealDetailView.as_view(), name='meal-detail'), # GET single meal
    path('meal-logs/', MealLogCreateView.as_view(), name='meal-logs'), # POST
    path('meal-logs/list/', MealLogListView.as_view(), name='meal-logs-list'), # GET
    path('calorie-entry/', CalorieEntryCreateView.as_view(), name='calorie-entry'), # POST
    path('mealplan/<int:pk>/add-food/', MealPlanAddFoodView.as_view(), name='mealplan-add-food'),

    path('mealplan/<int:pk>/add-food/', MealPlanAddFoodView.as_view(), name='mealplan-add-food'),
]
